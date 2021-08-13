import discord
from discord.ext import commands, tasks
from discord.utils import get
import json
from discord import asset
from discord.user import User


intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
client = commands.Bot(command_prefix='*', intents=intents)

welcome = "<:Wjin:865274048988184588><:Ejin:865274113174405131><:Ljin:865274170157432843><:Cjin:865274259353370634><:Ojin:865274346129850408><:Mjin:865274436168450058><:Ejin:865274113174405131>"


@client.event
async def on_ready():
    print('never gonna give you up')



















@client.event
async def on_member_join(member):
    print(f'welcome {member}')
    channel = client.get_channel(854247382086189066)
    await channel.send(
        "<:Wjin:865274048988184588><:Ejin:865274113174405131><:Ljin:865274170157432843><:Cjin:865274259353370634><:Ojin:865274346129850408><:Mjin:865274436168450058><:Ejin:865274113174405131>")
    embed1 = discord.Embed(title=f"Welcome {member}!", description=f"Contribute to #jin-chain to get started!")
    await channel.send(embed=embed1)
    role = get(member.guild.roles, id=833781809128669265)
    await member.add_roles(role)


@client.event
async def on_message(message):
    if not message.author.bot:
        print('function load')
        with open('level.json','r') as f:
            users = json.load(f)
            print('file load')
        await update_data(users, message.author,message.guild)
        await add_experience(users, message.author, 1, message.guild)
        await level_up(users, message.author,message.channel, message.guild)

        with open('level.json','w') as f:
            json.dump(users, f)
    await client.process_commands(message)




async def update_data(users, user,server):
    if not str(server.id) in users:
        users[str(server.id)] = {}
        if not str(user.id) in users[str(server.id)]:
            users[str(server.id)][str(user.id)] = {}
            users[str(server.id)][str(user.id)]['experience'] = 0
            users[str(server.id)][str(user.id)]['level'] = 1
    elif not str(user.id) in users[str(server.id)]:
            users[str(server.id)][str(user.id)] = {}
            users[str(server.id)][str(user.id)]['experience'] = 0
            users[str(server.id)][str(user.id)]['level'] = 1

async def add_experience(users, user, exp, server):
  users[str(user.guild.id)][str(user.id)]['experience'] += exp

async def level_up(users, user, channel, server):
  experience = users[str(user.guild.id)][str(user.id)]['experience']
  lvl_start = users[str(user.guild.id)][str(user.id)]['level']
  lvl_end = int(experience ** (1/4))
  if str(user.guild.id) != '757383943116030074':
    if lvl_start < lvl_end:
      await channel.send('{} has leveled up to Level {}'.format(user.mention, lvl_end))
      users[str(user.guild.id)][str(user.id)]['level'] = lvl_end


@client.command(aliases = ['xp'])
async def level(ctx,member: discord.Member = None):

    if not member:
        user = ctx.message.author
        with open('level.json','r') as f:
            users = json.load(f)
        lvl = users[str(ctx.guild.id)][str(user.id)]['level']
        exp = users[str(ctx.guild.id)][str(user.id)]['experience']

        embed = discord.Embed(title = 'Level {}'.format(lvl), description = f"{exp} XP " ,color = discord.Color.green())
        embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
        await ctx.send(embed = embed)
    else:
      with open('level.json','r') as f:
          users = json.load(f)
      lvl = users[str(ctx.guild.id)][str(member.id)]['level']
      exp = users[str(ctx.guild.id)][str(member.id)]['experience']
      embed = discord.Embed(title = 'Level {}'.format(lvl), description = f"{exp} XP" ,color = discord.Color.green())
      embed.set_author(name = member, icon_url = member.avatar_url)

      await ctx.send(embed = embed)



@client.event
async def on_member_remove(member):
    print(f'goodbye {member}')


@client.command()
async def jin(ctx):
    await ctx.send('<:jinhappy1:835921639551008818>')


@client.command()
async def xbox(ctx):
    await ctx.send('better')


@client.command()
async def playstation(ctx):
    await ctx.send('<:sony:858204031067357195>')


@client.command()
async def rickroll(ctx):
    await ctx.send('https://tenor.com/view/dance-moves-dancing-singer-groovy-gif-17029825')


@client.command()
async def rule16(ctx):
    await ctx.send('https://tenor.com/view/dead-chat-passione-admin-passione-jojolion-gif-19211422')


@client.command()
async def welcome(ctx):
    await ctx.send(
        "<:Wjin:865274048988184588><:Ejin:865274113174405131><:Ljin:865274170157432843><:Cjin:865274259353370634><:Ojin:865274346129850408><:Mjin:865274436168450058><:Ejin:865274113174405131>")





      

client.run('ODcyMTk0NzA3MTE0MDQ1NDQw.YQmUng.NX93HMWlDNvAmPPMQVqix1kasNg')
