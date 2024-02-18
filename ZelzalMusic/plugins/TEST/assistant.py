
from pyrogram import filters
from pyrogram.types import Message

from ZelzalMusic import ASS_MENTION, LOGGER, SUDOERS, app, app2


@app.on_message(filters.command(["asspfp", "setpfp"]) | filters.command(["صوره","صورة"],prefixes= ["/", "!","","#"]) & SUDOERS)
async def set_pfp(_, message: Message):
    if message.reply_to_message.photo:
        fuk = await message.reply_text("⌔ جاري تغير صور‏‏ه الحساب المساعد")
        img = await message.reply_to_message.download()
        try:
            await app2.set_profile_photo(photo=img)
            return await fuk.edit_text(
                f"⌔ {ASS_MENTION} تم تغيير صورة الحساب المساعد"
            )
        except:
            return await fuk.edit_text("⌔ فشل في تغيير صورة الحساب المساعد")
    else:
        await message.reply_text(
            "⌔ لازم تعمل ريب علي الصورة 🤓"
        )


@app.on_message(filters.command(["مسح", "مسح صورة"]) & SUDOERS)
async def set_pfp(_, message: Message):
    try:
        pfp = [p async for p in app2.get_chat_photos("me")]
        await app2.delete_profile_photos(pfp[0].file_id)
        return await message.reply_text(
            "⌔ تم ازاله صوره الحساب المساعد"
        )
    except Exception as ex:
        LOGGER.error(ex)
        await message.reply_text("⌔ فشل في حذف الصورة")


@app.on_message(filters.command(["بايو", "وضع بايو"]) & SUDOERS)
async def set_bio(_, message: Message):
    msg = message.reply_to_message
    if msg:
        if msg.text:
            newbio = msg.text
            await app2.update_profile(bio=newbio)
            return await message.reply_text(
                f"⌔ {ASS_MENTION} تم تغيير البايو"
            )
    elif len(message.command) != 1:
        newbio = message.text.split(None, 1)[1]
        await app2.update_profile(bio=newbio)
        return await message.reply_text(f"⌔ {ASS_MENTION} تم تغيير البايو")
    else:
        return await message.reply_text(
            "⌔ اعمل ريب علي البايو 🤓"
        )


@app.on_message(filters.command(["اسم", "وضع اسم"]) & SUDOERS)
async def set_name(_, message: Message):
    msg = message.reply_to_message
    if msg:
        if msg.text:
            name = msg.text
            await app2.update_profile(first_name=name)
            return await message.reply_text(
                f"⌔ {ASS_MENTION} تم تغيير الاسم"
            )
    elif len(message.command) != 1:
        name = message.text.split(None, 1)[1]
        await app2.update_profile(first_name=name, last_name="")
        return await message.reply_text(f"⌔ {ASS_MENTION} ‌‌‌تم تغيير الاسم")
    else:
        return await message.reply_text(
            "⌔ اعمل ريب علي الاسم 🤓"
        )
