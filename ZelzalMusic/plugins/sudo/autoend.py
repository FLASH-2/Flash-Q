

from ZelzalMusic.plugins.play.filters import command
from pyrogram import filters
from pyrogram.types import Message

from ZelzalMusic import app
from ZelzalMusic.misc import SUDOERS
from ZelzalMusic.utils.database import autoend_off, autoend_on


@app.on_message(command(["المغادره التلقائية", "المغادره التلقائيه"]) & SUDOERS)
async def auto_end_stream(_, message: Message):
    usage = "<b>• مثــال :</b>\n\nالمغادره التلقائيه [تفعيل | تعطيل]"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip().lower()
    if state == "on":
        await autoend_on()
        await message.reply_text(
            "» تم تفعيل المغادرة التلقائية للمساعد .. بنجاح\n\nالحساب المساعد سوف يقوم بمغادرة الدردشة تلقائياً .. عند عدم وجود اشخاص في المكالمة"
        )
    elif state == "off":
        await autoend_off()
        await message.reply_text("» تم تعطيل وضع المغادرة التلقائية للمساعد .. بنجاح.")
    else:
        await message.reply_text(usage)
