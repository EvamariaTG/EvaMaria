from pyrogram import Client, filters
 
EMOJI = "🎯" #use the emoji which supports animation
 
 
@Client.on_message(
    filters.command(["roll", "throw"]))
async def roll_dice(client, message):
    rep_mesg_id = message.message_id
    if message.reply_to_message:
        rep_mesg_id = message.reply_to_message.message_id
    await client.send_dice(
        chat_id=message.chat.id,
        emoji=EMOJI,
        disable_notification=True,
        reply_to_message_id=rep_mesg_id
    )
