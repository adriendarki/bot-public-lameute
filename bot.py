### CONF ####

import asyncio
import json
import discord
from discord.ext import commands


chan_dev = discord.Object(id="533699221073952768")

with open("token.json", "r") as conffile:
    config = json.load(conffile)

bot = commands.Bot(command_prefix="!",
                   description="description du bot voici les differentes commandes utilisables a l'heure actuelle ")
bot.remove_command('help')

# this specifies what extensions to load when the bot starts up
startup_extensions = ["fonctions.message", "fonctions.clear", "fonctions.help", "fonctions.8loup",
                      "fonctions.cryptomonnaie",
                      "fonctions.lapiece", "fonctions.math", "fonctions.sondage", "fonctions.experience", "fonctions.music",

                      ]


async def my_background_task(self):
    await self.wait_until_ready()
    counter = 0
    channel = self.get_channel(533707060743766039)  # channel ID goes here
    while not self.is_closed():
        counter += 1
        await channel.send(counter)
        await asyncio.sleep(60)  # task runs every 60 seconds


@bot.event
async def on_ready():
    # information de lancement du bot + activité en cours
    print('en ligne en tant que')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    activity = discord.Game(name="attaquer des poules")
    await bot.change_presence(status=discord.Status.online, activity=activity)


@bot.event
async def on_member_join(member):
    # envoie un message dans le channel d'apparition plus définie le role "Louveteau"
    bonjour = """ bienvenue dans la meute {0} !
        fais un petit tour dans #l-assemblée-des-loups pour avoir un max d'information sur l'antre des loups !
        """.format(member.mention)
    channel = bot.get_channel(533699221073952768)
    await channel.send(bonjour)
    role = discord.utils.get(member.guild.roles, name='Louveteau')
    await member.add_roles(role)


if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))
bot.run(config["token"])
