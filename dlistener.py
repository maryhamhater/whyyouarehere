#secret = jFuuSAUE3N7i7WF_fLr1s4cPZNZ90U6W
#permission = 67648
#client = 583319453253500968
#token = NTgzMzE5NDUzMjUzNTAwOTY4.XO6sdQ.QfG4-Z5wcKECtCNyzjdM7gcmntI
#https://discordapp.com/oauth2/authorize?client_id=583319453253500968&scope=bot&permissions=67648

import discord


token = "NTgzMzE5NDUzMjUzNTAwOTY4.XO6sdQ.QfG4-Z5wcKECtCNyzjdM7gcmntI"  


client = discord.Client()  # starts the discord client.



@client.event  
async def on_ready():  
    print(f'logged in as {client.user}') 

 
@client.event
async def on_message(message):
    print("-------------------------------------------------------------------------------------------------------------------------------------------")
    print(f"{message.channel}: {message.author}: {message.content} ")
    print("-------------------------------------------------------------------------------------------------------------------------------------------")

client.run(token)
 










