 from pyrogram import Client, filters
 
 EMOJI = "🎲" #use the emoji which supports animation
 
 
 @Client.on_message(filters.command("roll", "dice")) #change the command according to your emoji name
 async def roll_dice(bot, message):
     rep_msg_id = message.message.id
     if message.reply_to_message:
         rep_msg_id = message.reply_to_message.message.id
     await bot.send_dice(
     chat.id=message.chat.id,
     emoji=EMOJI,
     disable_web_page_preview=True,
     reply_to_message_id=rep_msg_id
     )
