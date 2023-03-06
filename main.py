####--------------------------------#### 
#--# Author: by uriid1 #--# 
#--# License: GNU GPL #--# 
#--# Telegram: @rp_party #--# 
#--# Mail: appdurov@gmail.com #--# 
####--------------------------------#### 

#################### 
## Import libs 
import sys 
import asyncio 
import time 
from telethon.sync import TelegramClient 
from telethon import TelegramClient 
from telethon import events 
# from telethon import functions, types 
# from telethon.tl.types import ChatBannedRights 
# from telethon.tl.functions.users import GetFullUserRequest 
# from telethon.tl.functions.channels import EditBannedRequest 

########################### 
## Console color print 
red = [206, 76, 54] 
green = [68, 250, 123] 
blue = [253, 127, 233] 
yellow = [241, 250, 118] 
orange = [255, 184, 107] 
def colored(color, text): 
    return "\033[38;2;{};{};{}m{}\033[38;2;255;255;255m".format(color[0], color[1], color[2], text) 

########################### 
## Settings 
api_id = int(sys.argv[1]) 
api_hash = str(sys.argv[2]) 
## Connect 
client = TelegramClient('users/current_user', api_id, api_hash) 
client.start() 

#################### 
## Account info 
#################### 
entity = client.get_entity("me") 
MY_ID = entity.id 
print( 
    "[" 
    + colored(green, "PROFILE: ") 
    + str(entity.first_name) 
    + " | " + colored(orange, "Id: ") + str(MY_ID) 
    + " | " + colored(orange, "Uname: ") + "@" + str(entity.username) 
    + "]" 
) 

######################## 
## Check script work 
## CMD: ping 
######################## 
@client.on(events.NewMessage(outgoing=True, pattern='ping')) 
async def handler(event): 
    if event.message.from_id.user_id != MY_ID: 
        return 
    
    m = await event.respond('pong') 
    await asyncio.sleep(1) 
    await client.delete_messages(event.chat_id, [event.id, m.id]) 

###################### 
## Heart Animation 
## CMD: .heart 
## ARG: text 
###################### 
heart_emoji = [ 
    "✨-💎", 
    "✨-🌺", 
    "☁️-😘", 
    "✨-🌸", 
    "🌾-🐸", 
    "🔫-💥", 
    "☁️-💟", 
    "🍀-💖", 
    "🌴-🐼", 
] 

edit_heart = ''' 
1 2 2 1 2 2 1
2 2 2 2 2 2 2 
2 2 2 2 2 2 2 
1 2 2 2 2 2 1 
1 1 2 2 2 1 1 
 1 1 1 2 1 1
''' 

@client.on(events.NewMessage(pattern=".heart+")) 
async def handler(event): 
    if event.message.from_id.user_id != MY_ID: 
        return 
        
    try: 
        text = 
        event.message.message.replace(".heart ", "") 
        if text == ".heart": 
        text = "Хочешь так же? Подпишись @S0XSU" 
        
        message = event.message 
        chat = event.chat_id 
        
        while(true):
        
        # play anim 
        frame_index = 0 
        while(frame_index != len(heart_emoji)): 
            await client.edit_message(chat, message, edit_heart.replace("1", heart_emoji[frame_index].split("-")[0]) .replace("2", heart_emoji[frame_index].split("-")[1])) 
                
                await asyncio.sleep(1) 
                frame_index = frame_index + 1 
            
            await client.edit_message(chat, message, text) 
                except: 
                    print( "[" + colored(red, "Error") + "] " + "Не удалось выполнить команду [.heart] Возможно вы словили flood." ) 
            
## RUN 
client.run_until_disconnected()