
# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

from pyrogram.types import InlineKeyboardButton

class Data:
    HELP = """
<b> ❏ BOT COMMAND
 ├ /start - Start Bot or Get Posts
 ├ /about - About This Bot
 ├ /help - Help Command
 ├ /ping - To Check Bot Alive or dead
 └ /uptime - Bot Status
 
 ❏ ADMIN COMMAND
 ├ /logs - Bot Logs
 ├ /setvar - [Admin Command]
 ├ /delvar - [Admin Command]
 ├ /getvar - [Admin Command]
 ├ /users - Bot users
 ├ /batch - Create Link 
 ├ /speedtest - Bot Speed
 └ /broadcast - Broadcast Messages

👨‍💻 Develoved by </b><a href='https://t.me/Netflix_Dual'>@Itz_Zeno</a>
"""

    close = [
        [InlineKeyboardButton("CLOSE", callback_data="close")]
    ]

    mbuttons = [
        [
            InlineKeyboardButton("ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
            InlineKeyboardButton("CLOSE", callback_data="close")
        ],
    ]

    buttons = [
        [
            InlineKeyboardButton("ABOUT", callback_data="about"),
            InlineKeyboardButton("CLOSE", callback_data="close")
        ],
    ]

    ABOUT = """
<b>Bot About:

@{} adalah Bot Telegram untuk menyimpan Postingan atau File yang dapat Diakses melalui Link Khusus.

 • Creator: @{}
 • Anime Movie: <a href='https://t.me/Anime_and_Animation_Movies'>Anime Movie</a>
 • Anime Channel: <a href='https://t.me/Anime_Wide'>Anime Wide</a>

👨‍💻 Develoved by </b><a href='https://t.me/Netflix_Dual'>@Itz_Zeno</a>
"""
