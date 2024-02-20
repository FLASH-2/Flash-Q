from ZelzalMusic.utils.database import is_music_playing, music_off
from strings import get_command
import asyncio
from strings.filters import command
from ZelzalMusic import app
from ZelzalMusic.core.call import Zelzaly
from ZelzalMusic.utils.database import set_loop
from ZelzalMusic.utils.decorators import AdminRightsCheck
from ZelzalMusic.utils.database import is_muted, mute_on
from ZelzalMusic.utils.database import is_muted, mute_off
from ZelzalMusic.utils.database import is_music_playing, music_on
from datetime import datetime
from config import BANNED_USERS, MUSIC_BOT_NAME, PING_IMG_URL, lyrical, START_IMG_URL, MONGO_DB_URI, OWNER_ID
from ZelzalMusic.utils import bot_sys_stats
from ZelzalMusic.utils.decorators.language import language
import random
import config
import re
from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP
import string
import lyricsgenius as lg
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup, Message)
from pyrogram import Client, filters
from ZelzalMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from typing import Union
import sys
from os import getenv
from dotenv import load_dotenv

load_dotenv()

BOT_USERNAME = getenv("BOT_USERNAME")

START_IMG_URL = getenv("START_IMG_URL")

MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME")

# Commands
STOP_COMMAND = get_command("STOP_COMMAND")
PAUSE_COMMAND = get_command("PAUSE_COMMAND")
MUTE_COMMAND = get_command("MUTE_COMMAND")
UNMUTE_COMMAND = get_command("UNMUTE_COMMAND")
RESUME_COMMAND = get_command("RESUME_COMMAND")
PING_COMMAND = get_command("PING_COMMAND")
LYRICS_COMMAND = get_command("LYRICS_COMMAND")

api_key = "Vd9FvPMOKWfsKJNG9RbZnItaTNIRFzVyyXFdrGHONVsGqHcHBoj3AI3sIlNuqzuf0ZNG8uLcF9wAd5DXBBnUzA"
y = lg.Genius(
    api_key,
    skip_non_songs=True,
    excluded_terms=["(Remix)", "(Live)"],
    remove_section_headers=True,
)
y.verbose = False


    
@app.on_message(
    command(["قول"])
    & filters.group
    & ~filters.edited
)
@app.on_message(
    command(["قول"])
    & filters.private
    & ~filters.edited
)
@app.on_message(
    command(["قول"])
    & filters.channel
    & ~filters.edited
)
def echo(client, msg):
    text = msg.text.split(None, 1)[1]
    msg.reply(text)

@app.on_message(
    command(["انا مين"])
    & filters.group
    & ~filters.edited
)
@app.on_message(
    command(["انا مين"])
    & filters.private
    & ~filters.edited
)
@app.on_message(
    command(["انا مين"])
    & filters.channel
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    usr = await client.get_users(message.from_user.id)
    name = usr.first_name
    async for photo in client.iter_profile_photos(message.from_user.id, limit=1):
                    await message.reply_text( 
                    f"""انت {message.from_user.mention} روح قلبي .""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "‹ ᥴ𝗁ᥲᥒᥒᥱᥣ ᥉᥆υᖇᥴᥱ . ⚡️ ›", url=f"https://t.me/FLS_44"),
                ],
            ]
        ),
    )

@app.on_message(
     command(["شغل","تشغيل","سوره","سورة","اغنيه","اغنية","/skip","/settings","/play","/vplay","/stop"])
    & filters.private
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/738661f85fe3e4fd54d20.jpg",
        caption=f""" • عذرا  !. لا يمكنك التشغيل في الخاص\n\n• قم بأنشاء جروب ثم ضفني لكي اعمل\n\n• معلومات التشغيل انضم @FLS_44\n\n• البوت القرآن  @Boksha4bot\n\n• تقدر تشغل كل ما تحتاجه """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton("‹ اضف البوت لمجموعتك ›", url=f"https://t.me/Boksha4bot?startgroup=true"),
                ],[
                InlineKeyboardButton(
                        "‹ ᥴ𝗁ᥲᥒᥒᥱᥣ ᥉᥆υᖇᥴᥱ . ⚡️ ›", url=f"https://t.me/FLS_44"), 
                ]
            ]
        ),
    )

@app.on_message(
     command(["اسمي"])
    & filters.private
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/738661f85fe3e4fd54d20.jpg",
        caption=f""" ❃ | اسـمـڪ  : [ `{name}` ]\n✓ """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton("‹ اضف البوت لمجموعتك ›", url=f"https://t.me/Boksha4bot?startgroup=true"),
                ],[
                InlineKeyboardButton(
                        "‹ ᥴ𝗁ᥲᥒᥒᥱᥣ ᥉᥆υᖇᥴᥱ . ⚡️ ›", url=f"https://t.me/FLS_44"), 
                ]
            ]
        ),
    )

@app.on_message(
     command(["يوزري","معرفي"])
    & filters.private
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/738661f85fe3e4fd54d20.jpg",
        caption=f""" ❃ | يـوزرڪ : [ @{user} ] \n✓ """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton("‹ اضف البوت لمجموعتك ›", url=f"https://t.me/Boksha4bot?startgroup=true"),
                ],[
                InlineKeyboardButton(
                        "‹ ᥴ𝗁ᥲᥒᥒᥱᥣ ᥉᥆υᖇᥴᥱ . ⚡️ ›", url=f"https://t.me/FLS_44"), 
                ]
            ]
        ),
    )

@app.on_message(
     command(["بايو","البايو"])
    & filters.private
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/738661f85fe3e4fd54d20.jpg",
        caption=f""" ❃ | البـايـو : [ `{kbio}` ] \n✓""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton("‹ اضف البوت لمجموعتك ›", url=f"https://t.me/Boksha4bot?startgroup=true"),
                ],[
                InlineKeyboardButton(
                        "‹ ᥴ𝗁ᥲᥒᥒᥱᥣ ᥉᥆υᖇᥴᥱ . ⚡️ ›", url=f"https://t.me/FLS_44"), 
                ]
            ]
        ),
    )
                    
@app.on_message(
     command(["مبرمج السورس","البوب"])
    & filters.group
    & ~filters.edited
)
@app.on_message(
     command(["مبرمج السورس","البوب"])
    & filters.channel
    & ~filters.edited
)
@app.on_message(
     command(["مبرمج السورس","البوب"])
    & filters.private
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/738661f85fe3e4fd54d20.jpg",
        caption=f"""❃ 𝙽𝙰𝙼𝙴 : ❪ [𓏺 ժᥱ᥎ ᙓᥣ ᑭ᥆ᑭ . ⚡️ ˼](https://t.me/P_O_C)  ❫
❃ 𝚄𝚂𝙴𝚁 : ❪ @P_O_C ❫
❃ 𝙸𝙳   : ❪ 5627420357 ❫
❃ 𝙱𝙸𝙾  : ❪ انا كبير في عين نفسي. انما عينك انتا تع احطلك فيها قطره. @FLS_44 ❫ """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton("‹ ժᥱ᥎ ᙓᥣ ᑭ᥆ᑭ ›", url=f"https://t.me/P_O_C"),
                ],[
                InlineKeyboardButton(
                        "‹ ᥴ𝗁ᥲᥒᥒᥱᥣ ᥉᥆υᖇᥴᥱ . ⚡️ › ", url=f"https://t.me/FLS_44"), 
                ]
            ]
        ),
    )

@app.on_message(
     command(["مبرمج البوت","المبرمج"])
    & filters.group
    & ~filters.edited
)
@app.on_message(
     command(["مبرمج البوت","المبرمج"])
    & filters.private
    & ~filters.edited
)
@app.on_message(
     command(["مبرمج البوت","المبرمج"])
    & filters.channel
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/738661f85fe3e4fd54d20.jpg",
        caption=f"""❃ 𝙽𝙰𝙼𝙴 : ❪ [𓏺 ժᥱ᥎ ᙓᥣ ᑭ᥆ᑭ . ⚡️ ˼](https://t.me/P_O_C)  ❫
❃ 𝚄𝚂𝙴𝚁 : ❪ @P_O_C ❫
❃ 𝙸𝙳   : ❪ 5627420357 ❫
❃ 𝙱𝙸𝙾  : ❪ انا كبير في عين نفسي. انما عينك انتا تع احطلك فيها قطره. @FLS_44 ❫ """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton("‹ ժᥱ᥎ ᙓᥣ ᑭ᥆ᑭ ›", url=f"https://t.me/P_O_C"),
                ],[
                InlineKeyboardButton(
                        "‹ ᥴ𝗁ᥲᥒᥒᥱᥣ ᥉᥆υᖇᥴᥱ . ⚡️ ›", url=f"https://t.me/FLS_44"), 
                ]
            ]
        ),
    )

