import time
from random import choice

import discord
from discord.ext import commands


class Message(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def loup(self, ctx):
        # command de définition du bot
        embed = discord.Embed(
            title='LOUP MJ',
            description='yo les petits loups je suis Loup MJ, recommander  par <@226679530063003658> (le chef de la meute si ta pas compris) ',

            color=discord.Colour.dark_blue()
        )
        embed.set_footer(text='Loup MJ')
        await ctx.send(embed=embed)

    @commands.command(name='ping')
    async def ping(self, ctx):
        # command de ping permet de savoir le ping du bot
        pingtime = time.time()
        ping = time.time() - pingtime
        await ctx.send(":ping_pong: temps de réponse de `%.01f seconds`" % ping)

    @commands.command()
    async def bonjour(self, ctx):
        # command qui dit bonjour
        await ctx.send("bonjour gamin ")

    @commands.command()
    async def tank(self, ctx):
        # invoque un tank sur le terrain lessivor monte dedans et tu connais la suite
        image = 'https://media.giphy.com/media/2a5IGQ1n1Ap1e/giphy.gif'
        embed = discord.Embed(
            title='LOUP MJ',
            description=' attention <@284671200779698186> déboule en tank est te roule dessus. ',
            color=discord.Colour.dark_blue()
        )
        embed.set_image(url=image)
        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def name(self, ctx):
        # command retour le nom de utilisateur avec mention
        await  ctx.send("{} c'est bien ton nom ?".format(ctx.message.author.mention))

    @commands.command(name='love')
    async def love(self, ctx):
        image = 'https://media.giphy.com/media/NkpL5z9KMqPx6/giphy.gif'
        author = ctx.message.author.name
        messages = [f'{author} vous envoie DU LOVE  <3']

        embed = discord.Embed(color=0xFF6AE5,
                              title=choice(messages))
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)

        embed.set_image(url=image)
        await ctx.send(embed=embed)

    @commands.command(name='wolf')
    async def wolf(self, ctx):
        image = 'https://giphy.com/search/wolf'
        author = ctx.message.author.name
        messages = [f'{author}']

        embed = discord.Embed(color=0xFF6AE5,
                              title=choice(messages))
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)

        embed.set_image(url=image)
        await ctx.send(embed=embed)

    @commands.command(name='reverse')
    async def reverse(self, ctx, *args):
        to_reverse = " ".join(args) if len(args) > 0 else ctx.message.content
        await ctx.message.channel.send(to_reverse[::-1])

    @commands.command(name='dit')
    async def dit(self, ctx, *args):
        await ctx.message.delete()
        to_reverse = " ".join(args) if len(args) > 0 else ctx.message.content
        await ctx.message.channel.send(to_reverse)


def setup(bot):
    bot.add_cog(Message(bot))
