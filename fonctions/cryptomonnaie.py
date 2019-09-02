import json
import aiohttp
from discord.ext import commands


class Cryptomonnaie(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def bitcoin(self, ctx):
        # appelle une api et transforme la réponse en donnée lisible pour lire le prix du BTC
        url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
        async with aiohttp.ClientSession() as session:  # Async HTTP request
            raw_response = await session.get(url)
            response = await raw_response.text()
            response = json.loads(response)
            await  ctx.send(" le prix du Bitcoin est de : $" + response['bpi']['USD']['rate'])

    @commands.command()
    async def eth(self, ctx):
        # appelle une api et transforme la réponse en donnée lisible pour lire le prix de l ETH
        url = 'https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=BTC,USD,EUR.json'
        async with aiohttp.ClientSession() as session:  # Async HTTP request
            raw_response = await session.get(url)
            response = await raw_response.text()
            response = json.loads(response)
            await  ctx.send(" le prix du Bitcoin est de : $" + response['BTC']['USD'])


def setup(bot):
    bot.add_cog(Cryptomonnaie(bot))