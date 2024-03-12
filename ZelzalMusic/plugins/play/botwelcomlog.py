
from pyrogram import Client, filters
from pyrogram.types import Message
from ZelzalMusic import app
from ZelzalMusic.utils.database import get_served_chats
from config import LOGGER_ID


async def lul_message(chat_id: int, message: str):
    await app.send_message(chat_id=chat_id, text=message)


@app.on_message(filters.new_chat_members)
async def on_new_chat_members(client: Client, message: Message):
    if (await client.get_me()).id in [user.id for user in message.new_chat_members]:
        added_by = message.from_user.first_name if message.from_user else "ᴜɴᴋɴᴏᴡɴ ᴜsᴇʀ"
        matlabi_jhanto = message.chat.title
        served_chats = len(await get_served_chats())
        chat_id = message.chat.id
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "ᴩʀɪᴠᴀᴛᴇ ᴄʜᴀᴛ"
        lemda_text = f"""
        <b>•────‌‌‏❃ ǫᴜʀᴀɴ ❃──‌‌‏─‌‌‏─•</b>
<b>إشعـار من البوت  ❃</b>
ٴ<b>•────‌‌‏❃ ǫᴜʀᴀɴ ❃──‌‌‏─‌‌‏─•</b>
<b>- سيـدي المطـور 🧑🏻‍💻</b>
<b>-  تم اضافة البوت لجروب جديد ❃</b>

<b>- الاسم :</b> {message.from_user.mention}
<b>- اليوزر :</b> @{message.from_user.username}
<b>- ايدي المستخدم :</b> <code>{message.from_user.id}</code>

<b>- اسم المجموعة :</b> {message.chat.title}
<b>- يوزر المجموعة :</b> @{message.chat.username}
<b>- ايدي المجموعة :</b> <code>{message.chat.id}</code>"""
        await lul_message(LOGGER_ID, lemda_text)
