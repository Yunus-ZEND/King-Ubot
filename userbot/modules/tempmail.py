# BASED FROM ULTROID PORTED FOR KING UBOT BY ALVIN / @LIUALVINAS
# THANKS ULTROID
# DONT REMOVE THIS
# ALVIN GANTENG
# @LORDUSERBOT_GROUP

from telethon import events
from userbot import CMD_HELP, bot
from userbot.events import register
from telethon.errors.rpcerrorlist import YouBlockedUserError
import asyncio


@register(outgoing=True, pattern=r"^\.tm(?: |$)(.*)")
async def _(event):
    chat = "@TempMailBot"
    lynx = await event.edit("Sedang Memprosess...")
    async with bot.conversation(chat) as conv:
        try:
            response = conv.wait_event(events.NewMessage(
                incoming=True,
                from_users=220112646
            )
            )
            await conv.send_message("/start")
            await asyncio.sleep(1)
            await conv.send_message("Generate New")
            response = await response
            lynxuserbot = ((response).reply_markup.rows[2].buttons[0].url)
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await king.edit("`Mohon Maaf, Silahkan Buka` @TempMailBot `Lalu Tekan Start dan Coba Lagi.`")
            return
        await event.edit(f"**KING TEMPMAIL** ~ `{response.message.message}`\n\n[KLIK DISINI UNTUK VERIFIKASI]({kingubot})")


# Alvin Ganteng
# Ported For Lynx-Userbot From Ultroid

CMD_HELP.update(
    {
        "tempmail": "**Plugin : **`tempmail`\
        \n\n  •  **Perintah :** `.tm` <menulis teks gmail>\
        \n  •  **Function : **Mendapatkan Email Gratis di Tempmail.\
    "
    }
)
