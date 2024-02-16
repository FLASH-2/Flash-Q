from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from ZelzalMusic import app

@app.on_message(filters.incoming & filters.private, group=-2)
async def MUST_JOINN_channel(bot: Client, msg: Message):
    if not "https://t.me/FLS_45":  # Not compulsory
        return
    try:
        try:
            await bot.get_chat_member("FLS_45", msg.from_user.id)
        except UserNotParticipant:
            if "https://t.me/FLS_45".isalpha():
                link = "https://t.me/FLS_45"
            else:
                chat_info = await bot.get_chat("FLS_45")
                link = chat_info.invite_link
            try:
                await msg.reply(
                    f"❃︙عذࢪاَ عزيزي ↫ {msg.from_user.mention} \n❃︙عـليك الاشـتࢪاك في قنـاة البـوت اولآ .\nꔹ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ꔹ",
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("« ᥴ𝗁ᥲᥒᥒᥱᥣ ᥉᥆υᖇᥴᥱ »", url=link)]
                    ])
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"I m not admin in the MUST_JOINN chat @FLS_45 !")