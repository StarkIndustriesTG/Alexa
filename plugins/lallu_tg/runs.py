import random
from pyrogram import Client, filters
from info import COMMAND_HAND_LER
from plugins.helper_functions.cust_p_filters import f_onw_fliter


RUN_STRINGS = (
    
"Oh .. arrogance ... just like that .... no change ..... nothing goes wrong .... !!!",
 "Allah ... every child ... passion ...",
 "I do not know how to read, sir. I do not know how to read. Understand, there is no heaven, no hell, 'single life', everyone decides where and how to do it",
"What a bombastic explosion! Such a terrific disclosure !! " The Today ... Do not go down ..",
"I can do that ‌ Do I can do that ",
"Tiger biscuits do not have to have tigers because there is cream in the cream biscuits."
"My lord ... you do not allow me to be good. Did your father make porridge and chicken? Waste of toddy and wet rain ....",
"Where have you been for so long ....!",
"I do not know English at all ....",
"All the Dreams Like Twinkle Stars ...",
"My Periphery Muthappa give him a way",
"Will you pay the dowry tied to your sister Alia",
"You're so tired "," You're waiting with tears in your eyes",
"Chellakandu ennu pota tadi.ya. . \ Patto to die with you patto.",

)

@Client.on_message(
    filters.command("runs", COMMAND_HAND_LER) &
    f_onw_fliter
)
async def runs(_, message):
    """ /runs strings """
    effective_string = random.choice(RUN_STRINGS)
    if message.reply_to_message:
        await message.reply_to_message.reply_text(effective_string)
    else:
        await message.reply_text(effective_string)
