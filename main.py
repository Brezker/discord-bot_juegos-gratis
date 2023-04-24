import discord

# Define las intenciones necesarias para tu bot
intents = discord.Intents.default()
intents.members = True

# Crea una instancia de Client con las intenciones definidas
client = discord.Client(intents=intents)

# Define la función on_ready para que se ejecute cuando el bot se conecte
@client.event
async def on_ready():
    print('¡Bot conectado!')
    canal_bot = client.get_channel(1100146594801795163)
    await canal_bot.send('¡Hola a todos!, soy un bot.')

# Define la función on_message para que se ejecute cuando llega un mensaje
@client.event
async def on_message(message):
    # Verifica que el mensaje no proviene del bot para evitar un bucle infinito
    if message.author == client.user:
        return

    # Verifica si el mensaje contiene el comando '!hola'
    if message.content.startswith('!hola'):
        # Responde al mensaje con un saludo
        await message.channel.send('¡Hola, {}!'.format(message.author.name))
        print('Hola soy bot')

# Ejecuta el bot con el token correspondiente
client.run('MTEwMDEzNjk2NzQ2OTAyNzM5MA.Gst7Xd.pRyzNbxhpmLrKbeaPgg_TeoDavbjMqhzMyO9HQ')

