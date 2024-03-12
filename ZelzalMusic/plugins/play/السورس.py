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
        caption=f"""❃ 𝚃𝙷𝙴 𝙱𝙴𝚂𝚃 𝚂𝙾𝚄𝚁𝙲𝙴 𝙾𝙽 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                    InlineKeyboardButton(
                        "𝙰𝙳𝙳 𝙼𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 ", url=f"https://t.me/{app.username}?startgroup=true"),
                ],[
                    InlineKeyboardButton(
                        "𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝚂𝙾𝚄𝚁𝙲𝙴", url=f"https://t.me/FLS_44"),
                    InlineKeyboardButton(
                        "𝙶𝚁𝙾𝚄𝙿 𝚂𝙾𝚄𝚁𝙲𝙴", url=f"https://t.me/FLS_45"),
                ],[
                    InlineKeyboardButton(
                        "𝙳𝙴𝚅 𝙴𝙻𝙿𝙾𝙿", user_id=5627420357),
                ],[
                    InlineKeyboardButton(text="𝙲𝙻𝙾𝚂𝙴", callback_data="close"),   
            ]
        ]
         ),
     )