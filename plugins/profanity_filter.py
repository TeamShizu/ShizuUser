# ShizuUser - UserBot
# Copyright (C) 2021 TeamShizuUser
#
# This file is a part of < https://github.com/TeamShizu/ShizuUser/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamShizu/ShizuUser/blob/main/LICENSE/>.

"""
✘ Commands Available -

•`{i}addprofanity`
   If someone sends bad word in a chat, Then bot will delete that message.

•`{i}remprofanity`
   From chat from Profanity list.

"""


from ProfanityDetector import detector
from pyShizuUser.functions.nsfw_db import is_profan, profan_chat, rem_profan

from . import *


@ShizuUser_cmd(pattern="addprofanity$", admins_only=True)
async def addp(e):
    profan_chat(e.chat_id, "mute")
    await eod(e, "`Added This Chat for Profanity Filtering!`", time=10)


@ShizuUser_cmd(pattern="remprofanity", admins_only=True)
async def remp(e):
    rem_profan(e.chat_id)
    await eod(e, "`Removed This Chat from Profanity Filtering!`", time=10)


@ShizuUser_bot.on(events.NewMessage(incoming=True))
async def checkprofan(e):
    chat = e.chat_id
    if is_profan(chat) and e.text:
        x, y = detector(e.text)
        if y:
            await e.delete()
