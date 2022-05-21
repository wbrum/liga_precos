import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

print(TOKEN)

# Define prefixos

magic_prefix = '-magic'

pkmn_prefix = '-pkmn'

ygo_prefix = '-ygo'


def define_prefix(prefix):
    match prefix:
        case magic_prefix:
            return 'https://www.ligamagic.com.br/?view=cards%2Fcard&card='
        case pkmn_prefix:
            return 'https://www.ligapokemon.com.br/?view=cards/card&card='
        case ygo_prefix:
            return 'https://www.ligayugioh.com.br/?view=cards/card&card='
        case _:
            return 'Comando inválido'


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    url_beginning = ''
    card_name = ''
    url_ending = '&tipo=1'

    if message.author == client.user or (
        not message.content.startswith(magic_prefix)
            and not message.content.startswith(pkmn_prefix)
            and not message.content.startswith(ygo_prefix)):
        return

    args = message.content.strip().split(' ')
    command = args.pop(0)

    print(args)
    print(command)

    url_beginning = define_prefix(command)

    if args.__len__() == 0:
        await message.channel.send(
            f'Você não enviou o nome da carta, {message.author}!')

    else:
        for val in args:
            print(val)
            card_name = card_name + val + '+'

    # Replace em caracteres especiais

    card_name = card_name.replace('/', '%2F')  # Ex: Ready // Willing
    card_name = card_name.replace(',', '%2C')  # Ex: Narset, Parter of Veils

    url_final = url_beginning + card_name[:-1] + url_ending
    await message.channel.send(url_final)


client.run(TOKEN)
