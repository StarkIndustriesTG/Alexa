class script(object):
    START_TXT = """𝙷𝙴𝙻𝙾 {},
𝙼𝚈 𝙽𝙰𝙼𝙴 𝙸𝚂 <a href=https://t.me/{}>{}</a>, 𝙸 𝙲𝙰𝙽 𝙿𝚁𝙾𝚅𝙸𝙳𝙴 𝙼𝙾𝚅𝙸𝙴𝚂, 𝙹𝚄𝚂𝚃 𝙰𝙳𝙳 𝙼𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 𝙰𝙽𝙳 𝙼𝙰𝙺𝙴 𝙼𝙴 𝙰𝙳𝙼𝙸𝙽.. 𝚃𝙷𝙴𝙽 𝚂𝙴𝙴 𝙼𝚈 𝙿𝙾𝚆𝙴𝚁𝚂 ♥️♥️🔥"""
    HELP_TXT = """𝙷𝙴𝚈 {}
𝙷𝙴𝚁𝙴 𝙸𝚂 𝚃𝙷𝙴 𝙷𝙴𝙻𝙿 𝙵𝙾𝚁 𝙼𝚈 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂."""
    ABOUT_TXT = """✪ 𝙼𝚈 𝙽𝙰𝙼𝙴: {}
✪ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁: <a href='https://telegram.dog/heart_recipe'>➳ ✰ 𝑶𝒐 𝑰𝒕'𝒔 𝑴𝒆 🤦</a>
✪ 𝙻𝙸𝙱𝚁𝙰𝚁𝚈: <a href='https://docs.pyrogram.com'>𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼</a>
✪ 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴: 𝙿𝚈𝚃𝙷𝙾𝙽 𝟹
✪ 𝙳𝙰𝚃𝙰 𝙱𝙰𝚂𝙴: 𝙼𝙾𝙽𝙶𝙾 𝙳𝙱
✪ 𝙱𝙾𝚃 𝚂𝙴𝚁𝚅𝙴𝚁: 𝙷𝙴𝚁𝙾𝙺𝚄
✪ 𝙱𝚄𝙸𝙻𝙳 𝚂𝚃𝙰𝚃𝚄𝚂   : v1.0.1 [ 𝙱𝙴𝚃𝙰 ]
✪ 𝚄𝙿𝙳𝙰𝚃𝙴𝚂: <a href='https://telegram.dog/VK_LINKZ'>𝙲𝙻𝙸𝙲𝙺 𝙷𝙴𝚁𝙴</a>
✪ 𝙼𝙾𝚅𝙸𝙴𝚂 𝙲𝙷𝙰𝙽𝙽𝙴𝙻: <a href='https://telegram.dog/+XX7Ox8faMtE1ZTY1'>𝚃𝙾𝚄𝙲𝙷 𝙷𝙴𝚁𝙴</a>"""
    DONATION_TXT = """<b>𝐃𝐨𝐧𝐚𝐭𝐢𝐨𝐧 & 𝐏𝐚𝐢𝐝 𝐏𝐫𝐨𝐦𝐨𝐭𝐢𝐨𝐧</b> 

›› <b>𝐃𝐨𝐧𝐚𝐭𝐢𝐨𝐧</b>

⪼ <b>𝐘𝐨𝐮 𝐂𝐚𝐧 𝐃𝐨𝐧𝐚𝐭𝐞 𝐀𝐧𝐲 𝐀𝐦𝐨𝐮𝐧𝐭 𝐘𝐨𝐮 𝐇𝐚𝐯𝐞 💳. 
<b>━━━━━━━━━᚜ Payment Methods ᚛━━━━━━━━━
✮ 𝗚𝗼𝗼𝗴𝗹𝗲𝗣𝗮𝘆
✮ 𝗣𝗮𝘆𝘁𝗺
✮ 𝗣𝗵𝗼𝗻𝗲𝗣𝗲
✮ 𝗣𝗮𝘆𝗣𝗮𝗹
_𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐌𝐞 𝐅𝐨𝐫 𝐊𝐧𝐨𝐰 𝐀𝐛𝐨𝐮𝐭 𝐓𝐡𝐞 𝐏𝐚𝐲𝐦𝐞𝐧𝐭 𝐈𝐧𝐟𝐨_
━━━━━━━━━━━━᚜ <a href=https://t.me/Aadhi011><b>ꪖꪖᦔꫝỉ</b></a> ᚛━━━━━━━━━━━━

›› <b>𝐏𝐚𝐢𝐝 𝐏𝐫𝐨𝐦𝐨𝐭𝐢𝐨𝐧</b>

⪼ <b>𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐌𝐞 𝐖𝐢𝐭𝐡 𝐘𝐨𝐮 𝐂𝐨𝐧𝐭𝐞𝐧𝐭 𝐖𝐡𝐢𝐜𝐡 𝐘𝐨𝐮 𝐖𝐚𝐧𝐭 𝐓𝐨 𝐏𝐫𝐨𝐦𝐨𝐭𝐞 . 
<b>━━━━━━━━━᚜ Payment Methods ᚛━━━━━━━━━
✮ 𝗚𝗼𝗼𝗴𝗹𝗲𝗣𝗮𝘆
✮ 𝗣𝗮𝘆𝘁𝗺
✮ 𝗣𝗵𝗼𝗻𝗲𝗣𝗲
✮ 𝗣𝗮𝘆𝗣𝗮𝗹
_𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐌𝐞 𝐖𝐢𝐭𝐡 𝐘𝐨𝐮𝐫 𝐂𝐨𝐧𝐭𝐞𝐧𝐭 𝐀𝐧𝐝 𝐊𝐧𝐨𝐰 𝐀𝐛𝐨𝐮𝐭 𝐓𝐡𝐞 𝐏𝐚𝐲𝐦𝐞𝐧𝐭 𝐈𝐧𝐟𝐨_
━━━━━━━━━━━━᚜ <a href=https://t.me/Aadhi011><b>ꪖꪖᦔꫝỉ</b></a> ᚛━━━━━━━━━━━━"""
    PROMOTION_TXT = """<b>〄 𝐏𝐚𝐢𝐝 𝐏𝐫𝐨𝐦𝐨𝐭𝐢𝐨𝐧 〄</b>

⪼ <b>𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐌𝐞 𝐖𝐢𝐭𝐡 𝐘𝐨𝐮 𝐂𝐨𝐧𝐭𝐞𝐧𝐭 𝐖𝐡𝐢𝐜𝐡 𝐘𝐨𝐮 𝐖𝐚𝐧𝐭 𝐓𝐨 𝐏𝐫𝐨𝐦𝐨𝐭𝐞 . 
<b>━━━━━━━━━᚜ Payment Methods ᚛━━━━━━━━━
✮ 𝗚𝗼𝗼𝗴𝗹𝗲𝗣𝗮𝘆
✮ 𝗣𝗮𝘆𝘁𝗺
✮ 𝗣𝗵𝗼𝗻𝗲𝗣𝗲
✮ 𝗣𝗮𝘆𝗣𝗮𝗹
_𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐌𝐞 𝐖𝐢𝐭𝐡 𝐘𝐨𝐮𝐫 𝐂𝐨𝐧𝐭𝐞𝐧𝐭 𝐀𝐧𝐝 𝐊𝐧𝐨𝐰 𝐀𝐛𝐨𝐮𝐭 𝐓𝐡𝐞 𝐏𝐚𝐲𝐦𝐞𝐧𝐭 𝐈𝐧𝐟𝐨_
━━━━━━━━━━━━᚜ <a href=https://t.me/Aadhi011><b>ꪖꪖᦔꫝỉ</b></a> ᚛━━━━━━━━━━━━""" 
    FILE_TXT = """➤ 𝐇𝐞𝐥𝐩: 𝐅𝐢𝐥𝐞 𝐒𝐭𝐨𝐫𝐞 𝐌𝐨𝐝𝐮𝐥𝐞../

<b>By Using This Module You can store files in My database and I will You A Permanent link To access The saved Files.If You want to add files from a Public channel send the file link only or You want to store files from a Private channel you must make me admin on their to access files files.../</b>

⪼ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞 ›

➪ /plink ›› <b>𝖱𝖾𝗉𝗅𝗒 𝗍𝗈 𝖺𝗇𝗒 𝗆𝖾𝖽𝗂𝖺 𝗍𝗈 𝗀𝖾𝗍 𝗅𝗂𝗇𝗄.</b>
➪ /pbatch ›› <b>𝖴𝗌𝖾 𝗒𝗈𝗎𝗋 𝗆e𝖽𝗂𝖺 𝗅𝗂𝗇𝗄 𝗐𝗂𝗍𝗁 𝗍𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽.</b>
➪ /batch ›› <b>To Create Link For Multiple Post.</b>

⪼ 𝐄𝐱𝐚𝐦𝐩𝐥𝐞 ›

<code>/batch https://t.me/c/1749754594/332 https://t.me/c/1749754594/336</code>"""
    WHOIS_TXT ="""<b>WHOIS MODULE</b>
Note:- Give a user details
•/whois :-give a user full details"""
    FUN_TXT ="""<b>Gᴀᴍᴇs</b> 
    
<b>🎲 NOTHING MUCH JUST SOME FUN THINGS</b>
t𝗋𝗒 𝗍𝗁𝗂𝗌 𝖮𝗎𝗍: 
𝟣. /dice - Roll The Dice 
𝟤. /Throw 𝗈𝗋 /Dart - 𝖳𝗈 𝖬𝖺𝗄𝖾 Drat 
3. /Runs - Jokes 
4. /Goal or /Shoot - To Make A Goal Or Shoot
5. /luck or /cownd - Spin the Lucky"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and ᗩᒍᗩ᙭  will respond whenever a keyword is found the message

<b>NOTE:</b>
1. ᗩᒍᗩ᙭ should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    SONG_TXT = """<b>🎼Song Download🎼</b>
Song Download Module, For Those Who Love Music

