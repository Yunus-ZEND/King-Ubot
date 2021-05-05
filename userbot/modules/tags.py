# Ultroid - UserBot
# Copyright (C) 2020 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.
# Ported for King-Ubot by @PacarFerdilla

import asyncio
from telethon.tl.types import ChannelParticipantAdmin as admin
from telethon.tl.types import ChannelParticipantCreator as owner
from telethon.tl.types import UserStatusOffline as off
from telethon.tl.types import UserStatusOnline as onn
from telethon.tl.types import UserStatusRecently as rec
from telethon.utils import get_display_name
from telethon import custom, events
from userbot import CMD_HELP, bot
from userbot.events import register

@register(outgoing=True, pattern=r"^.tags(?: |$)(on|off|all|bots|rec|admins|owner)?")
async def _(event):
    okk = event.text
    lll = event.pattern_match.group(2)
    users = 0
    o = 0
    nn = 0
    rece = 0
    if lll:
        xx = f"{lll}"
    else:
        xx = ""
    async for bb in event.client.iter_participants(event.chat_id, 99):
        users = users + 1
        x = bb.status
        y = bb.participant
        if isinstance(x, onn):
            o = o + 1
            if "on" in okk:
                xx += f"\n[{get_display_name(bb)}](tg://user?id={bb.id})"
        if isinstance(x, off):
            nn = nn + 1
            if "off" in okk:
                if not (bb.bot or bb.deleted):
                    xx += f"\n[{get_display_name(bb)}](tg://user?id={bb.id})"
        if isinstance(x, rec):
            rece = rece + 1
            if "rec" in okk:
                if not (bb.bot or bb.deleted):
                    xx += f"\n[{get_display_name(bb)}](tg://user?id={bb.id})"
        if isinstance(y, owner):
            if "admin" or "owner" in okk:
                xx += f"\n꧁[{get_display_name(bb)}](tg://user?id={bb.id})꧂"
        if isinstance(y, admin):
            if "admin" in okk:
                if not bb.deleted:
                    xx += f"\n[{get_display_name(bb)}](tg://user?id={bb.id})"
        if "all" in okk:
            if not (bb.bot or bb.deleted):
                xx += f"\n[{get_display_name(bb)}](tg://user?id={bb.id})"
        if "bot" in okk:
            if bb.bot:
                xx += f"\n[{get_display_name(bb)}](tg://user?id={bb.id})"
    await event.client.send_message(e.chat_id, xx)
    await event.delete()


CMD_HELP.update(
    {
        "tags": "**Plugin : **`tags`\
        \n\n  •  **Perintah :** `.tagall`\
        \n  •  **Function : **Tag Top 100 Members di group chat.\
        \n\n  •  **Perintah :** `.tagowner`\
        \n  •  **Function : **Tag Owner group chat\
        \n\n  •  **Perintah : **`.tagadmins`\
        \n  •  **Function : **Tag Admins group chat.\
        \n\n  •  **Perintah :** `.tagbots`\
        \n  •  **Function : **Tag Bots group chat.\
        \n\n  •  **Perintah :** `.tagrec`\
        \n  •  **Function : **Tag Member yang Baru Aktif.\
        \n\n  •  **Perintah :** `.tagon`\
        \n  •  **Function : **Tag Online Members (hanya berfungsi jika privasi dimatikan)\
        \n\n  •  **Perintah :** `.tagoff`\
        \n  •  **Function : **Tag Offline Members (hanya berfungsi jika privasi dimatikan)\
        "
    }
)
