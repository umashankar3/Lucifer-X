#    Lucifer - UserBot
#    Copyright (C) 2020 Lucifer

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

from telethon.tl.types import Channel

from Lucifer import *
from Lucifer import ALIVE_NAME, bot, lucifer
from Lucifer.LuciferConfig import Config, Var

# stats
if Var.PRIVATE_GROUP_ID:
    log = "Enabled"
else:
    log = "Disabled"

if Config.TG_BOT_USER_NAME_BF_HER:
    bots = "Enabled"
else:
    bots = "Disabled"

if Var.LYDIA_API_KEY:
    lyd = "Enabled"
else:
    lyd = "Disabled"

if Config.SUDO_USERS:
    sudo = "Disabled"
else:
    sudo = "Enabled"

if Var.PMSECURITY.lower() == "off":
    pm = "Disabled"
else:
    pm = "Enabled"

LUCIFERUSER = str(ALIVE_NAME) if ALIVE_NAME else "@LuciferXsupport"

Lucifer = f"L U C I F E R 𝚅𝙴𝚁𝚂𝙸𝙾𝙽: {Lucifer}\n"
Lucifer += f"𝙻𝙾𝙶 𝙶𝚁𝙾𝚄𝙿: {log}\n"
Lucifer += f"𝙼𝚈 𝙰𝚂𝚂𝙸𝚂𝚃𝙰𝙽𝚃 𝙱𝙾𝚃: {bots}\n"
Lucifer += f"𝙻𝚈𝙳𝙸𝙰: {lyd}\n"
Lucifer += f"𝚂𝚄𝙳𝙾 𝚄𝚂𝙴𝚁: {sudo}\n"
Lucifer += f"𝙿𝙼 𝚂𝙴𝙲𝚄𝚁𝙸𝚃𝚈: {pm}\n"
Lucifer += f"\n𝚅𝙸𝚂𝙸𝚃 @LuciferXsupport 𝙵𝙾𝚁 𝙰𝚂𝚂𝙸𝚂𝚃𝙰𝙽𝚃.\n"
Luciferstats = f"{Lucifer}"

LUCIFER_NAME = bot.me.first_name
OWNER_ID = bot.me.id

# count total number of groups


async def lucifer_grps(event):
    a = []
    async for dialog in event.client.iter_dialogs():
        entity = dialog.entity
        if isinstance(entity, Channel):
            if entity.megagroup:
                if entity.creator or entity.admin_rights:
                    a.append(entity.id)
    return len(a), a