<b>🎈 Command 🎈</b>

- /song [Song Name] - To Download Music 😁

<b>🌀Usage🌀</b>
- Can Be Used By Everyone
- Works in bot pm

Made By <a href=https://t.me/+veUIdIW2CQ5mOGU5>𝐌𝐖 𝐔𝐩𝐝𝐚𝐭𝐞𝐬</a>"""
    PIN_TXT ="""<b>PIN MODULE</b>
<b>Pin :</b>

<b>All The Pin Related Commands Can Be Found Here; Keep Your Chat Up To Date On The Latest News With A Simple Pinned Message!</b>

<b>📚 Commands & Usage:</b>

◉ /pin :- Pin The Message You Replied To Message To Send A Notification To Group Members
◉ /unpin :- Unpin The Current Pinned Message. If Used As A Reply, Unpins The Replied To Message"""
    PASTE_TXT = """Help: <b>Paste</b>

Paste some texts or documents on a website!

<b>Commands and Usage:</b>

• /paste [text] - paste the given text on Pasty

<b>NOTE:</b>

• These commands works on both pm and group.
• These commands can be used by any group member."""
    GTRANS_TXT = """Help: <b> TTS 🎤 module:</b>

Translate text to speech

<b>Commands and Usage:</b>

• /tts <text> : convert text to speech

<b>NOTE:</b>

• IMDb should have admin privillage.
• These commands works on both pm and group.
• IMDb can translate texts to 200+ languages."""
    PINGS_TXT ="""<b>🌟 Ping:</b>

Helps you to know your ping 🚶🏼‍♂️

<b>Commands:</b>

• /alive - To check you are alive.
• /help - To get help 
• /ping - To get your ping 
• /repo - Source Code. 

<b>🏹Usage🏹 :</b>

• This commands can be used in pms and groups
• This commands can be used buy everyone in the groups and bots pm
• Share us for more features"""
    TELE_TXT = """<b>▫️HELP: Telegraph▪️</b>

Do as you wish with telegra.ph module!

</b>USAGE:</b>

🤧 /telegraph - Send me Picture or Vide Under (5MB)

<b>NOTE:</b>

• This Command Is Available in goups and pms
• This Command Can be used by everyone"""
    JSON_TXT ="""<b>JSON:</b>

Bot returns json for all replied messages with /json

<b>Features:</b>

Message Editting JSON
Pm Support
Group Support

<b>Note:</b>

Everyone can use this command , if spaming happens bot will automatically ban you from the group."""
    PURGE_TXT = """<b>💣Purge💣</b>
    
Delete A Lot Of Messages From Groups! 
    
 <b>ADMIN</b> 

◉ /purge :- Delete All Messages From The Replied To Message, To The Current Message"""
    BUTTON_TXT = """Help: <b>Buttons</b>

-ᗩᒍᗩ᙭  Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. ᗩᒍᗩ᙭ supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/+veUIdIW2CQ5mOGU5)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>𝙽𝙾𝚃𝙴:</b>

𝚃𝙷𝙴𝚂𝙴 𝙰𝚁𝙴 𝚃𝙷𝙴 𝙴𝚇𝚃𝚁𝙰 𝙵𝙴𝙰𝚃𝚄𝚁𝙴𝚂 

<b>𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 𝙰𝙽𝙳 𝚄𝚂𝙰𝙶𝙴:</b>

✯ /id - <code>𝚃𝙾 𝙶𝙴𝚃 𝙸𝙳 𝙾𝙵 𝙰 𝚂𝙿𝙴𝙲𝙸𝙵𝙸𝙴𝙳 𝚄𝚂𝙴𝚁.</code>
✯ /info  - <code>𝙶𝙴𝚃 𝙸𝙽𝙵𝙾𝚁𝙼𝙰𝚃𝙸𝙾𝙽 𝙰𝙱𝙾𝚄𝚃 𝙰 𝚄𝚂𝙴𝚁.</code>
✯ /imdb  - <code>𝙶𝙴𝚃 𝚃𝙷𝙴 𝙵𝙻𝙸𝙼 𝙸𝙽𝙵𝙾𝚁𝙼𝙰𝚃𝙸𝙾𝙽 𝙵𝙾𝚁 𝙸𝙼𝙳𝙱 𝚂𝙾𝚄𝚁𝙲𝙴.</code>
✯ /search  - <code>𝙶𝙴𝚃 𝚃𝙷𝙴 𝙵𝙻𝙸𝙼 𝙸𝙽𝙵𝙾𝚁𝙼𝙰𝚃𝙸𝙾𝙽 𝙵𝚁𝙾𝙼 𝚅𝙰𝚁𝙸𝙾𝚄𝚂 𝚂𝙾𝚄𝚁𝙲𝙴𝚂.</code>"""
    ADMIN_TXT = """➤ 𝙷𝙴𝙻𝙿: <b>𝙰𝙳𝙼𝙸𝙽 𝙼𝙾𝙳𝚂</b>

<b>𝙽𝙾𝚃𝙴:</b>

𝚃𝙷𝙸𝚂 𝙼𝙾𝙳𝚄𝙻𝙴 𝚆𝙾𝚁𝙺𝚂 𝙾𝙽𝙻𝚈 𝙵𝙾𝚁 𝙰𝙳𝙼𝙸𝙽𝚂

<b>𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 𝙰𝙽𝙳 𝚄𝚂𝙰𝙶𝙴:</b>

✯ /logs - <code>𝚃𝙾 𝙶𝙴𝚃 𝚃𝙷𝙴 𝚁𝙴𝚂𝙲𝙴𝙽𝚃 𝙴𝚁𝚁𝙾𝚁𝚂</code>
✯ /stats - <code>𝚃𝙾 𝙶𝙴𝚃 𝚃𝙷𝙴 𝚂𝚃𝙰𝚃𝚄𝚂 𝙾𝙵 𝙵𝙸𝙻𝙴𝚂 𝙸𝙽 𝙳𝙱.</code>
✯ /delete - <code>𝚃𝙾 𝙳𝙴𝙻𝙴𝚃𝙴 𝙰 𝚂𝙿𝙴𝙲𝙸𝙵𝙸𝙲 𝙵𝙸𝙻𝙴 𝙵𝚁𝙾𝙼 𝙳𝙱.</code>
✯ /users - <code>𝚃𝙾 𝙶𝙴𝚃 𝙻𝙸𝚂𝚃 𝙾𝙵 𝙼𝚈 𝚄𝚂𝙴𝚁𝚂 𝙰𝙽𝙳 𝙸𝙳𝚂.</code>
✯ /chats - <code>𝚃𝙾 𝙶𝙴𝚃 𝙻𝙸𝚂𝚃 𝙾𝙵 𝚃𝙷𝙴 𝙼𝚈 𝙲𝙷𝙰𝚃𝚂 𝙰𝙽𝙳 𝙸𝙳𝚂.</code>
✯ /leave  - <code>𝚃𝙾 𝙻𝙴𝙰𝚅𝙴 𝙵𝚁𝙾𝙼 𝙰 𝙲𝙷𝙰𝚃.</code>
✯ /disable  -  <code>𝚃𝙾 𝙳𝙸𝚂𝙰𝙱𝙻𝙴 𝙰 𝙲𝙷𝙰𝚃.</code>
✯ /ban_user  - <code>𝚃𝙾 𝙱𝙰𝙽 𝙰 𝚄𝚂𝙴𝚁.</code>
✯ /unban_user  - <code>𝚃𝙾 𝚄𝙽𝙱𝙰𝙽 𝙰 𝚄𝚂𝙴𝚁.</code>
✯ /channel - <code>𝚃𝙾 𝙶𝙴𝚃 𝙻𝙸𝚂𝚃 𝙾𝙵 𝚃𝙾𝚃𝙰𝙻 𝙲𝙾𝙽𝙽𝙴𝙲𝚃𝙴𝙳 𝙲𝙷𝙰𝙽𝙽𝙴𝙻𝚂.</code>
✯ /broadcast - <code>𝚃𝙾 𝙱𝚁𝙾𝙳𝙲𝙰𝚂𝚃 𝙰 𝙼𝙴𝚂𝚂𝙰𝙶𝙴 𝚃𝙾 𝙰𝙻𝙻 𝚄𝚂𝙴𝚁𝚂.</code>"""
    STATUS_TXT = """<b>᚛› 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code></b>
<b>✫ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code></b>
<b>✫ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code></b>
<b>✫ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝙱</b>
<b>✫ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝙱</b>"""
    LOG_TEXT_G = """#𝐍𝐞𝐰𝐆𝐫𝐨𝐮𝐩
    
<b>᚛› 𝙶𝚁𝙾𝚄𝙿 ⪼ {}(<code>{}</code>)</b>
<b>᚛› 𝚃𝙾𝚃𝙰𝙻 𝙼𝙴𝙼𝙱𝙴𝚁𝚂 ⪼ <code>{}</code></b>
<b>᚛› 𝙰𝙳𝙳𝙴𝙳 𝙱𝚈 ⪼ {}</b>
"""
    LOG_TEXT_P = """#𝐍𝐞𝐰𝐔𝐬𝐞𝐫
    
<b>᚛› 𝐈𝐃 - <code>{}</code></b>
<b>᚛› 𝐍𝐚𝐦𝐞 - {}</b>
"""
    REPORT_TXT = """➤ 𝙷𝙴𝙻𝙿: 𝚁𝙴𝙿𝙾𝚁𝚃 ⚠️

𝚃𝙷𝙸𝚂 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 𝙷𝙴𝙻𝙿 𝚈𝙾𝚄 𝚃𝙾 𝚁𝙴𝙿𝙾𝚁𝚃 𝙰 𝙼𝙴𝚂𝚂𝙰𝙶𝙴 𝙾𝚁 𝙰 𝚄𝚂𝙴𝚁 𝚃𝙾 𝚃𝙷𝙴 𝚁𝙴𝚂𝙿𝙴𝙲𝚃𝙸𝚅𝙴 𝙶𝚁𝙾𝚄𝙿 𝙰𝙳𝙼𝙸𝙽𝚂.𝙳𝙾𝙽'𝚃 𝙼𝙸𝚂𝚄𝚂𝙴 𝚃𝙷𝙸𝚂 𝙲𝙾𝙼𝙼𝙰𝙽𝙳.

➤ 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 𝙰𝙽𝙳 𝚄𝚂𝙰𝙶𝙴 :

➪/report 𝗈𝗋 @admins - 𝚃𝙾 𝚁𝙴𝙿𝙾𝚁𝚃 𝙰 𝚄𝚂𝙴𝚁 𝚃𝙾 𝚃𝙷𝙴 𝙰𝙳𝙼𝙸𝙽𝚂 (𝚁𝙴𝙿𝙻𝚈 𝚃𝙾 𝙰 𝙼𝙴𝚂𝚂𝙰𝙶𝙴)."""

    CORONA_TXT = """➤ 𝙷𝙴𝙻𝙿: 𝙲𝙾𝚅𝙸𝙳

𝚃𝙷𝙸𝚂 𝙲𝙾𝙼𝙼𝙰𝙽𝙳 𝙷𝙴𝙻𝙿𝚂 𝚈𝙾𝚄 𝙺𝙽𝙾𝚆 𝙳𝙰𝙸𝙻𝚈 𝙸𝙽𝙵𝙾𝚁𝙼𝙰𝚃𝙸𝙾𝙽 𝙰𝙱𝙾𝚄𝚃 𝙲𝙾𝚅𝙸𝙳

➤ 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 𝙰𝙽𝙳 𝚄𝚂𝙰𝙶𝙴:

➪ /covid - 𝚄𝚂𝙴 𝚃𝙷𝙸𝚂 𝙲𝙾𝙼𝙼𝙰𝙽𝙳 𝚆𝙸𝚃𝙷 𝚈𝙾𝚄𝚁 𝙲𝙾𝚄𝙽𝚃𝚁𝚈 𝙽𝙰𝙼𝙴 𝚃𝙾 𝙶𝙴𝚃 𝙲𝙾𝚅𝙸𝙳 𝙸𝙽𝙵𝙾𝚁𝙼𝙰𝚃𝙸𝙾𝙽

✎ 𝙴𝚇𝙰𝙼𝙿𝙻𝙴:

/covid 𝖨𝗇𝖽𝗂𝖺"""

    URLSHORT_TXT = """➤ 𝙷𝙴𝙻𝙿: 𝚄𝚁𝙻 𝚂𝙷𝙾𝚁𝚃𝙽𝙴𝚁

𝚃𝙷𝙸𝚂 𝙲𝙾𝙼𝙼𝙰𝙽𝙳 𝙷𝙴𝙻𝙿𝚂 𝚈𝙾𝚄 𝚃𝙾 𝚂𝙷𝙾𝚁𝚃 𝙰 𝚄𝚁𝙻

➤ 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 𝙰𝙽𝙳 𝚄𝚂𝙰𝙶𝙴 :

➪ /short: 𝚄𝚂𝙴 𝚃𝙷𝙸𝚂 𝙲𝙾𝙼𝙼𝙰𝙽𝙳 𝚆𝙸𝚃𝙷 𝚈𝙾𝚄𝚁 𝙻𝙸𝙽𝙺 𝚃𝙾 𝙶𝙴𝚃 𝚂𝙷𝙾𝚁𝚃𝙴𝙳 𝙻𝙸𝙽𝙺𝚂

✎ 𝙴𝚇𝙰𝙼𝙿𝙻𝙴:

/short https://t.me/VK_LINKZ"""

    VIDEO_TXT ="""𝙷𝙴𝙻𝙿 𝚈𝙾𝚄 𝚃𝙾 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝚅𝙸𝙳𝙴𝙾 𝙵𝚁𝙾𝙼 𝚈𝙾𝚄𝚃𝚄𝙱𝙴.

• 𝚄𝚂𝙰𝙶𝙴

𝚈𝙾𝚄 𝙲𝙰𝙽 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝙰𝙽𝚈 𝚅𝙸𝙳𝙴𝙾 𝙵𝚁𝙾𝙼 𝚈𝙾𝚄𝚃𝚄𝙱𝙴

🤔 𝙷𝙾𝚆 𝚃𝙾 𝚄𝚂𝙴

• 𝚃𝚈𝙿𝙴 /video or /mp4 𝙰𝙽𝙳 (𝚅𝙸𝙳𝙴𝙾 𝙻𝙸𝙽𝙺)

• 𝙴𝚇𝙰𝙼𝙿𝙻𝙴:

/𝘮𝘱4 https://youtu.be/Your Link"""

    ZOMBIES_TXT = """𝙷𝙴𝙻𝙿 𝚈𝙾𝚄 𝚃𝙾 𝙺𝙸𝙲𝙺 𝚄𝚂𝙴𝚁𝚂

<b>𝙺𝙸𝙲𝙺 𝙸𝙽𝙰𝙲𝚃𝙸𝚅𝙴 𝙼𝙴𝙼𝙱𝙴𝚁𝚂 𝙵𝚁𝙾𝙼 𝙶𝚁𝙾𝚄𝙿,𝙰𝙳𝙳 𝙼𝙴 𝙰𝚂 𝙰𝙳𝙼𝙸𝙽 𝚆𝙸𝚃𝙷 𝙱𝙰𝙽 𝚄𝚂𝙴𝚁𝚂 𝙿𝙴𝚁𝙼𝙸𝚂𝚂𝙸𝙾𝙽 𝙸𝙽 𝙶𝚁𝙾𝚄𝙿.</b>

<b>𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 𝙰𝙽𝙳 𝚄𝚂𝙰𝙶𝙴:</b>

✯ /inkick - 𝙲𝙾𝙼𝙼𝙰𝙽𝙳 𝚆𝙸𝚃𝙷 𝚁𝙴𝚀𝚄𝙸𝚁𝙴𝙳 𝙰𝚁𝙶𝚄𝙼𝙽𝙴𝚃𝚂 𝙰𝙽𝙳 𝙸 𝚆𝙸𝙻𝙻 𝙺𝙸𝙲𝙺 𝙼𝙴𝙼𝙱𝙴𝚁𝚂 𝙵𝚁𝙾𝙼 𝙶𝚁𝙾𝚄𝙿.
✯ /instatus - 𝚃𝙾 𝙲𝙷𝙴𝙲𝙺  𝙲𝚄𝚁𝚁𝙴𝙽𝚃 𝚂𝚃𝙰𝚃𝚄𝚂 𝙾𝙵 𝙲𝙷𝙰𝚃 𝙼𝙴𝙼𝙱𝙴𝚁 𝙵𝚁𝙾𝙼 𝙶𝚁𝙾𝚄𝙿.
✯ /inkick within_month long_time_ago - 𝚃𝙾 𝙺𝙸𝙲𝙺 𝙼𝙴𝙼𝙱𝙴𝚁𝚂 𝚆𝙷𝙾 𝙰𝚁𝙴 𝙾𝙵𝙵𝙻𝙸𝙽𝙴 𝙵𝙾𝚁 𝙼𝙾𝚁𝙴 𝚃𝙷𝙰𝙽 6 - 7 𝙳𝙰𝚈𝚂.
✯ /inkick long_time_ago - 𝚃𝙾 𝙺𝙸𝙲𝙺 𝙼𝙴𝙼𝙱𝙴𝚁𝚂 𝚆𝙷𝙾 𝙰𝚁𝙴 𝙾𝙵𝙵𝙻𝙸𝙽𝙴 𝙵𝙾𝚁 𝙼𝙾𝚁𝙴 𝚃𝙷𝙰𝙽 𝙰 𝙼𝙾𝙽𝚃𝙷 𝙰𝙽𝙳 𝙳𝙴𝙻𝙴𝚃𝙴𝙳 𝙰𝙲𝙲𝙾𝚄𝙽𝚃𝚂.
✯ /dkick - 𝚃𝙾 𝙺𝙸𝙲𝙺 𝙳𝙴𝙻𝙴𝚃𝙴𝙳 𝙰𝙲𝙲𝙾𝚄𝙽𝚃𝚂."""

    IMAGE_TXT = """➤ 𝙷𝙴𝙻𝙿: 𝙸𝙼𝙰𝙶𝙴

𝚃𝙷𝙸𝚂 𝙲𝙾𝙼𝙼𝙰𝙽𝙳 𝙷𝙴𝙻𝙿𝚂 𝚈𝙾𝚄 𝚃𝙾 𝙴𝙳𝙸𝚃 𝙰 𝙸𝙼𝙰𝙶𝙴 𝚅𝙴𝚁𝚈 𝙴𝙰𝚂𝙸𝙻𝚈

➤ 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 𝙰𝙽𝙳 𝚄𝚂𝙰𝙶𝙴:

➪ 𝙹𝚄𝚂𝚃 𝚂𝙴𝙽𝙳 𝙼𝙴 𝙰 𝙸𝙼𝙰𝙶𝙴 𝚃𝙾 𝙴𝙳𝙸𝚃 🤳

𝙼𝙰𝙳𝙴 𝙱𝚈 <a href=https://telegram.dog/heart_recipe>➳ ✰ 𝑶𝒐 𝑰𝒕'𝒔 𝑴𝒆 🤦</a>"""

    STICKER_TXT = """𝚈𝙾𝚄 𝙲𝙰𝙽 𝚄𝚂𝙴 𝚃𝙷𝙸𝚂 𝙼𝙾𝙳𝚄𝙻𝙴 𝚃𝙾 𝙵𝙸𝙽𝙳 𝙰𝙽𝚈 𝚂𝚃𝙸𝙲𝙺𝙴𝚁𝚂 𝙸𝙳.

❂ 𝚄𝚂𝙰𝙶𝙴

𝚃𝙾 𝙶𝙴𝚃 𝚂𝚃𝙸𝙲𝙺𝙴𝚁 𝙸𝙳
 
  🤔 𝙷𝙾𝚆 𝚃𝙾 𝚄𝚂𝙴
 
➳ 𝚁𝙴𝙿𝙻𝚈 𝚃𝙾 𝙰𝙽𝚈 𝚂𝚃𝙸𝙲𝙺𝙴𝚁 [/stickerid]"""

    YTTHUMB_TXT = """𝙷𝙴𝙻𝙿𝚂 𝚃𝙾 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝙰𝙽𝚈 𝚈𝙾𝚄𝚃𝚄𝙱𝙴 𝚅𝙸𝙳𝙴𝙾 𝚃𝙷𝚄𝙼𝙱𝙽𝙰𝙸𝙻
    
🤔 𝙷𝙾𝚆 𝚃𝙾 𝚄𝚂𝙴

𝚃𝚈𝙿𝙴 /ytthumb 𝙰𝙽𝙳 𝚅𝙸𝙳𝙴𝙾 𝙻𝙸𝙽𝙺

✎ 𝙴𝚇𝙰𝙼𝙿𝙻𝙴

/ytthumb https://youtu.be/yourlink"""

    ABOOK_TXT = """➤ 𝙷𝙴𝙻𝙿: 𝙰𝚄𝙳𝙸𝙾𝙱𝙾𝙾𝙺

𝚈𝙾𝚄 𝙲𝙰𝙽 𝙲𝙾𝙽𝚅𝙴𝚁𝚃 𝙰 𝙿𝙳𝙵 𝙵𝙸𝙻𝙴 𝚃𝙾 𝙰 𝙰𝚄𝙳𝙸𝙾 𝙵𝙸𝙻𝙴 𝚆𝙸𝚃𝙷 𝚃𝙷𝙸𝚂 𝙲𝙾𝙼𝙼𝙰𝙽𝙳 ✯

➤ 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 𝙰𝙽𝙳 𝚄𝚂𝙰𝙶𝙴:

➪ /audiobook: 𝚁𝙴𝙿𝙻𝚈 𝚃𝙷𝙸𝚂 𝙲𝙾𝙼𝙼𝙰𝙽𝙳 𝚆𝙸𝚃𝙷 𝙰𝙽𝚈 𝙿𝙳𝙵 𝚃𝙾 𝙶𝙴𝙽𝙴𝚁𝙰𝚃𝙴 𝚃𝙷𝙴 𝙰𝚄𝙳𝙸𝙾"""

    GTRANS_TXT = """➤ 𝙷𝙴𝙻𝙿: 𝙶𝙾𝙾𝙶𝙻𝙴 𝚃𝚁𝙰𝙽𝚂𝙻𝙰𝚃𝙴𝚁

𝚃𝙷𝙸𝚂 𝙲𝙾𝙼𝙼𝙰𝙽𝙳 𝙷𝙴𝙻𝙿𝚂 𝚈𝙾𝚄 𝚃𝙾 𝚃𝚁𝙰𝙽𝚂𝙻𝙰𝚃𝙴 𝙰 𝚃𝙴𝚇𝚃 𝚃𝙾 𝙰𝙽𝚈 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴𝚂 𝚈𝙾𝚄 𝚆𝙰𝙽𝚃.𝚃𝙷𝙸𝚂 𝙲𝙾𝙼𝙼𝙰𝙽𝙳 𝚆𝙾𝚁𝙺𝚂 𝙸𝙽 𝙱𝙾𝚃𝙷 𝙿𝙼 𝙰𝙽𝙳 𝙶𝚁𝙾𝚄𝙿 ✯

➤ 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 𝙰𝙽𝙳 𝚄𝚂𝙰𝙶𝙴:

➪/tr - 𝚃𝙾 𝚃𝚁𝙰𝙽𝚂𝙻𝙰𝚃𝙴 𝚃𝙴𝚇𝚃𝚂 𝚃𝙾 𝙰 𝚂𝙿𝙴𝙲𝙸𝙵𝙸𝙲 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴

➤ 𝙽𝙾𝚃𝙴:
𝚆𝙷𝙸𝙻𝙴 𝚄𝚂𝙸𝙽𝙶 /tr 𝚈𝙾𝚄 𝚂𝙷𝙾𝚄𝙻𝙳 𝚂𝙿𝙴𝙲𝙸𝙵𝚈 𝚃𝙷𝙴 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴 𝙲𝙾𝙳𝙴

✎ 𝙴𝚇𝙰𝙼𝙿𝙻𝙴: /𝗍𝗋 𝗆𝗅
 • 𝖾𝗇 = 𝙴𝙽𝙶𝙻𝙸𝚂𝙷
 • 𝗆𝗅 = 𝙼𝙰𝙻𝙰𝚈𝙰𝙻𝙰𝙼
 • 𝗁𝗂 = 𝙷𝙸𝙽𝙳𝙸"""

    RESTRIC_TXT = """➤ 𝙷𝙴𝙻𝙿: 𝙼𝚄𝚃𝙴 🚫

𝚃𝙷𝙴𝚂𝙴 𝙰𝚁𝙴 𝚃𝙷𝙴 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 𝙵𝙾𝚁 𝙰 𝙶𝚁𝙾𝚄𝙿 𝙰𝙳𝙼𝙸𝙽 𝚆𝙷𝙸𝙲𝙷 𝙲𝙰𝙽 𝚄𝚂𝙴 𝚃𝙾 𝙼𝙰𝙽𝙰𝙶𝙴 𝚃𝙷𝙴𝙸𝚁 𝙶𝚁𝙾𝚄𝙿 𝙴𝙵𝙵𝙸𝙲𝙸𝙴𝙽𝚃𝙻𝚈.

➪/ban: 𝚃𝙾 𝙱𝙰𝙽 𝙰 𝚄𝚂𝙴𝚁 𝙵𝚁𝙾𝙼 𝚃𝙷𝙴 𝙶𝚁𝙾𝚄𝙿.
➪/unban: 𝚃𝙾 𝚄𝙽𝙱𝙰𝙽 𝙰 𝚄𝚂𝙴𝚁 𝙸𝙽 𝚃𝙷𝙴 𝙶𝚁𝙾𝚄𝙿.
➪/tban: 𝚃𝙾 𝚃𝙴𝙼𝙿𝙾𝚁𝙰𝚁𝙸𝙻𝚈 𝙱𝙰𝙽 𝙰 𝚄𝚂𝙴𝚁.
➪/mute: 𝚃𝙾 𝙼𝚄𝚃𝙴 𝙰 𝚄𝚂𝙴𝚁 𝙸𝙽 𝚃𝙷𝙴 𝙶𝚁𝙾𝚄𝙿.
➪/unmute: 𝚃𝙾 𝚄𝙽𝙼𝚄𝚃𝙴 𝚃𝙷𝙴 𝚄𝚂𝙴𝚁 𝙸𝙽 𝚃𝙷𝙴 𝙶𝚁𝙾𝚄𝙿.
➪/tmute: 𝚃𝙾 𝚃𝙴𝙼𝙿𝙾𝚁𝙰𝚁𝙸𝙻𝚈 𝙼𝚄𝚃𝙴 𝙰 𝚄𝚂𝙴𝚁.

➤ 𝙽𝙾𝚃𝙴:
𝚆𝙷𝙸𝙻𝙴 𝚄𝚂𝙸𝙽𝙶 /tmute 𝗈𝗋 /tban 𝚈𝙾𝚄 𝚂𝙷𝙾𝚄𝙻𝙳 𝚂𝙿𝙴𝙲𝙸𝙵𝚈 𝚃𝙷𝙴 𝚃𝙸𝙼𝙴 𝙻𝙸𝙼𝙸𝚃.

✎ 𝙴𝚇𝙰𝙼𝙿𝙻𝙴: /𝗍𝖻𝖺𝗇 2𝖽 𝗈𝗋 /𝗍𝗆𝗎𝗍𝖾 2𝖽.
𝚈𝙾𝚄 𝙲𝙰𝙽 𝚄𝚂𝙴 𝚅𝙰𝙻𝚄𝙴𝚂: 𝗆/𝗁/𝖽. 
 • 𝗆 = 𝙼𝙸𝙽𝚄𝚃𝙴𝚂
 • 𝗁 = 𝙷𝙾𝚄𝚁𝚂
 • 𝖽 = 𝙳𝙰𝚈𝚂"""
    CREATOR_REQUIRED = """❗<b>𝚈𝙾𝚄 𝙷𝙰𝚅𝙴 𝚃𝙾 𝙱𝙴 𝚃𝙷𝙴 𝙶𝚁𝙾𝚄𝙿 𝙲𝚁𝙴𝙰𝚃𝙾𝚁 𝚃𝙾 𝙳𝙾 𝚃𝙷𝙰𝚃.</b>"""
      
    INPUT_REQUIRED = "❗ **𝙰𝚁𝙶𝚄𝙼𝙴𝙽𝚃𝚂 𝚁𝙴𝚀𝚄𝙸𝚁𝙴𝙳**"
      
    KICKED = """✔️ 𝚂𝚄𝙲𝙲𝙴𝚂𝚂𝙵𝚄𝙻𝙻𝚈 𝙺𝙸𝙲𝙺𝙴𝙳 {} 𝙼𝙴𝙼𝙱𝙴𝚁𝚂 𝙰𝙲𝙲𝙾𝚁𝙳𝙸𝙽𝙶 𝚃𝙾 𝚃𝙷𝙴 𝙰𝚁𝙶𝚄𝙼𝙽𝙴𝚃𝚂 𝙿𝚁𝙾𝚅𝙸𝙳𝙴𝙳."""
      
    START_KICK = """🚮 𝚁𝙴𝙼𝙾𝚅𝙸𝙽𝙶 𝙸𝙽𝙰𝙲𝚃𝙸𝚅𝙴 𝙼𝙴𝙼𝙱𝙴𝚁𝚂 𝚃𝙷𝙸𝚂 𝙼𝙰𝚈 𝚃𝙰𝙺𝙴 𝙰 𝚆𝙷𝙸𝙻𝙴..."""
      
    ADMIN_REQUIRED = """❗<b>𝙸 𝚆𝙸𝙻𝙻 𝙽𝙾𝚃 𝙶𝙾 𝚃𝙷𝙴 𝙿𝙻𝙰𝙲𝙴 𝚆𝙷𝙴𝚁𝙴 𝚈𝙾𝚄 𝙳𝙸𝙳𝙽'𝚃 𝙼𝙰𝙳𝙴 𝙼𝙴 𝙰𝙳𝙼𝙸𝙽🥵..𝚂𝙾 𝙰𝙳𝙳 𝙼𝙴 𝙰𝙶𝙸𝙰𝙽 𝚆𝙸𝚃𝙷 𝙵𝚄𝙻𝙻 𝙰𝙳𝙼𝙸𝙽 𝚁𝙸𝙶𝙷𝚃𝚂..🧐</b>"""
      
    DKICK = """✔️ 𝙺𝙸𝙲𝙺𝙴𝙳 {} 𝙳𝙴𝙻𝙴𝚃𝙴𝙳 𝙰𝙲𝙲𝙾𝚄𝙽𝚃𝚂 𝚂𝚄𝙲𝙲𝙴𝚂𝚂𝙵𝚄𝙻𝙻𝚈."""
      
    FETCHING_INFO = """<b>💖 𝙻𝙴𝚃'𝚂 𝙱𝙴𝙰𝚃 𝙸𝚃 𝙰𝙻𝙻 𝙽𝙾𝚆...</b>"""
      
    STATUS = """{}\n<b>Chat Member Status</b>**\n\n```<i>Recently``` - {}\n```Within Week``` - {}\n```Within Month``` - {}\n```Long Time Ago``` - {}\nDeleted Account - {}\nBot - {}\nUnCached - {}</i>
"""
