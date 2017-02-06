import discord
import asyncio
import os

# LogBot made by Zock629
# Help provided by wubbalubbadubdub
# Bot last updated 03/02/2017


client = discord.Client()                                       # This is the bot


index = ''
with open("server.txt", "r") as file:
		for line in file:
			mydic = {}											#creates an empty dictionary
			mydic[line] = ''
			if line in mydic:
				while os.path.exists(line+" "+'log'+" "+index+'.txt'):
					mydic[line] += '1'

@client.event
async def on_message(message):                                  # Do this with the message when you get a message
	with open("server.txt", "r") as file:
		for line in file: 
			ServerName = line
			ServerName = ServerName.replace(" ", "")
			ServerName = ServerName.lower()
			SName = message.server.name
			SName = SName.replace(" ", "")
			SName = SName.lower()
			
			if line in mydic:
				log = " "+'log'+mydic[line]+'.txt'
			
			if SName == ServerName:
				Server = message.server.name
				print("{} in {} : {} : {}".format(          # Print the message to terminal
				message.author.name,
				message.server.name, 
				message.channel.name, 
				message.content
				))
				
				os.chdir("Logs")
				
				with open(Server+log, 'a') as file:
					file.write("{} in {} : {}\n".format(
					message.author.name,
					message.channel.name, 
					message.content
					))
					
					os.chdir("../")

with open("token.txt", "r") as file:
	token = file.read().strip()                                 # Read in the token from file
	

client.run(token, bot=False)                                    # Run the bot