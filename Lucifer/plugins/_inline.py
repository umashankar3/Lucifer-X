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

from . import *

fuk_uid = bot.uid
HELP_PIC = "https://telegra.ph/file/6676e5fd9f46eccd2061f.jpg"
PMPERMIT_PIC = os.environ.get("PMPERMIT_PIC", None)
TELEPIC = (
    PMPERMIT_PIC
    if PMPERMIT_PIC
    else "https://telegra.ph/file/6676e5fd9f46eccd2061f.jpg"
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
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "UMASHANKAR User"
USER_BOT_WARN_ZERO = "`𝙸 𝙷𝙰𝚅𝙴 𝚆𝙰𝚁𝙽𝙴𝙳 𝚈𝙾𝚄 𝙽𝙾𝚃 𝚃𝙾 𝚂𝙿𝙰𝙼 😑😑. 𝙽𝙾𝚆 𝚈𝙾𝚄 𝙷𝙰𝚅𝙴 𝙱𝙴𝙴𝙽 𝙱𝙻𝙾𝙲𝙺𝙴𝙳 𝙰𝙽𝙳 𝚁𝙴𝙿𝙾𝚁𝚃𝙴𝙳 𝚄𝙽𝚃𝙸𝙻 𝙵𝚄𝚃𝚄𝚁𝙴 𝙽𝙾𝚃𝙸𝙲𝙴.`\n\n**GoodBye!** "

if Var.LOAD_MYBOT == "True":
    USER_BOT_NO_WARN = (
        "**𝙷𝙴𝚈 𝚃𝙷𝙸𝚂 𝙸𝚂 UMASHANKAR 𝙿𝙼 𝚂𝙴𝙲𝚄𝚁𝙸𝚃𝚈 !!! 𝙷𝙴𝚁𝙴 𝚃𝙾 𝙿𝚁𝙾𝚃𝙴𝙲𝚃 [{}](tg://user?id={})**\n\n"
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

CUSTOM_HELP_EMOJI = os.environ.get("CUSTOM_HELP_EMOJI", "⚜")
HELP_ROWS = int(os.environ.get("HELP_ROWS", 3))
HELP_COLOUMNS = int(os.environ.get("HELP_COLOUMNS", 4))

if Var.TG_BOT_USER_NAME_BF_HER is not None and tgbot is not None:

    @tgbot.on(events.InlineQuery)  # pylint:disable=E0602
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        if event.query.user_id == bot.uid and query.startswith("`ℓυcιғεя"):
            rev_text = query[::-1]
            but = [[custom.Button.inline("💬 Oᴘᴇɴ ʜᴇʟᴘ ᴍᴇɴᴜ »»", data="menu")]]
            but += [[custom.Button.inline("💡 Pɪɴɢ »»", data="ping")]]
            but += [[Button.url("Mʏ ᴍᴀsᴛᴇʀ »»", "tg://user?id={fuk_uid})")]]
            but += [[custom.Button.inline("Mᴀsᴛᴇʀ•ᴛᴏᴏʟs", data="mtools")]]
            but += [[custom.Button.inline("Iɴʟɪɴᴇ", data="linline")]]
            but += [
                [
                    Button.url("🔰 Sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ »»", "t.me/shayari_jok"),
                    Button.url("🔰 Uᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ", "t.me/UMASHANKAR31"),
                ]
            ]
            result = builder.photo(
                file=HELP_PIC,
                text="{}\n𝙲𝚄𝚁𝚁𝙴𝙽𝚃𝙻𝚈 𝙻𝙾𝙰𝙳𝙴𝙳 𝙿𝙻𝚄𝙶𝙸𝙽𝚂: {}".format(query, len(CMD_LIST)),
                buttons=but,
                link_preview=False,
            )
        elif event.query.user_id == bot.uid and query.startswith("stats"):
            result = builder.article(
                title="Stats",
                text=f"**𝙻𝙴𝚃𝙷𝙰𝙻 𝚄𝙱 𝚂𝚃𝙰𝚃𝚂 𝙾𝙵 𝚃𝙷𝙴 [{DEFAULTUSER}](tg://user?id={myid})**\n\n__𝙱𝙾𝚃 𝙸𝚂 𝚂𝙼𝙾𝙾𝚃𝙷𝙻𝚈 𝚁𝚄𝙽𝙽𝙸𝙽𝙶, 𝙼𝙰𝚂𝚃𝙴𝚁!__\n\n(c) @Lucifer_support_group",
                buttons=[
                    [custom.Button.inline("Stats", data="statcheck")],
                    [Button.url("INSTAGRAM 💝", "https://instagram.com/umashankar31981")],
                    [
                        Button.url(
                            "FACEBOOK!",
                            "https://www.facebook.com/Umashankar31981",
                        )
                    ],
                ],
            )
        elif event.query.user_id == bot.uid and query.startswith("**PM"):
            TELEBT = USER_BOT_NO_WARN.format(DEFAULTUSER, myid, MESAG)
            result = builder.photo(
                file=TELEPIC,
                text=TELEBT,
                buttons=[
                    [
                        custom.Button.inline("Request ", data="req"),
                        custom.Button.inline("Chat 💭", data="chat"),
                    ],
                    [custom.Button.inline("To spam 🚫", data="heheboi")],
                    [custom.Button.inline("What is this ❓", data="pmclick")],
                ],
            )
        elif event.query.user_id == bot.uid and query == "repo":
            result = builder.article(
                title="Repository",
                text=f"Lucifer - Telegram Userbot.",
                buttons=[
                    [
                        Button.url(
                            "💝 FACEBOOK",
                            "https://www.facebook.com/Umashankar31981",
                        ),
                        Button.url(
                            "INSTAGRAM",
                            "https://instagram.com/umashankar31981",
                        ),
                    ],
                    [Button.url("𝚂𝚄𝙿𝙿𝙾𝚁𝚃 𝙲𝙷𝙰𝚃", "https://t.me/umashankar31")],
                ],
            )
        else:
            result = builder.article(
                "𝚂𝙾𝚄𝚁𝙲𝙴 𝙲𝙾𝙳𝙴",
                text="**Welcome to Lethal**\n\n`Click below buttons for more`",
                buttons=[
                    [
                        custom.Button.url(
                            "🚑 Support Group 🚑", "https://t.me/shayari_jok"
                        )
                    ],
                    [
                        custom.Button.url(
                            "👨‍💻Source Code‍💻", "https://instagram.com/umashankar31981"
                        ),
                        custom.Button.url(
                            "Deployer🌀",
                            "@Umashankar31",
                        ),
                    ],
                    [
                        custom.Button.url(
                            "Updates ↗️", "https://t.me/shayari_jok"
                        )
                    ],
                ],
                link_preview=False,
            )
        await event.answer([result] if result else None)

    @tgbot.on(
        events.callbackquery.CallbackQuery(  # pylint:disable=E0602
            data=re.compile(rb"helpme_next\((.+?)\)")
        )
    )
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:  # pylint:disable=E0602
            current_page_number = int(event.data_match.group(1).decode("UTF-8"))
            buttons = paginate_help(current_page_number + 1, CMD_LIST, "helpme")
            # https://t.me/shayari_jok/52766
            await event.edit(buttons=buttons)
        else:
            reply_pop_up_alert = "Please get your own Userbot from @shayari_jok , and don't use mine!"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"pmclick")))
    async def on_pm_click(event):
        if event.query.user_id == bot.uid:
            reply_pop_up_alert = "This ain't for you, master!"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        else:
            await event.edit(
                f"This is the PM Security for {DEFAULTUSER} to keep away spammers and retards.\n\nProtected by [UMASHANKAR](t.me/shayari_jok)"
            )

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"menu")))
    async def megic(event):
        if event.query.user_id == bot.uid:
            buttons = paginate_help(0, CMD_LIST, "helpme")
            await event.edit(buttons=buttons)
        else:
            reply_pop_up_alert = "This bot ain't for u!!"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"ping")))
