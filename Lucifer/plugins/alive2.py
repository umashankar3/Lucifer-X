import time

from telethon import version
from userbot.utils import admin_cmd, sudo_cmd

from Lucifer import ALIVE_NAME, StartTime, luciferver
from Lucifer.helper import functions as dcdef
from Lucifer.LuciferConfig import Config, Var

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "ℓυcιғεя x υsεя"

# Thanks to Sipak bro and Aryan..
# animation Idea by @ItzSipak && @Hell boy_pikachu
# Made by @hellboi_atul ....and thanks to @Crackexy for the logos...
# Kang with credits else gay...
# alive.py for DC(DARK COBRA)
# modded for Lucifer X Userbot
global fuk
fuk = borg.uid
edit_time = 5
""" =======================CONSTANTS====================== """
file1 = "https://t.me/shayari_jok/52766"
""" =======================CONSTANTS====================== """
# ======CONSTANTS=========#
CUSTOM_ALIVE = Var.CUSTOM_ALIVE if Var.CUSTOM_ALIVE else "ℓυcιғεя Ӽ ʊֆɛʀɮօȶ ɨֆ օռʟɨռɛ!"
ALV_PIC = (
    Var.ALIVE_PIC
    if Var.ALIVE_PIC
    else "https://t.me/shayari_jok/52766"
)
luciferemoji = Var.CUSTOM_ALIVE_EMOJI if Var.CUSTOM_ALIVE_EMOJI else "**〢**"
if Config.SUDO_USERS:
    sudo = "Enabled"
else:
    sudo = "Disabled"
# ======CONSTANTS=========#


@Lucifer.on(admin_cmd(pattern=r"alive"))
@Lucifer.on(sudo_cmd(pattern=r"alive", allow_sudo=True))
async def hmm(yes):
    await yes.get_chat()
    global fuk
    fuk = borg.uid
    await yes.delete()
    uptime = await dcdef.get_readable_time((time.time() - StartTime))
    pm_caption = f"{luciferemoji}**{CUSTOM_ALIVE}**\n\n"
    pm_caption += f"{luciferemoji}**Mʏ sʏsᴛᴇᴍ ɪs ᴘᴇʀғᴇᴄᴛʟʏ ʀᴜɴɴɪɢ**\n\n"
    pm_caption += f"{luciferemoji} Aʙᴏᴜᴛ ᴍʏ sʏsᴛᴇᴍ ✗\n\n"
    pm_caption += f"{luciferemoji} **LUCIFER 𝙓 𝙑𝙀𝙍𝙎𝙄𝙊𝙉**: `{luciferver}`\n"
    pm_caption += f"{luciferemoji} **𝙏𝙀𝙇𝙀𝙏𝙃𝙊𝙉 𝙑𝙀𝙍𝙎𝙄𝙊𝙉** ☞ {version.__version__}\n"
    pm_caption += (
        f"{luciferemoji} **𝙎𝙐𝙋𝙋𝙊𝙍𝙏 𝘾𝙃𝘼𝙉𝙉𝙀𝙇** ☞ [UMASHANKAR YADAV](https://t.me/UMASHANKAR31)\n"
    )
    pm_caption += f"{luciferemoji} **𝙇𝙄𝘾𝙀𝙉𝙎𝙀**  ☞ [FACEBOOK](https://www.facebook.com/Umashankar31981)\n"
    pm_caption += f"{luciferemoji} **𝘾𝙊𝙋𝙔𝙍𝙄𝙂𝙃𝙏 𝘽𝙔** ☞ [INSTAGRAM](https://instagram.com/umashankar31981)\n\n"
    pm_caption += f"{luciferemoji} **LUCIFER 𝙐𝙋𝙏𝙄𝙈𝙀** ☞ {uptime}\n\n"
    pm_caption += (
        f"{luciferemoji} **𝙈𝙔 𝙋𝙀𝙍𝙊 𝙈𝘼𝙎𝙏𝙀𝙍** ☞ [{DEFAULTUSER}](tg://user?id={fuk})\n"
    )
    on = await borg.send_file(
        yes.chat_id, file=ALV_PIC, caption=pm_caption, link_preview=False
    )


# This Alive is for Lucifer X modded from dc
# use with credits
