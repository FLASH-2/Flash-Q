
from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import Message

import config
from ZelzalMusic import BOT_NAME, app


@app.on_message(
    filters.command(["config", "variables"]) | filters.command(["الحاجات","الفارات","الايبهات","كونفنج"],prefixes= ["/", "!","","#"]) & filters.user(config.OWNER_ID)
)
async def get_vars(_, message: Message):
    try:
        await app.send_message(
            chat_id=int(config.OWNER_ID),
            text=f"""<u>**{BOT_NAME} ᴄᴏɴғɪɢ ᴠᴀʀɪᴀʙʟᴇs :**</u>

**قناة السورس :** `{config.SUPPORT_CHANNEL}`
**جروب السورس :** `{config.SUPPORT_CHAT}`

**توكن البوت :** `{config.BOT_TOKEN}`
**حد المدة :** `{config.DURATION_LIMIT}`

**ايدي المالك :** `{config.OWNER_ID}`
**ايدي جروب السجل :** `{config.LOGGER_ID}`

**الجلسة :** `{config.STRING_SESSION}`""",
            disable_web_page_preview=True,
        )
    except:
        return await message.reply_text("⋄ فشل في إرسال متغيرات التكوين .")
    if message.chat.type != ChatType.PRIVATE:
        await message.reply_text(
            "⋄ ᴘʟᴇᴀsᴇ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴘᴍ, ɪ'ᴠᴇ sᴇɴᴛ ᴛʜᴇ ᴄᴏɴғɪɢ ᴠᴀʀɪᴀʙʟᴇs ᴛʜᴇʀᴇ."
        )
