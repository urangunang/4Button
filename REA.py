# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

from pyrogram.types import InlineKeyboardButton

class Data:
    HELP = """
<b> ❏ Perintah untuk Pengguna BOT
 ├ /start - Mulai Bot
 ├ /about - Tentang Bot ini
 ├ /help - Bantuan Perintah Bot ini
 ├ /ping - Untuk mengecek bot hidup
 └ /uptime - Untuk melihat status bot 
 
 ❏ Perintah Untuk Admin BOT
 ├ /logs - Untuk melihat logs bot
 ├ /setvar - Untuk mengatur var dengan command dibot
 ├ /delvar - Untuk menghapus var dengan command dibot
 ├ /getvar - Untuk melihat salah satu var dengan command dibot
 ├ /users - Untuk melihat statistik pengguna bot
 ├ /batch - Untuk membuat link lebih dari satu file
 ├ /speedtest - Untuk Mengetes kecepatan server bot
 └ /broadcast - Untuk mengirim pesan broadcast ke pengguna bot

👨‍💻 Develoved by </b><a href='https://t.me/ReaSupport'><b>ReaSupport</b></a>

Sumber: @Lunatic0de & @Mahadappa
"""

    close = [
        [InlineKeyboardButton("ᴛᴜᴛᴜᴘ", callback_data="close")]
    ]

    mbuttons = [
        [
            InlineKeyboardButton("ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
            InlineKeyboardButton("ᴛᴜᴛᴜᴘ", callback_data="close")
        ],
    ]

    buttons = [
        [
            InlineKeyboardButton("Order Bot", callback_data="order"),
            InlineKeyboardButton("ᴛᴜᴛᴜᴘ", callback_data="close")
        ],
    ]

    ORDER = """
<b>Tentang Bot ini:

@{} adalah Bot Telegram untuk menyimpan Postingan atau File yang dapat Diakses melalui Link Khusus.

 • Creator: @{}
 • Framework: <a href='https://docs.pyrogram.org'>Pyrogram</a>


 Ingin membuat Bot seperti ini chat @SayaKyu
 
👨‍💻 Develoved by </b><a href='https://t.me/ReaSupport'>ReaSupport</a>
"""
