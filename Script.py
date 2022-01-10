class script(object):
    START_TXT = """𝙷𝙴𝙻𝙾 {},
𝙼𝚈 𝙽𝙰𝙼𝙴 𝙸𝚂 <a href=https://t.me/{}>{}</a>, 𝙸 𝙲𝙰𝙽 𝙿𝚁𝙾𝚅𝙸𝙳𝙴 𝙼𝙾𝚅𝙸𝙴𝚂, 𝙹𝚄𝚂𝚃 𝙰𝙳𝙳 𝙼𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 𝙰𝙽𝙳 𝙴𝙽𝙹𝙾𝚈 😍"""
    HELP_TXT = """𝙷𝙴𝚈 {}
𝙷𝙴𝚁𝙴 𝙸𝚂 𝚃𝙷𝙴 𝙷𝙴𝙻𝙿 𝙵𝙾𝚁 𝙼𝚈 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂."""
    ABOUT_TXT = """🔥 𝙼𝚈 𝙽𝙰𝙼𝙴: {}
🔥𝙲𝚁𝙴𝙰𝚃𝙾𝚁: <a href=https://t.me/mksupport1>ᎷᏦ ՏႮᏢᏢϴᎡͲ</a>
🔥 𝙻𝙸𝙱𝚁𝙰𝚁𝚈: 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼
🔥 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴: ᏢᎡᏆᏙᎪͲᎬ
🔥𝙳𝙰𝚃𝙰 𝙱𝙰𝚂𝙴: ᏢᎡᏆᏙᎪͲᎬ
🔥 𝙱𝙾𝚃 𝚂𝙴𝚁𝚅𝙴𝚁: ᏢᎡᏆᏙᎪͲᎬ
🔥 𝙱𝚄𝙸𝙻𝙳 𝚂𝚃𝙰𝚃𝚄𝚂: v6.0.1 [ 𝙱𝙴𝚃𝙰 ]"""
    SOURCE_TXT = """<b>NOTE:</b>
-  ᎷᏦ ᏆՏ Ꭺ ϴᏢᎬΝ ՏϴႮᎡᏟᎬ ᏢᎡϴᎫᎬᏟͲ.
  

<b>DEVS:</b>
- <a href=https://t.me/mksupport1>ᎷᏦ 🔥</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- ҒᏆᏞͲᎬᎡ ᏆՏ ͲᎻᎬ ҒᎬᎪͲႮᎡᎬ ᏔᎬᎡᎬ ႮՏᎬᎡՏ ᏟᎪΝ ՏᎬͲ ᎪႮͲϴᎷᎪͲᎬᎠ ᎡᎬᏢᏞᏆᎬՏ ҒϴᎡ Ꭺ ᏢᎪᎡͲᏆᏟႮᏞᎪᎡ ᏦᎬᎽᏔϴᎡᎠ ᎪΝᎠ ᎷᏦ 🔥 ᏔᏆᏞᏞ ᎡᎬՏᏢϴΝᎠ ᏔᎻᎬΝᎬᏙᎬᎡ Ꭺ ᏦᎬᎽᏔϴᎡᎠ ᏆՏ ҒϴႮΝᎠ ͲᎻᎬ ᎷᎬՏՏᎪᏀᎬ


<b>NOTE:</b>
1. ᎷᏦ ՏᎻϴႮᏞᎠ ᎻᎪᏙᎬ ᎪᎠᎷᏆΝ ᏢᎡᏆᏙᏆᏞᏞᎪᏀᎬ.
2. ϴΝᏞᎽ ᎪᎠᎷᏆΝՏ ᏟᎪΝ ᎪᎠᎠ ҒᏆᏞͲᎬᎡՏ ᏆΝ Ꭺ ᏟᎻᎪͲ.
3. ᎪᏞᎬᎡͲ ᏴႮͲͲϴΝՏ ᎻᎪᏙᎬ Ꭺ ᏞᏆᎷᏆͲ ϴҒ 64 ᏟᎻᎪᎡᎪᏟͲᎬᎡՏ.


<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

-ᎷᏦ ՏႮᏢᏢϴᎡͲՏ ᏴϴͲᎻ ႮᎡᏞ ᎪΝᎠ ᎪᏞᎬᎡͲ ᏆΝᏞᏆΝᎬ ᏴႮͲͲϴΝՏ.


<b>NOTE:</b>
1. ͲᎬᏞᎬᏀᎡᎪᎷ ᏔᏆᏞᏞ ΝϴͲ ᎪᏞᏞϴᏔՏ ᎽϴႮ Ͳϴ ՏᎬΝᎠ ᏴႮͲͲϴΝՏ ᏔᏆͲᎻϴႮͲ ᎪΝᎽ ᏟϴΝͲᎬΝͲ, Տϴ ᏟϴΝͲᎬΝͲ ᏆՏ ᎷᎪΝᎠᎪͲϴᎡᎽ.
2.  ᎷᏦ ՏႮᏢᏢϴᎡͲՏ ᏴႮͲͲϴΝՏ ᏔᏆͲᎻ ᎪΝᎽ ͲᎬᏞᎬᏀᎡᎪᎷ ᎷᎬᎠᏆᎪ ͲᎽᏢᎬ.
3. ᏴႮͲͲϴΝՏ ՏᎻϴႮᏞᎠ ᏴᎬ ᏢᎡϴᏢᎬᎡᏞᎽ ᏢᎪᎡՏᎬᎠ ᎪՏ ᎷᎪᎡᏦᎠϴᏔΝ ҒϴᎡᎷᎪͲ.


<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/mksupport1)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. ᎷᎪᏦᎬ ᎷᎬ ͲᎻᎬ ᎪᎠᎷᏆΝ ϴҒ ᎽϴႮᎡ ᏟᎻᎪΝΝᎬᏞ ᏆҒ ᏆͲ'Տ ᏢᎡᏆᏙᎪͲᎬ.
2. ᎷᎪᏦᎬ ՏႮᎡᎬ ͲᎻᎪͲ ᎽϴႮᎡ ᏟᎻᎪΝΝᎬᏞ ᎠϴᎬՏ ΝϴͲ ᏟϴΝͲᎪᏆΝՏ ᏟᎪᎷᎡᏆᏢՏ, ᏢϴᎡΝ ᎪΝᎠ ҒᎪᏦᎬ ҒᏆᏞᎬՏ.
3. ҒϴᎡᏔᎪᎡᎠ ͲᎻᎬ ᏞᎪՏͲ ᎷᎬՏՏᎪᏀᎬ Ͳϴ ᎷᎬ ᏔᏆͲᎻ ϘႮϴͲᎬՏ.
 Ꮖ'ᏞᏞ ᎪᎠᎠ ᎪᏞᏞ ͲᎻᎬ ҒᏆᏞᎬՏ ᏆΝ ͲᎻᎪͲ ᏟᎻᎪΝΝᎬᏞ Ͳϴ ᎷᎽ ᎠᏴ."""
    CONNECTION_TXT = """Help: <b>Connections</b>

-ႮՏᎬᎠ Ͳϴ ᏟϴΝΝᎬᏟͲ ᏴϴͲ Ͳϴ ᏢᎷ ҒϴᎡ ᎷᎪΝᎪᏀᏆΝᏀ ҒᏆᏞͲᎬᎡՏ 
- ᏆͲ ᎻᎬᏞᏢՏ Ͳϴ ᎪᏙϴᏆᎠ ՏᏢᎪᎷᎷᏆΝᏀ ᏆΝ ᏀᎡϴႮᏢՏ.

<b>NOTE:</b>
1. ϴΝᏞᎽ ᎷᏦ ᏟᎪΝ ᎪᎠᎠ Ꭺ ᏟϴΝΝᎬᏟͲᏆϴΝ.
2. ՏᎬΝᎠ<code>/connect</code> ҒϴᎡ ᏟϴΝΝᎬᏟͲᏆΝᏀ ᎷᎬ Ͳϴ ႮᎡ ᏢᎷ

<b>Commands and Usage:</b>
• /connect  - <code>ᏟϴΝΝᎬᏟͲ Ꭺ ᏢᎪᎡͲᏆᏟႮᏞᎪᎡ ᏟᎻᎪͲ Ͳϴ ᎽϴႮᎡ ᏢᎷ</code>
• /disconnect  - <code>ᎠᏆՏᏟϴΝΝᎬᏟͲ ҒᎡϴᎷ Ꭺ ᏟᎻᎪͲ</code>
• /connections - <code>ᏞᏆՏͲ ᎪᏞᏞ ᎽϴႮᎡ ᏟϴΝΝᎬᏟͲᏆϴΝՏ</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
ͲᎻᎬՏᎬ ᎪᎡᎬ ͲᎻᎬ ᎬХͲᎡᎪ ҒᎬᎪͲႮᎡᎬՏ ϴҒ ᎷᏦ ՏႮᏢᏢϴᎡͲ 🔥


<b>Commands and Usage:</b>
• /id - <code>ᏀᎬͲ ᏆᎠ ϴҒ Ꭺ ՏᏢᎬᏟᏆҒᏆᎬᎠ  ႮՏᎬᎡ.</code>
• /info  - <code>ᏀᎬͲ ᏆΝҒϴᎡᎷᎪͲᏆϴΝ ᎪᏴϴႮͲ Ꭺ ႮՏᎬᎡ.</code>
• /imdb  - <code>ᏀᎬͲ ͲᎻᎬ ҒᏆᏞᎷ ᏆΝҒϴᎡᎷᎪͲᏆϴΝ ҒᎡϴᎷ ᏆᎷᎠᏴ ՏϴႮᎡᏟᎬ.</code>
• /search  - <code>ᏀᎬͲ ͲᎻᎬ ҒᏆᏞᎷ ᏆΝҒϴᎡᎷᎪͲᏆϴΝ ҒᎡϴᎷ ᏙᎪᎡᏆϴႮՏ ՏϴႮᎡᏟᎬՏ.</code>"""
    ADMIN_TXT = """Help: <b>MK mods</b>

<b>NOTE:</b>
ͲᎻᏆՏ ᎷϴᎠႮᏞᎬ ϴΝᏞᎽ ᏔϴᎡᏦՏ ҒϴᎡ ᎷᎽ ᎷᏦ🔥

<b>Commands and Usage:</b>
• /logs - <code>Ͳϴ ᏀᎬͲ ͲᎻᎬ ᎡᎬՏᏟᎬΝͲ ᎬᎡᎡϴᎡՏ.</code>
• /stats - <code>Ͳϴ ᏀᎬͲ ՏͲᎪͲႮՏ ϴҒ ҒᏆᏞᎬՏ ᏆΝ ᎠᏴ.</code>
• /delete - <code>Ͳϴ ᎠᎬᏞᎬͲᎬ Ꭺ ՏᏢᎬᏟᏆҒᏆᏟ ҒᏆᏞᎬ ҒᎡϴᎷ ᎠᏴ</code>
• /users - <code>Ͳϴ ᏀᎬͲ ᏞᏆՏͲ ϴҒ ᎷᎽ ႮՏᎬᎡՏ ᎪΝᎠ ᏆᎠՏ.</code>
• /chats - <code>Ͳϴ ᏀᎬͲ ᏞᏆՏͲ ϴҒ ͲᎻᎬ ᎷᎽ ᏟᎻᎪͲՏ ᎪΝᎠ ᏆᎠՏ.</code>
• /leave  - <code>Ͳϴ ᏞᎬᎪᏙᎬ ҒᎡϴᎷ Ꭺ ᏟᎻᎪͲ.</code>
• /disable  -  <code>Ꭰϴ ᎠᏆՏᎪᏴᏞᎬ Ꭺ ᏟᎻᎪͲ.</code>
• /ban  - <code>Ͳϴ ᏴᎪΝ Ꭺ ႮՏᎬᎡ.</code>
• /unban  - <code>Ͳϴ ႮΝᏴᎪΝ Ꭺ ႮՏᎬᎡ.</code>
• /channel - <code>Ͳϴ ᏀᎬͲ ᏞᏆՏͲ ϴҒ ͲϴͲᎪᏞ ᏟϴΝΝᎬᏟͲᎬᎠ ᏟᎻᎪΝΝᎬᏞՏ</code>
• /broadcast - <code>Ͳϴ ᏴᎡϴᎪᎠᏟᎪՏͲ Ꭺ ᎷᎬՏՏᎪᏀᎬ Ͳϴ ᎪᏞᏞ ႮՏᎬᎡՏ</code>"""
    STATUS_TXT = """😻𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
😻 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
😻 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
😻 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
😻 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""

⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠____",
            "------------------>",    
            "------>;(^。^)ノ",
            "(￣ー￣) DED",
            "**Target killed successfully"
]




love_siren = [
            "❤️❤️❤️🧡🧡🧡💚💚💚\n💙💙💙💜💜💜🖤🖤🖤",
            "🖤🖤🖤💜💜💜💙💙💙\n❤️❤️❤️🧡🧡🧡💚💚💚",
            "💛💛💛💙💙💙❤️❤️❤️\n💜💜💜❤️❤️❤️🧡🧡🧡",
            "❤️❤️❤️🧡🧡🧡💚💚💚\n💙💙💙💜💜💜🖤🖤🖤",
            "🖤🖤🖤💜💜💜💙💙💙\n❤️❤️❤️🧡🧡🧡💚💚💚",
            "💛💛💛💙💙💙❤️❤️❤️\n💜💜💜❤️❤️❤️🧡🧡🧡",
            "❤️❤️❤️🧡🧡🧡💚💚💚\n💙💙💙💜💜💜🖤🖤🖤",
            "🖤🖤🖤💜💜💜💙💙💙\n❤️❤️❤️🧡🧡🧡💚💚💚",
            "💛💛💛💙💙💙❤️❤️❤️\n💜💜💜❤️❤️❤️🧡🧡🧡"
]

hack_you = [
            "Looking for TG databases in targeted person...",
            " User online: True\nTelegram access: True\nRead Storage: True ",
            "Hacking... 20.63%\n[███░░░░░░░░░░░░░░░░░]",    
            "Hacking... 86.21%\n[███████████████░░░░░]",
            "Hacking... 93.50%\n[█████████████████░░░]",
            "hacking....  100%\n[████████████████████]",
]




bomb_ettu = [
             "▪️▪️▪️▪️\n▪️▪️▪️▪️\n▪️▪️▪️▪️\n▪️▪️▪️▪️\n▪️▪️▪️▪️",
             "💣💣💣💣\n▪️▪️▪️▪️\n▪️▪️▪️▪️\n▪️▪️▪️▪️\n▪️▪️▪️▪️", 
             "▪️▪️▪️▪️\n💣💣💣💣\n▪️▪️▪️▪️\n▪️▪️▪️▪️\n▪️▪️▪️▪️",
             "▪️▪️▪️▪️\n▪️▪️▪️▪️\n💣💣💣💣\n▪️▪️▪️▪️\n▪️▪️▪️▪️",
             "▪️▪️▪️▪️\n▪️▪️▪️▪️\n▪️▪️▪️▪️\n💣💣💣💣\n▪️▪️▪️▪️",
             "▪️▪️▪️▪️\n▪️▪️▪️▪️\n▪️▪️▪️▪️\n▪️▪️▪️▪️\n💣💣💣💣",
             "▪️▪️▪️▪️\n▪️▪️▪️▪️\n▪️▪️▪️▪️\n▪️▪️▪️▪️\n💥💥💥💥",
             "▪️▪️▪️▪️\n▪️▪️▪️▪️\n▪️▪️▪️▪️\n💥💥💥💥\n💥💥💥💥",
             "▪️▪️▪️▪️\n▪️▪️▪️▪️\n▪️▪️▪️▪️\n▪️▪️▪️▪️\n😵😵😵😵",
]




@user_admin
@run_async
def bombs(update: Update, context: CallbackContext):
    bot,args = context.bot, context.args
    msg = update.effective_message.reply_text('💣') 
    for x in range(EDIT_TIMES):
        msg.edit_text(bomb_ettu[x%9])
        time.sleep(EDIT_SLEEP)
    msg.edit_text('RIP PLOX...')



@user_admin
@run_async
def hack(update: Update, context: CallbackContext):
    bot, args = context.bot, context.args
    msg = update.effective_message.reply_text('Target selected') 
    for x in range(EDIT_TIMES):
        msg.edit_text(hack_you[x%5])
        time.sleep(EDIT_SLEEP)
    msg.edit_text('successful hacked all data send on my Database')





@user_admin
@run_async
def love(update: Update, context: CallbackContext):
    bot, args = context.bot, context.args
    msg = update.effective_message.reply_text('❣️') 
    for x in range(EDIT_TIMES):
        msg.edit_text(love_siren[x%5])
        time.sleep(EDIT_SLEEP)
    msg.edit_text('True Love💞')




@user_admin
@run_async
def kill(update: Update, context: CallbackContext):
    bot, args = context.bot, context.args
    msg = update.effective_message.reply_text('🔫') 
    for x in range(EDIT_TIMES):
        msg.edit_text(kill_you[x%12])
        time.sleep(EDIT_SLEEP)
    msg.edit_text('⚰')




help = """
╔ /love*:* 
╠ /hack*:*
╠ /bombs*:*
╚ /kill*:*
"""

mod_name = "Animation"


KILL_HANDLER = DisableAbleCommandHandler("kill",kill)
LOVE_HANDLER = DisableAbleCommandHandler("love", love)
HACK_HANDLER = DisableAbleCommandHandler("hack", hack)
BOMBS_HANDLER = DisableAbleCommandHandler("bombs",bombs)
dispatcher.add_handler(KILL_HANDLER)
dispatcher.add_handler(LOVE_HANDLER)
dispatcher.add_handler(HACK_HANDLER)
dispatcher.add_handler(BOMBS_HANDLER)

command_list = ["love", "hack", "bombs", "kill"]

command_list = ["love", "hack", "bombs","kill"]
    
handlers = [LOVE_HANDLER, HACK_HANDLER, BOMBS_HANDLER, KILL_HANDLER

    
