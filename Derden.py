import discord
import random
from gen import gen_pass
client = discord.Client(intents=discord.Intents.all())

game = ['Орёл', 'Решка']

@client.event
async def on_ready(): #функция, отражающая готовность бота к работе
    print(f'Вы зареганы {client.user}')
    print('Ваш пароль для входа', gen_pass(10))

@client.event
async def on_message(message): #Направлена на общение с пользователем
    if message.author == client.user:
        return
    if message.content.startswith('!hello'):
        await message.channel.send('hi!')
    if message.author == client.user:
        return
    if message.content.startswith('!Game'):
        await message.channel.send(random.choice(game))

client.run('#token')
