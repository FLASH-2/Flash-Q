
from pyrogram import Client

import config

from ..logging import LOGGER

assistants = []
assistantids = []


class Userbot(Client):
    def __init__(self):
        self.one = Client(
            name="ZelzaLAss1",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING1),
            no_updates=True,
        )
        self.two = Client(
            name="ZelzaLAss2",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING2),
            no_updates=True,
        )
        self.three = Client(
            name="ZelzaLAss3",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING3),
            no_updates=True,
        )
        self.four = Client(
            name="ZelzaLAss4",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING4),
            no_updates=True,
        )
        self.five = Client(
            name="ZelzaLAss5",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING5),
            no_updates=True,
        )

    async def start(self):
        LOGGER("قرآن فلاش").info(f"جارِ تشغيل الحساب المساعد . . .")
        if config.STRING1:
            await self.one.start()
            try:
                await self.one.join_chat("FLS_46")
                await self.one.join_chat("FLS_47")
                await self.one.join_chat("FLS_45")
                await self.one.join_chat("FLS_45")
                await self.one.join_chat("FLS_48")
            except:
                pass
            assistants.append(1)
            try:
                await self.one.send_message(config.LOGGER_ID, "» تم تشغيـل الحسـاب المسـاعـد .. بنجـاح ✅")
            except:
                LOGGER(__name__).error(
                    "فشل حساب المساعد 1 في الوصول إلى مجموعة السجل.  تأكد من إضافة مساعدك إلى مجموعة السجل الخاصة بك وترقيتة كمسؤول!"
                )
                exit()
            self.one.id = self.one.me.id
            self.one.name = self.one.me.first_name
            self.one.username = self.one.me.username
            assistantids.append(self.one.id)
            LOGGER("قرآن فلاش").info(f"تم بدء تشغيل الحساب المساعد {self.one.name} ...✓")

        if config.STRING2:
            await self.two.start()
            try:
                await self.two.join_chat("FLS_47")
                await self.two.join_chat("FLS_45")
                await self.two.join_chat("FLS_45")
                await self.two.join_chat("FLS_48")
            except:
                pass
            assistants.append(2)
            try:
                await self.two.send_message(config.LOGGER_ID, "» تم تشغيـل الحسـاب المسـاعـد² .. بنجـاح ✅")
            except:
                LOGGER(__name__).error(
                    "فشل حساب المساعد 2 في الوصول إلى مجموعة السجل.  تأكد من إضافة مساعدك إلى مجموعة السجل الخاصة بك وترقيتة كمسؤول!"
                )
                exit()
            self.two.id = self.two.me.id
            self.two.name = self.two.me.mention
            self.two.username = self.two.me.username
            assistantids.append(self.two.id)
            LOGGER("قرآن فلاش").info(f"بدأ المساعد الثاني كـ {self.two.name}")

        if config.STRING3:
            await self.three.start()
            try:
                await self.three.join_chat("FLS_47")
                await self.three.join_chat("FLS_45")
                await self.three.join_chat("FLS_45")
                await self.three.join_chat("FLS_48")
            except:
                pass
            assistants.append(3)
            try:
                await self.three.send_message(config.LOGGER_ID, "» تم تشغيـل الحسـاب المسـاعـد³ .. بنجـاح ✅")
            except:
                LOGGER(__name__).error(
                    "فشل حساب المساعد 3 في الوصول إلى مجموعة السجل.  تأكد من إضافة مساعدك إلى مجموعة السجل الخاصة بك وترقيتة كمسؤول! "
                )
                exit()
            self.three.id = self.three.me.id
            self.three.name = self.three.me.mention
            self.three.username = self.three.me.username
            assistantids.append(self.three.id)
            LOGGER("قرآن فلاش").info(f"المساعد الثالث بدأ كـ {self.three.name}")

        if config.STRING4:
            await self.four.start()
            try:
                await self.four.join_chat("FLS_47")
                await self.four.join_chat("FLS_45")
                await self.four.join_chat("FLS_45")
                await self.four.join_chat("FLS_48")
            except:
                pass
            assistants.append(4)
            try:
                await self.four.send_message(config.LOGGER_ID, "» تم تشغيـل الحسـاب المسـاعـد⁴ .. بنجـاح ✅")
            except:
                LOGGER(__name__).error(
                    "فشل حساب المساعد 4 في الوصول إلى مجموعة السجل.  تأكد من إضافة مساعدك إلى مجموعة السجل الخاصة بك وترقيتة كمسؤول! "
                )
                exit()
            self.four.id = self.four.me.id
            self.four.name = self.four.me.mention
            self.four.username = self.four.me.username
            assistantids.append(self.four.id)
            LOGGER("قرآن فلاش").info(f"بدأ المساعد الرابع كـ {self.four.name}")

        if config.STRING5:
            await self.five.start()
            try:
                await self.five.join_chat("FLS_47")
                await self.five.join_chat("FLS_45")
                await self.five.join_chat("FLS_45")
                await self.five.join_chat("FLS_48")
            except:
                pass
            assistants.append(5)
            try:
                await self.five.send_message(config.LOGGER_ID, "» تم تشغيـل الحسـاب المسـاعـد⅝ .. بنجـاح ✅")
            except:
                LOGGER(__name__).error(
                    "فشل حساب المساعد 5 في الوصول إلى مجموعة السجل.  تأكد من إضافة مساعدك إلى مجموعة السجل الخاصة بك وترقيتة كمسؤول! "
                )
                exit()
            self.five.id = self.five.me.id
            self.five.name = self.five.me.mention
            self.five.username = self.five.me.username
            assistantids.append(self.five.id)
            LOGGER("قرآن فلاش").info(f"المساعد الخامس بدأ كـ {self.five.name}")

    async def stop(self):
        LOGGER("قرآن فلاش").info(f"إيقاف المساعدين...")
        try:
            if config.STRING1:
                await self.one.stop()
            if config.STRING2:
                await self.two.stop()
            if config.STRING3:
                await self.three.stop()
            if config.STRING4:
                await self.four.stop()
            if config.STRING5:
                await self.five.stop()
        except:
            pass
