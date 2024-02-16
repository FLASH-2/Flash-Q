from config import MUST_JOINN

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from ZelzalMusic import app


@app.on_message(filters.incoming & filters.private, group=-2)
async def MUST_JOINN_channel(bot: Client, msg: Message):
    if not MUST_JOINN:
        return
    try:
        try:
            await bot.get_chat_member(MUST_JOINN, msg.from_user.id)
        except UserNotParticipant:
            if MUST_JOINN.isalpha():
                link = "https://t.me/FLS_45" + MUST_JOINN
            else:
                chat_info = await bot.get_chat(MUST_JOINN)
                link = chat_info.invite_link
            try:
                await msg.reply_photo(
                    photo="https://telegra.ph/file/738661f85fe3e4fd54d20.jpg", caption=f"عليك الإنضمام إلى جروب السورس [جروب السورس]({link}) وبعدها حاول مرة اخرى !",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("« ᘜᖇ᥆υρ ᥉᥆υᖇᥴᥱ »", url=link),
                            ]
                        ]
                    )
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"Promote me as an admin in the MUST_JOINN chat : @FLS_45 !")
