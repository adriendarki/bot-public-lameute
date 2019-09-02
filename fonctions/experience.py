import time

import discord
from discord.ext import commands
import json
import asyncio


class Experience(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.bot.loop.create_task(self.save_users())
        #with open(r"C:/var/www/lameuteusers.json", 'r') as f:
        with open(r"C:\Users\adrie\PycharmProjects\untitled5\users.json", 'r') as f:
            self.users = json.load(f)

    async def save_users(self):
        await self.bot.wait_until_ready()
        while not self.bot.is_closed():
            #with open(r"C:/var/www/lameuteusers.json", 'w') as f:
            with open(r"C:\Users\adrie\PycharmProjects\untitled5\users.json", 'w') as f:
                json.dump(self.users, f, indent=4)

            await asyncio.sleep(5)

    def lvl_up(self, author_id):
        cur_xp = self.users[author_id]['experience']
        cur_lvl = self.users[author_id]['level']
        if time.time() - self.users[author_id]["last_message"] > 30:
            self.users[author_id]["last_message"] = time.time()
        if cur_xp >= round((4 * (cur_lvl ** 3)) / 5):
            self.users[author_id]['level'] += 1
            return True
        else:
            return False

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        author_id = str(message.author.id)

        if not author_id in self.users:
            self.users[author_id] = {}
            self.users[author_id]['level'] = 1
            self.users[author_id]['experience'] = 0
            self.users[author_id]["last_message"] = 0

        self.users[author_id]['experience'] += 1

        if self.lvl_up(author_id):
            await  message.channel.send(
                f"{message.author.mention} tu es maintenant niveau {self.users[author_id]['level']}! gg !")

    @commands.command()
    async def level(self, ctx, member: discord.Member = None):
        member = ctx.author if not member else member
        member_id = str(member.id)

        if not member_id in self.users:
            await ctx.send(" Cette personne na pas de niveau")
        else:
            embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

            embed.set_author(name=f"Level - {member}", icon_url=self.bot.user.avatar_url)

            embed.add_field(name="level", value=self.users[member_id]['level'])
            embed.add_field(name="experience", value=self.users[member_id]['experience'])

            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Experience(bot))