async def _(event):
    start = datetime.now()
    end = datetime.now()
    ms = (end - start).microseconds
    reply_pop_up_alert = f"ʙᴏᴛ•Pɪɴɢ = {ms} microseconds"
    await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"req")))
    async def on_pm_click(event):
        if event.query.user_id == bot.uid:
            reply_pop_up_alert = "This ain't for you, master!"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        else:
            await event.edit(
                f"Okay, `{DEFAULTUSER}` would get back to you soon!\nTill then please **wait patienly and don't spam here.**"
            )
            target = await event.client(GetFullUserRequest(event.query.user_id))
            first_name = html.escape(target.user.first_name)
            ok = event.query.user_id
            if first_name is not None:
                first_name = first_name.replace("\u2060", "")
            tosend = f"Hey {DEFAULTUSER}, [{first_name}](tg://user?id={ok}) is **requesting** something in PM!"
            await tgbot.send_message(LOG_GP, tosend)

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"chat")))
    async def on_pm_click(event):
        event.query.user_id
        if event.query.user_id == bot.uid:
            reply_pop_up_alert = "This ain't for you, master!"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        else:
            await event.edit(
                f"Oho, you want to chat...\nPlease wait and see if {DEFAULTUSER} is in a mood to chat, if yes, he will be replying soon!\nTill then, **do not spam.**"
            )
            target = await event.client(GetFullUserRequest(event.query.user_id))
            ok = event.query.user_id
            first_name = html.escape(target.user.first_name)
            if first_name is not None:
                first_name = first_name.replace("\u2060", "")
            tosend = f"Hey {DEFAULTUSER}, [{first_name}](tg://user?id={ok}) wants to PM you for **Random Chatting**!"
            await tgbot.send_message(LOG_GP, tosend)

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"plshelpme")))
    async def on_pm_click(event):
        if event.query.user_id == bot.uid:
            reply_pop_up_alert = "This ain't for you, master!"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        else:
            await event.edit(
                f"Oh!\n{DEFAULTUSER} would be glad to help you out...\nPlease leave your message here **in a single line** and wait till I respond 😊"
            )
            target = await event.client(GetFullUserRequest(event.query.user_id))
            first_name = html.escape(target.user.first_name)
            ok = event.query.user_id
            if first_name is not None:
                first_name = first_name.replace("\u2060", "")
            tosend = f"Hey {DEFAULTUSER}, [{first_name}](tg://user?id={ok}) wants to PM you for **help**!"
            await tgbot.send_message(LOG_GP, tosend)

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"heheboi")))
    async def on_pm_click(event):
        if event.query.user_id == bot.uid:
            reply_pop_up_alert = "This ain't for you, master!"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        else:
            await event.edit(
                f"Oh, so you are here to spam 😤\nGoodbye.\nYour message has been read and successfully ignored."
            )
            await borg(functions.contacts.BlockRequest(event.query.user_id))
            target = await event.client(GetFullUserRequest(event.query.user_id))
            ok = event.query.user_id
            first_name = html.escape(target.user.first_name)
            if first_name is not None:
                first_name = first_name.replace("\u2060", "")
            first_name = html.escape(target.user.first_name)
            await tgbot.send_message(
                LOG_GP,
                f"[{first_name}](tg://user?id={ok}) tried to **spam** your inbox.\nHenceforth, **blocked**",
            )

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"close")))
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:
            await event.edit(
                "Menu Closed!!", buttons=[Button.inline("Re-open Menu", data="reopen")]
            )
        else:
            reply_pop_up_alert = (
                "Please get your own userbot from @Lucifer_support_group "
            )
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"statcheck")))
    async def rip(event):
        text = lethalstats
        await event.answer(text, alert=True)

    @tgbot.on(
        events.callbackquery.CallbackQuery(  # pylint:disable=E0602
            data=re.compile(rb"helpme_prev\((.+?)\)")
        )
    )
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:  # pylint:disable=E0602
            current_page_number = int(event.data_match.group(1).decode("UTF-8"))
            buttons = paginate_help(
                current_page_number - 1, CMD_LIST, "helpme"  # pylint:disable=E0602
            )
            # https://t.me/TelethonChat/115200
            await event.edit(buttons=buttons)
        else:
            reply_pop_up_alert = "Please get your own Userbot, and don't use mine!"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"reopen")))
    async def megic(event):
        if event.query.user_id == bot.uid:
            buttons = paginate_help(0, CMD_LIST, "helpme")
            await event.edit("Menu-Reopened", buttons=buttons)
        else:
            reply_pop_up_alert = "This bot ain't for u!!"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

    @tgbot.on(
        events.callbackquery.CallbackQuery(  # pylint:disable=E0602
            data=re.compile(b"us_plugin_(.*)")
        )
    )
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:
            plugin_name = event.data_match.group(1).decode("UTF-8")
            help_string = ""
            help_string += f"Commands Available in {plugin_name} - \n"
            try:
                if plugin_name in CMD_HELP:
                    for i in CMD_HELP[plugin_name]:
                        help_string += i
                    help_string += "\n"
                else:
                    for i in CMD_LIST[plugin_name]:
                        help_string += i
                        help_string += "\n"
            except BaseException:
                pass
            if help_string == "":
                reply_pop_up_alert = "{} has no detailed info.\nUse .help {}".format(
                    plugin_name, plugin_name
                )
            else:
                reply_pop_up_alert = help_string
            reply_pop_up_alert += "\n Use .unload {} to remove this plugin\n\
                © Lethal".format(
                plugin_name
            )
            if len(help_string) >= 140:
                oops = "List too long!\nCheck your saved messages!"
                await event.answer(oops, cache_time=0, alert=True)
                help_string += "\n\nThis will be auto-deleted in 1 minute!"
                if bot is not None and event.query.user_id == bot.uid:
                    ok = await bot.send_message("me", help_string)
                    await asyncio.sleep(60)
                    await ok.delete()
            else:
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        else:
            reply_pop_up_alert = "Please get your own Userbot, and don't use mine!"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)


