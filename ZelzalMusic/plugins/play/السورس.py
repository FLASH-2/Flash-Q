import asyncio

import os
import time
import requests
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZelzalMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZelzalMusic import app
from random import  choice, randint

                
@app.on_message(
    command(["سورس","السورس","سورس البوب"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/738661f85fe3e4fd54d20.jpg",
        caption=f"""« S᥆υᖇᥴᥱ ᖴᥣᥲ᥉Ꮒ »""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                    InlineKeyboardButton(
                        "« ᗩძძ TᏂᥱ ᙖ᥆T T᥆ Y᥆ᥙɾ ᘜɾ᥆ᥙρ »", url=f"https://t.me/{app.username}?startgroup=true"),
                ],[
                    InlineKeyboardButton(
                        "« ᥴ𝗁ᥲᥒᥒᥱᥣ ᥉᥆υᖇᥴᥱ »", url=f"https://t.me/OOOJ30"),
                    InlineKeyboardButton(
                        "« ᘜᖇ᥆υρ ᥉᥆υᖇᥴᥱ »", url=f"https://t.me/M_4_M_C"),
                ],[
                    InlineKeyboardButton(
                        "« ժᥱ᥎ ᙓᥣ ᑭ᥆ᑭ ", user_id=5627420357),
                ],[
                    InlineKeyboardButton(text="« مسح »", callback_data="close"),   
            ]
        ]
         ),
     )