RUN_STRINGS = (
    "**ET DAH JAMET JAMET W TANYA BIAR APA LU BEGITU HA !!!**",
    "𝗚𝗔𝗨𝗦𝗔 𝗦𝗢𝗞 𝗞𝗘𝗥𝗔𝗦 𝗟𝗢 𝗞𝗢𝗡𝗧𝗢𝗟, 𝗞𝗔𝗟𝗢 𝗗𝗜 𝗧𝗢𝗡𝗚𝗞𝗥𝗢𝗡𝗚𝗔𝗡 𝗝𝗔𝗗𝗜 𝗕𝗔𝗕𝗨 !!",
    "**LARI ADA JAMET TELE WKWKWKWKWK**",
    "**IDIH KONTOL SO KERAS AMAT SINI KELUARGA LU GUA LUDAIN CUIHKKKK !!**",
    "**KALO KOSAKATA LU CUMAN BEGITU DOANG GA BAKAL BIKIN NYALI GUA CIUT KONTOL !!**",
    "**ET DAH JAMET JAMET NGACA ITU MUKA LU KAYA KULI BEGO WKWKWKWK**",
    "**JAMET KAYA LU MAH GA PANTES IKUT WAR,LU TUH PANTES NYA JADI TALENT DESAH WKWKWWK**",
    "**IDIH SADAR DIRI LU TUH JAMET KONTOL,LU TUH GA BAKAL BISA MAKAN ENAK KALO GA NGUMPULIN PAKU DI JALANAN WKWKWKW**",
    "**LARI ADA JAMET REPLY CHAT GUA YAHAHAHAHA**",
    "**ETD DAH BADUT BIAR APASIH LU BEGITU HA !!!**",
    "**BADAN PANUAN MUKA KULI HATI HELLO KITTY HIYAAAAAA !!!**",
    "**DI KATA MANTEP KALI YA NYENGGOL NYENGGOL ALIANSI GUA , NANTI GUA SERANG BALIK LANGSUNG TUTUP GC LO KONTOL !!!**",
    "**YBG AKU MAH APSH ANAK MUTUALAN XIXI**",
    "**TYPING AJA MASIH TREMOR SOBAT MANTEP LAWAN GHA WKWKWKWKWK !!! **",
    "**LAH UDAH GITU DOANG KOSAKATA LU? KUNO KONTOL !!!**",
    "**LU TUH GA PANTES BEGO LAWAN GUA , LU TUH PANTES NYA LAWAN ANAK MUTUALAN WKWKWKWKWKWWKWK**",
    "**ADUH LUCU BAT LAWAN BADUT TELE**",
    "**TYPING MASIH COPAS GAUSH SO SO AN LAWAN GUA YANG ADA LU MALU TOLOLLLL !!! **",
    "**Sadboi Userbot by Lunglung.**",
)

SLAP_TEMPLATES = (
    "{user1} {hits} {user2} with a {item}.",
    "{user1} {hits} {user2} in the face with a {item}.",
    "{user1} {hits} {user2} around a bit with a {item}.",
    "{user1} {throws} a {item} at {user2}.",
    "{user1} grabs a {item} and {throws} it at {user2}'s face.",
    "{user1} launches a {item} in {user2}'s general direction.",
    "{user1} starts slapping {user2} silly with a {item}.",
    "{user1} pins {user2} down and repeatedly {hits} them with a {item}.",
    "{user1} grabs up a {item} and {hits} {user2} with it.",
    "{user1} ties {user2} to a chair and {throws} a {item} at them.",
    "{user1} gave a friendly push to help {user2} learn to swim in lava."
)

ITEMS = (
    "cast iron skillet",
    "large trout",
    "baseball bat",
    "cricket bat",
    "wooden cane",
    "nail",
    "printer",
    "shovel",
    "CRT monitor",
    "physics textbook",
    "toaster",
    "portrait of Richard Stallman",
    "television",
    "five ton truck",
    "roll of duct tape",
    "book",
    "laptop",
    "old television",
    "sack of rocks",
    "rainbow trout",
    "rubber chicken",
    "spiked bat",
    "fire extinguisher",
    "heavy rock",
    "chunk of dirt",
    "beehive",
    "piece of rotten meat",
    "bear",
    "ton of bricks",
)

THROW = (
    "throws",
    "flings",
    "chucks",
    "hurls",
)

HIT = (
    "hits",
    "whacks",
    "slaps",
    "smacks",
    "bashes",
)

MARKDOWN_HELP = """
Markdown is a very powerful formatting tool supported by telegram. {} has some enhancements, to make sure that \
saved messages are correctly parsed, and to allow you to create buttons.

- <code>_italic_</code>: wrapping text with '_' will produce italic text
- <code>*bold*</code>: wrapping text with '*' will produce bold text
- <code>`code`</code>: wrapping text with '`' will produce monospaced text, also known as 'code'
- <code>[sometext](someURL)</code>: this will create a link - the message will just show <code>sometext</code>, \
and tapping on it will open the page at <code>someURL</code>.
EG: <code>[test](example.com)</code>

- <code>[buttontext](buttonurl:someURL)</code>: this is a special enhancement to allow users to have telegram \
buttons in their markdown. <code>buttontext</code> will be what is displayed on the button, and <code>someurl</code> \
will be the url which is opened.
EG: <code>[This is a button](buttonurl:example.com)</code>

If you want multiple buttons on the same line, use :same, as such:
<code>[one](buttonurl://example.com)
[two](buttonurl://google.com:same)</code>
This will create two buttons on a single line, instead of one button per line.
"""

EnglishStrings = {
    "send-help": """*Main commands available*:
 - /start: start the bot
 - /help or /help <module name>: PM's you info about that module.
 - /lang: Change bot language
 - /settings:
   - in PM: will send you your settings for all supported modules.
   - in a group: will redirect you to pm, with all that chat's settings.
   {}
   """,

    "send-group-settings": """Hi there! There are quite a few settings for *{}* - go ahead and pick what
you're interested in.""",

#Misc
"RUNS-K": RUN_STRINGS,
"SLAP_TEMPLATES-K": SLAP_TEMPLATES,
"ITEMS-K": ITEMS,
"HIT-K": HIT,
"THROW-K": THROW,
"ITEMP-K": ITEMS,
"ITEMR-K": ITEMS,
"MARKDOWN_HELP-K": MARKDOWN_HELP,

#GDPR
"send-gdpr": """Your personal data has been deleted.\n\nNote that this will not unban \
you from any chats, as that is telegram data, not YanaBot data.
Flooding, warns, and gbans are also preserved, as of \
[this](https://ico.org.uk/for-organisations/guide-to-the-general-data-protection-regulation-gdpr/individual-rights/right-to-erasure/), "
which clearly states that the right to erasure does not apply \
\"for the performance of a task carried out in the public interest\", as is \
the case for the aforementioned pieces of data."""

}
