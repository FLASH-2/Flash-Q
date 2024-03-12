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
    command(["البوب","المطور","بوب",])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/738661f85fe3e4fd54d20.jpg",
        caption=f"""◉ 𝙽𝙰𝙼𝙴 : ❪ 𝙴𝙻𝙿𝙾𝙿 ❫
◉ 𝚄𝚂𝙴𝚁 : ❪ @P_O_C ❫
◉ 𝙸𝙳       : ❪ 5627420357 ❫
◉ 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 : ❪ @FLS_44 ❫
◉ 𝙶𝚁𝙾𝚄𝙿    : ❪ @FLS_45 ❫""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                    InlineKeyboardButton(
                        "𝙳𝙴𝚅 𝙴𝙻𝙿𝙾𝙿", url=f"https://t.me/P_O_C"),
            ]
        ]
         ),
     )
  