@app.on_message(
     command(["صاحب السورس","صاحب العظمه","بوب","البوب"])
    & filters.group
    & ~filters.edited
)
@app.on_message(
     command(["صاحب السورس","صاحب العظمه","بوب","البوب"])
    & filters.channel
    & ~filters.edited
)
@app.on_message(
     command(["صاحب السورس","صاحب العظمه","بوب","البوب"])
    & filters.private
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/738661f85fe3e4fd54d20.jpg",
        caption=f"""❃ 𝙽𝙰𝙼𝙴 : ❪ [𓏺 ժᥱ᥎ ᙓᥣ ᑭ᥆ᑭ . ⚡️ ˼](https://t.me/P_O_C)  ❫
❃ 𝚄𝚂𝙴𝚁 : ❪ @P_O_C ❫
❃ 𝙸𝙳   : ❪ 5627420357 ❫
❃ 𝙱𝙸𝙾  : ❪ انا كبير في عين نفسي. انما عينك انتا تع احطلك فيها قطره. @FLS_44 ❫ """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton("‹ ժᥱ᥎ ᙓᥣ ᑭ᥆ᑭ ›", url=f"https://t.me/P_O_C"),
                ],[
                InlineKeyboardButton(
                        "‹ ᥴ𝗁ᥲᥒᥒᥱᥣ ᥉᥆υᖇᥴᥱ . ⚡️ ›", url=f"https://t.me/FLS_44"), 
                ]
            ]
        ),
    )

@app.on_message(
     command(["المطور البوب","المبرمج البوب"])
    & filters.group
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/738661f85fe3e4fd54d20.jpg",
        caption=f"""❃ 𝙽𝙰𝙼𝙴 : ❪ [𓏺 ժᥱ᥎ ᙓᥣ ᑭ᥆ᑭ . ⚡️ ˼](https://t.me/P_O_C)  ❫
❃ 𝚄𝚂𝙴𝚁 : ❪ @P_O_C ❫
❃ 𝙸𝙳   : ❪ 5627420357 ❫
❃ 𝙱𝙸𝙾  : ❪ انا كبير في عين نفسي. انما عينك انتا تع احطلك فيها قطره. @FLS_44 ❫""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton("‹ ժᥱ᥎ ᙓᥣ ᑭ᥆ᑭ ›", url=f"https://t.me/P_O_C"),
                ],[
                InlineKeyboardButton(
                        "‹ ᥴ𝗁ᥲᥒᥒᥱᥣ ᥉᥆υᖇᥴᥱ . ⚡️ ›", url=f"https://t.me/FLS_44"), 
                ]
            ]
        ),
    )

@app.on_message(
    command(["سورس","السورس","يا سورس"])
    & filters.group
    & ~filters.edited
)
@app.on_message(
    command(["سورس","السورس","يا سورس"])
    & filters.channel
    & ~filters.edited
)
@app.on_message(
    command(["سورس","السورس","يا سورس","قناة","قناه"])
    & filters.private
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/738661f85fe3e4fd54d20.jpg",
        caption=f"""╭──── • ◈ • ────╮
么 [َ ᥴ𝗁ᥲᥒᥒᥱᥣ ᥉᥆υᖇᥴᥱ](t.me/FLS_44)
么 [َժᥱ᥎ ᙓᥣ ᑭ᥆ᑭ](t.me/P_O_C)
么 [َ ᘜᖇ᥆υρ ᥉᥆υᖇᥴᥱ ](t.me/FLS_45)
╰──── • ◈ • ────╯
⍟ 𝚃𝙷𝙴 𝙱𝙴𝚂𝚃 𝚂𝙾𝚄𝚁𝙲𝙴 𝙾𝙽 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                    InlineKeyboardButton(
                        "« ժᥱ᥎ ᙓᥣ ᑭ᥆ᑭ »", url=f"https://t.me/P_O_C"),
                ],[
                    InlineKeyboardButton(
                        "‹ ᥴ𝗁ᥲ️ꪀꪀᥱᥣ›", url=f"https://t.me/FLS_44"), 
                    InlineKeyboardButton(
                        "‹ ᘜᖇ᥆υρ ᥉᥆υᖇᥴᥱ›", url=f"https://t.me/FLS_45"),
                ],[
                    InlineKeyboardButton(
                        "‹ اضف البوت لمجموعتك ›", url=f"https://t.me/Boksha4bot?startgroup=true"),
            ]
        ]
         ),
     )
  
