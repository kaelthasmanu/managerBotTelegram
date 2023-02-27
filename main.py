import logging
from pyrogram import Client, filters, emoji
import vars

logging.basicConfig(filename='bot.log',level = logging.INFO , format="%(asctime)s - %(name)s - %(levelname)s - %(message)s,")
logger = logging.getLogger()

app = Client(
    "my_bot",
    api_id=vars.api_id, api_hash=vars.api_hash,
    bot_token=vars.bot_token
)

@app.on_message(filters.command("start"))
async def botWelcome(client, message):
    chat_id = message.chat.id
    user_username = message.from_user.username
    user_id = message.from_user.id
    vars.users_new.append(user_id)
    await app.send_message(chat_id, "Bienvenido a este bot de prueba")


@app.on_message(filters.chat(vars.target_chats) & filters.new_chat_members)
async def welcome(client, message):
    user_username = message.from_user.username
    user_id = message.from_user.id
    print("Welcome new members")
    new_members = [u.mention for u in message.new_chat_members]
    # Build the welcome message by using an emoji and the list we built above
    text = vars.message_Welcome.format(emoji.SPARKLES, ", ".join(new_members))
    # Send the welcome message, without the web page preview
    await message.reply_text(text, disable_web_page_preview=True)

@app.on_message((filters.chat(vars.target_chats) | filters.private) & filters.command("ban"))
async def banUser(client, message):
    chat_id = message.chat.id
    userToBan = message.text.split()  
    if len(userToBan) == 2:
        print(userToBan[1])
        for i in vars.target_chats:
            await app.ban_chat_member(i, userToBan[1])
    else:
        await app.send_message(chat_id , "Error!")

@app.on_message((filters.chat(vars.target_chats) | filters.private) & filters.command("delban"))
async def delBan(client, message):
    chat_id = message.chat.id
    userToUnban = message.text.split()
    if len(userToUnban) == 2:
        for i in vars.target_chats:
            await app.unban_chat_member(i, userToUnban[1])
    else:
        await app.send_message(chat_id , "Error!")

app.on_message((filters.chat(vars.target_chats) | filters.private) & filters.command("add"))
async def addUser(client,message):
    print("Hello World")
    userToAdd = message.text.split()


app.run()
