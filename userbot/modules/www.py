# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
# King Ubot
""" Userbot module containing commands related to the \
    Information Superhighway (yes, Internet). """

import asyncio
import time
import redis

from datetime import datetime

from speedtest import Speedtest
from userbot import CMD_HELP, StartTime, ALIVE_NAME
from userbot.events import register


async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["Dtk", "Mnt", "Jam", "Hari"]

    while count < 4:
        count += 1
        remainder, result = divmod(
            seconds, 60) if count < 3 else divmod(
            seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


@register(outgoing=True, pattern="^.error$")
async def redis(pong):
    """ For .ping command, ping the userbot from any chat.  """
    await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("__....................__")
    await pong.edit("__.............__")
    await pong.edit("__..........................__")
    await pong.edit("__...........__")
    await pong.edit("__.......................__")
    await pong.edit("__.................__")
    await pong.edit("__...........................__")
    await pong.edit("__....................__")
    await pong.edit("__𝐄 𝐑 𝐑 𝐎 𝐑__")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**╭━━━━━━━━━━━━━━━━━╮** \n"
                    f"**          - 𝐄 𝐑 𝐑 𝐎 𝐑 -** \n"
                    f"**  ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰** \n"
                    f"**        • ⁴⁰⁴  :** `%sms` \n"
                    f"**        • ⁴⁰⁴   :** `{ALIVE_NAME}` \n"
                    f"**╰━━━━━━━━━━━━━━━━━╯** \n" % (duration))


@register(outgoing=True, pattern="^.kping$")
async def redis(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("`..✘...𝗞𝗶𝗻𝗴..✘...`")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**`{ALIVE_NAME}`**\n"
                    f"✧ **-𝙨𝙞𝙣𝙮𝙖𝙡- :** "
                    f"`%sms` \n"
                    f"✧ **-𝙬𝙖𝙠𝙩𝙪- :** "
                    f"`{uptime}` \n" % (duration))


@register(outgoing=True, pattern="^.xping$")
async def redis(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("__✘__")
    await pong.edit("__✘✘__")
    await pong.edit("__✘✘✘__")
    await pong.edit("__✘__")
    await pong.edit("__✘✘__")
    await pong.edit("__✘✘✘__")
    await pong.edit("__✘__")
    await pong.edit("__✘✘__")
    await pong.edit("__⚡️__")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**👑 King-Ubot 👑**\n"
                    f"➾ __𝙨𝙞𝙣𝙮𝙖𝙡__    __:__ "
                    f"`%sms` \n"
                    f"➾ __𝙬𝙖𝙠𝙩𝙪__ __:__ "
                    f"`{uptime}` \n" % (duration))


@register(outgoing=True, pattern="^.ping$")
async def redis(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("__Connecting to data center.__")
    await pong.edit("__Connecting to data center..__")
    await pong.edit("__Connecting to data center...__")
    await pong.edit("__Connecting to data center.__")
    await pong.edit("__Connecting to data center..__")
    await pong.edit("__Connecting to data center...__")
    await pong.edit("__Connecting to data center.__")
    await pong.edit("__Connecting to data center..__")
    await pong.edit("__Connecting to data center...__")
    await pong.edit("✘")
    await asyncio.sleep(2)
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**═══════════════════** \n"
                    f"**       👑 King-Ubot 👑** \n"
                    f"**════════════════════** \n"
                    f"**➾ 𝙨𝙞𝙣𝙮𝙖𝙡   :** "
                    f"`%sms` \n"
                    f"**➾ 𝙬𝙖𝙠𝙩𝙪  :** "
                    f"`{uptime}` \n"
                    f"**👑 𝙠𝙞𝙣𝙜   :** `{ALIVE_NAME}` \n"
                    f"**═════════════════**" % (duration))


@register(outgoing=True, pattern="^.speed$")
async def speedtst(spd):
    """ For .speed command, use SpeedTest to check server speeds. """
    await spd.edit("`Menjalankan Tes Kecepatan Jaringan, Mohon Tunggu...`")
    test = Speedtest()

    test.get_best_server()
    test.download()
    test.upload()
    test.results.share()
    result = test.results.dict()

    await spd.edit("**Kecepatan Jaringan:\n**"
                   "✧ **Dimulai Pada :** "
                   f"`{result['timestamp']}` \n"
                   f" **━━━━━━━━━━━━━━━━━**\n\n"
                   "✧ **Download:** "
                   f"`{speed_convert(result['download'])}` \n"
                   "✧ **Upload:** "
                   f"`{speed_convert(result['upload'])}` \n"
                   "✧ **Siinyal:** "
                   f"`{result['ping']}` \n"
                   "✧ **ISP:** "
                   f"`{result['client']['isp']}` \n"
                   "✧ **BOT:** 👑 King-Ubot 👑")


def speed_convert(size):
    """
    Hi human, you can't read bytes?
    """
    power = 2**10
    zero = 0
    units = {0: '', 1: 'Kb/s', 2: 'Mb/s', 3: 'Gb/s', 4: 'Tb/s'}
    while size > power:
        size /= power
        zero += 1
    return f"{round(size, 2)} {units[zero]}"


@register(outgoing=True, pattern="^.pong$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    start = datetime.now()
    await pong.edit("`...........✘`")
    await pong.edit("`..........✘.`")
    await pong.edit("`.........✘..`")
    await pong.edit("`........✘...`")
    await pong.edit("`.......✘....`")
    await pong.edit("`......✘.....`")
    await pong.edit("`.....✘......`")
    await pong.edit("`....✘.......`")
    await pong.edit("`...✘........`")
    await pong.edit("`..✘.........`")
    await pong.edit("`.✘..........`")
    await pong.edit("`✘.✘.✘.✘.✘.✘`")
    end = datetime.now()
    duration = (end - start).microseconds / 9000
    await pong.edit(f"**👑 𝙠𝙞𝙣𝙜 : {ALIVE_NAME}**\n`%sms`" % (duration))


CMD_HELP.update(
    {
        "ping": "**✘ Plugin : **`ping`\
        \n\n  •  **Perintah :** `.ping` ; `kping` ; `.xping` ; `.error`\
        \n  •  **Function : **Untuk menunjukkan ping userbot.\
        \n\n  •  **Perintah :** `.pong`\
        \n  •  **Function : **Sama seperti perintah ping\
        \n\n  •  **Perintah :** `.speedtest`\
        \n  •  **Function : **Untuk Mengetes kecepatan server userbot.\
    "
    }
)
