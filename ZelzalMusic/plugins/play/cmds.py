

import asyncio
import os
import requests
import pyrogram
from pyrogram import Client, filters, emoji
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.errors import MessageNotModified
from ZelzalMusic import app
from config import OWNER_ID, LOGGER_ID


@app.on_message(command(["اوامر", "الاوامر"]))
async def zdatsr(client: Client, message: Message):
    usr = await client.get_users(OWNER_ID)
    name = usr.first_name
    usrnam = usr.username
    await message.reply_photo(
        photo=f"https://telegra.ph/file/738661f85fe3e4fd54d20.jpg",
        caption=f"""<b>» مرحبـاً بك عـزيـزي </b> {message.from_user.mention} .\n\n<b>» استخـدم الازرار بالاسفـل ❃\n» لـ تصفـح اوامـر بوت القرآن ❃</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• اوامــر التشغيــل •", callback_data="zzzll"),
                ],[
                    InlineKeyboardButton(
                        "• اوامـر القنـاة •", callback_data="zzzch"),
                    InlineKeyboardButton(
                        "• اوامـر الادمـن •", callback_data="zzzad"),
                ],[
                    InlineKeyboardButton(
                        "• اوامــر المطــور •", callback_data="zzzdv"),
                ],[
                    InlineKeyboardButton(name, url=f"https://t.me/{usrnam}"),
                ],[
                    InlineKeyboardButton(
                        "• S᥆υᖇᥴᥱ ᖴᥣᥲ᥉Ꮒ •", url="https://t.me/FLS_44"),
                ],
            ]
        ),
    )


@app.on_message(command(["مطور", "المطور"]) & filters.group)
async def zilzal(client: Client, message: Message):
    usr = await client.get_users(OWNER_ID)
    name = usr.first_name
    usrnam = usr.username
    async for photo in client.iter_profile_photos(OWNER_ID, limit=1):
                    await message.reply_photo(photo.file_id,       caption=f"""ٴ<b>•────‌‌‏✯ ᴇ_ᴍᴜsɪᴄ ✯──‌‌‏─‌‌‏─•</b>
                    
- المطور :[{usr.first_name}](https://t.me/{OWNER})
- اليوزر :@{usrnam} 
- الايدي :`{usr.id}`
 
ٴ<b>•────‌‌‏✯ ᴇ_ᴍᴜsɪᴄ ✯──‌‌‏─‌‌‏─•</b> """, 
reply_markup=InlineKeyboardMarkup(
          [               
            [            
              InlineKeyboardButton (name, url=f"https://t.me/{usrnam}"),
            ],[
              InlineKeyboardButton("•LorD Music•", url="https://t.me/M_r_zC"),
            ],
          ]
       )                 
    )                    
                    sender_id = message.from_user.id
                    sender_name = message.from_user.first_name
                    senderuser = message.from_user.username
                    sender_user = "@{senderuser}" if senderuser else "لا يوجـد"
                    await app.send_message(OWNER_ID, f"- المستخـدم {message.from_user.mention} يناديـك \n\n- الاسـم : {sender_name} \n- الايـدي : {sender_id}\n- اليـوزر : {sender_user}")
                    return await app.send_message(LOGGER_ID, f"- المستخـدم {message.from_user.mention} يناديـك \n\n- الاسـم : {sender_name} \n- الايـدي : {sender_id}\n- اليـوزر : {sender_user}")
