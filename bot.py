from random import randint
import time
import discord
import mc
from dataBase.dataBaseSelectAll import dataBaseSelectAll
from dataBase.dataBaseCreate import createServer
from dataBase.dataBaseInsert import Insert

class Bot(discord.Client):
    async def on_guild_join(self, guild):
        createServer(str(guild.id))

    async def on_message(self, message):
        Insert(message.channel.name, message.content, message.guild.id)


        if int(time.clock()) % randint(5, 50) == 0:
            self.generator = mc.StringGenerator(samples=dataBaseSelectAll(message.guild.id))
            self.result = self.generator.generate_string()
            if randint(1, 3) % 2 == 0:
                await message.channel.send(self.result.upper())
            else:
                await message.channel.send(self.result)
'''                
        elif message.content.startswith('$s'):
            self.generator = mc.StringGenerator(samples=dataBaseSelectAll(message.guild.id))
            self.result = self.generator.generate_string() 
            if randint(1, 3) % 2 == 0:
                await message.channel.send(self.result.upper())
            else:
                await message.channel.send(self.result)
'''


bot = Bot()

TOKEN = open('config/TOKEN.txt', 'r')
TOKEN = TOKEN.read()

bot.run(TOKEN)
