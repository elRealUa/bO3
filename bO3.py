import discord
from discord.ext import commands
import os
import random
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)
TOKEN = ""

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy {bot.user}!, aqui tienes mi lista de comandos:')
    await ctx.send(f'$alt')
    await ctx.send(f'$fact')

@bot.command()
async def fact(ctx):
    choices = ["Muchos productos de limpieza contienen sustancias químicas nocivas para el medio ambiente que pueden contaminar el agua y el suelo cuando se desechan.",
               "Solo el 21 porciento de el oxígeno en la atmósfera puede usarse para la respiración humana.",
               "La contaminación acústica, es el exceso de sonido que perturba el entorno natural y puede causar molestias o daños a la salud humana y animal.",
               "Los chicles pueden contaminar el medio ambiente si no se desechan adecuadamente. La goma base del chicle no es biodegradable, lo que significa que puede permanecer en el medio ambiente durante mucho tiempo después de ser desechada.",
               "La contaminación de pilas es muy perjudicial, ya que hacen que gaste más nuestra biodiversidad"
    ]
    choose = random.choice(choices)
    await ctx.send(choose)

@bot.command()
async def alt(ctx):
    choices = ["Reutilizar bolsas de plástico y dejar de usar plástico desechable.",
               "Evitar la quema de basura y llantas.",
               "Usar medios de transporte que no requieran de algun tipo de combustible perjudicial para el ambiente.",
               "Las botellas de plástico pueden ser reutilizadas de muchas maneras, una de ellas puede ser como macetas (al dividirlas por la mitad)."
    ]
    choose = random.choice(choices)
    await ctx.send(choose)
bot.run(TOKEN)
