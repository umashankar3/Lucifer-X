import asyncio
import html
import os
import re
from datetime import datetime
from math import ceil

from telethon import Button, custom, events, functions
from telethon.tl.functions.users import GetFullUserRequest

from Lucifer import ALIVE_NAME, CMD_HELP, CMD_LIST, CUSTOM_PMPERMIT, bot
from Lucifer.LuciferConfig import Var

fuk_uid = bot.uid
HELP_PIC = "https://telegra.ph/file/73373552e9217e010e853.jpg"
PMPERMIT_PIC = os.environ.get("PMPERMIT_PIC", None)
TELEPIC = (
    PMPERMIT_PIC
    if PMPERMIT_PIC
    else "https://telegra.ph/file/73373552e9217e010e853.jpg"
)
PM_WARNS = {}
PREV_REPLY_MESSAGE = {}
myid = bot.uid
mybot = Var.TG_BOT_USER_NAME_BF_HER
if mybot.startswith("@"):
    botname = mybot
else:
    botname = f"@{mybot}"
LOG_GP = Var.PRIVATE_GROUP_ID
MESAG = (
    str(CUSTOM_PMPERMIT)
    if CUSTOM_PMPERMIT
    else "`𝚈𝙾𝙾 𝙷𝙴𝚁𝙴 𝙸𝚂 L U C I F E R 𝙿𝙼 𝚂𝙴𝙲𝚄𝚁𝙸𝚃𝚈! 𝙿𝙻𝙴𝙰𝚂𝙴 𝚆𝙰𝙸𝚃 𝚃𝙸𝙻𝙻 𝙼𝚈 𝙼𝙰𝚂𝚃𝙴𝚁 𝙰𝙿𝙿𝚁𝙾𝚅𝙴. 🤓"
)
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Lucifer User"
USER_BOT_WARN_ZERO = "`𝙸 𝙷𝙰𝚅𝙴 𝚆𝙰𝚁𝙽𝙴𝙳 𝚈𝙾𝚄 𝙽𝙾𝚃 𝚃𝙾 𝚂𝙿𝙰𝙼 😑😑. 𝙽𝙾𝚆 𝚈𝙾𝚄 𝙷𝙰𝚅𝙴 𝙱𝙴𝙴𝙽 𝙱𝙻𝙾𝙲𝙺𝙴𝙳 𝙰𝙽𝙳 𝚁𝙴𝙿𝙾𝚁𝚃𝙴𝙳 𝚄𝙽𝚃𝙸𝙻 𝙵𝚄𝚃𝚄𝚁𝙴 𝙽𝙾𝚃𝙸𝙲𝙴.`\n\n**GoodBye!** "

if Var.LOAD_MYBOT == "True":
    USER_BOT_NO_WARN = (
        "**𝙷𝙴𝚈 𝚃𝙷𝙸𝚂 𝙸𝚂 L U C I F E R 𝙿𝙼 𝚂𝙴𝙲𝚄𝚁𝙸𝚃𝚈 !!! 𝙷𝙴𝚁𝙴 𝚃𝙾 𝙿𝚁𝙾𝚃𝙴𝙲𝚃 [{}](tg://user?id={})**\n\n"
        "{}\n\n"
        "𝙵𝙾𝚁 𝚄𝚁𝙶𝙴𝙽𝚃 𝙷𝙴𝙻𝙿, 𝙿𝙼 𝚅𝙸𝙰 {}"
        "\n𝙿𝙻𝙴𝙰𝚂𝙴 𝙲𝙷𝙾𝙾𝚂𝙴 𝚆𝙷𝚈 𝚈𝙾𝚄 𝙰𝚁𝙴 𝙷𝙴𝚁𝙴, 𝙵𝚁𝙾𝙼 𝚃𝙷𝙴 𝙰𝚅𝙰𝙸𝙻𝙰𝙱𝙻𝙴 𝙾𝙿𝚃𝙸𝙾𝙽\n\n".format(
            DEFAULTUSER, myid, MESAG, botname
        )
    )
elif Var.LOAD_MYBOT == "False":
    USER_BOT_NO_WARN = (
        "**𝙿𝙼 𝚂𝙴𝙲𝚄𝚁𝙸𝚃𝚈 𝙾𝙵 [{}](tg://user?id={})**\n\n"
        "{}\n"
        "\n𝙿𝙻𝙴𝙰𝚂𝙴 𝙲𝙷𝙾𝙾𝚂𝙴 𝚆𝙷𝚈 𝚈𝙾𝚄 𝙰𝚁𝙴 𝙷𝙴𝚁𝙴, 𝙵𝚁𝙾𝙼 𝚃𝙷𝙴 𝙰𝚅𝙰𝙸𝙻𝙰𝙱𝙻𝙴 𝙾𝙿𝚃𝙸𝙾𝙽\n".format(
            DEFAULTUSER, myid, MESAG
        )
    )

CUSTOM_HELP_EMOJI = os.environ.get("CUSTOM_HELP_EMOJI", "💞")
HELP_ROWS = int(os.environ.get("HELP_ROWS", 7))
HELP_COLOUMNS = int(os.environ.get("HELP_COLOUMNS", 4))

if Var.TG_BOT_USER_NAME_BF_HER is not None and tgbot is not None:
