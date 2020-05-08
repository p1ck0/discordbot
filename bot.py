from random import randint
import discord
import json
from discord.ext import commands
import time
import mc


class Bot(discord.Client):

    count = 0
    message_list = set()

    
    old_msgs = open('msg.txt', 'r', encoding='UTF=8')
    for msg in old_msgs:
        message_list.add(msg)
    
    old_msgs.close()
    

    async def on_message(self, message):
        self.count += 1
        self.message_list.add(message.content)
        print('сообщений получено',self.count)
        print('кол-во данных',len(self.message_list))
        
        
        if self.count % randint(5,50) == 0:
            self.generator = mc.StringGenerator(samples=self.message_list)
            self.result = self.generator.generate_string()
            print(self.result)
            if randint(1,3) % 2 == 0:
                await message.channel.send(self.result.upper())
            else:
                await message.channel.send(self.result)
        
        elif message.content.startswith('$s'):
            self.message_list.remove('$s')
            self.generator = mc.StringGenerator(samples=self.message_list)
            self.result = self.generator.generate_string()
            print(self.result)
            if randint(1,3) % 2 == 0:
                await message.channel.send(self.result.upper())
            else:
                await message.channel.send(self.result)
        
        if len(self.message_list) % 50 == 0:
            self.save = open('msg.txt', 'w', encoding='UTF=8')
            for msg in self.message_list:
                self.save.write(msg + '\n')
            self.save.close()
            print('засейвил')
             
    
bot = Bot()

token = open('token.txt', 'r')
token = token.read()

bot.run(token)