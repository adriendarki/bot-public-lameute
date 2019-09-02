import discord
from discord.ext import commands


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def help(self, ctx):
        # retour en privée l'integralité des commandes disponible pour le bot
        embed = discord.Embed(
            colour=discord.Colour.red()
        )
        embed.set_author(name='les commandes discord !')
        embed.add_field(name='!loup', value='description du bot')
        embed.add_field(name='!8loup', value='devinette')
        embed.add_field(name='!ping', value='ping le bot')
        embed.add_field(name='!bitcoin', value='bitcoin en dollar')
        embed.add_field(name='!coinflip', value='fait tourner une piece')
        embed.add_field(name='!rank', value='donne sont niveau')
        embed.set_footer(text='Loup MJ')
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Help(bot))