def paginate_help(page_number, loaded_plugins, prefix):
    number_of_rows = HELP_ROWS
    number_of_cols = HELP_COLOUMNS
    lethal = CUSTOM_HELP_EMOJI
    helpable_plugins = []
    for p in loaded_plugins:
        if not p.startswith("_"):
            helpable_plugins.append(p)
    helpable_plugins = sorted(helpable_plugins)
    modules = [
        custom.Button.inline(
            "{} {} {}".format(lethal, x, lethal), data="us_plugin_{}".format(x)
        )
        for x in helpable_plugins
    ]
    pairs = list(zip(modules[::number_of_cols], modules[1::number_of_cols]))
    if len(modules) % number_of_cols == 1:
        pairs.append((modules[-1],))
    max_num_pages = ceil(len(pairs) / number_of_rows)
    modulo_page = page_number % max_num_pages
    if len(pairs) > number_of_rows:
        pairs = pairs[
            modulo_page * number_of_rows : number_of_rows * (modulo_page + 1)
        ] + [
            (
                custom.Button.inline(
                    "🗡️ քʀɛʋɨօʊֆ", data="{}_prev({})".format(prefix, modulo_page)
                ),
                custom.Button.inline("⚙️ Close ⚙️", data="close"),
                custom.Button.inline(
                    "ռɛӼȶ 🗡️", data="{}_next({})".format(prefix, modulo_page)
                ),
            )
        ]
    return pairs


async def userinfo(event):
    target = await event.client(GetFullUserRequest(event.query.user_id))
    first_name = html.escape(target.user.first_name)
    if first_name is not None:
        first_name = first_name.replace("\u2060", "")
    return first_name
