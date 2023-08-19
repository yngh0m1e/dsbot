import discord
import random
from gen import gen_pass
client = discord.Client(intents=discord.Intents.all())

game = ['Орёл', 'Решка', 'Пистолет']

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
    if message.content.startswith('!game'):
        await message.channel.send(random.choice(game))
    if message.content.startswith('!help'):
        await message.channel.send('В боте есть несколько команд, такие как !hello(это для того чтобы поздороваться с ботом), также есть команда !game(она для того чтоюы сыграть в игру "Орёл, Решка или Пистолет")) ')
client.run('MTEzNTE1NDgyNzUwNTE3MjQ5MA.GlTO7N._DS5STiX5uXNmahjg4v0...')
