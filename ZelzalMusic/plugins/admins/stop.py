

from ZelzalMusic.plugins.play.filters import command
from pyrogram import filters
from pyrogram.types import Message

from ZelzalMusic import app
from ZelzalMusic.core.call import Zelzaly
from ZelzalMusic.utils.database import set_loop
from ZelzalMusic.utils.decorators import AdminRightsCheck
from ZelzalMusic.utils.inline import close_markup
from config import BANNED_USERS


@app.on_message(
    command(["/stop", "اسكت", "انهاء", "ايقاف", "ب"]) & ~BANNED_USERS
)
@AdminRightsCheck
async def stop_music(cli, message: Message, _, chat_id):
    if " " in message.text:
        return
    await Zelzaly.stop_stream(chat_id)
    await set_loop(chat_id, 0)
    user_mention = message.from_user.mention if message.from_user else "المشـرف"
    await message.reply_text(
        _["admin_5"].format(user_mention), reply_markup=close_markup(_)
    )
