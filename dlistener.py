

import discord


token = "your token here"  


client = discord.Client()  # starts the discord client.



@client.event  
async def on_ready():  
    print(f' {client.user} is the name of your bot') #it just says the name of the bot

 
@client.event
async def on_message(message): # when a message is sent to your server this shitty snippet of code will give it to you as output
    print("-------------------------------------------------------------------------------------------------------------------------------------------")
    print(f"{message.channel}: {message.author}: {message.content} ")
    print("-------------------------------------------------------------------------------------------------------------------------------------------")

client.run(token)
 










