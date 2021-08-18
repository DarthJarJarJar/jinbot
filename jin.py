import discord
from discord.ext import commands, tasks
from discord.utils import get
from discord import asset
from discord.user import User
import levelsys


intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
client = commands.Bot(command_prefix='*', intents=intents)

welcome = "<:Wjin:865274048988184588><:Ejin:865274113174405131><:Ljin:865274170157432843><:Cjin:865274259353370634><:Ojin:865274346129850408><:Mjin:865274436168450058><:Ejin:865274113174405131>"


@client.event
async def on_ready():
    print('never gonna give you up')
    await client.change_presence(activity=discord.Game(name="Jin of Jinshima"))






cogs = [levelsys]

for i in range(len(cogs)):
    cogs[i].setup(client)




@client.command(name='psn', help="Grabs your profile data from Psnprofile")
async def get_psnprofile(ctx, profileName: str):
    if ctx.author == client.user:
        return
    newProfile = PsnProfile(profileName)
    await ctx.channel.send("Please wait a moment...")
    newProfile.scrape_psnprofile()
    titleCard = profileName + "'s PSNProfile"
    gameData, rareData = newProfile.get_profile()
    newEmbed = discord.Embed(title=titleCard, url=newProfile.profile_url, description=gameData, color=0x2565c4)
    await ctx.channel.send(embed=newEmbed)







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
async def on_member_remove(member):
    print(f'goodbye {member}')


@client.command()
async def jin(ctx, num=1):
    if ctx.channel.name == ("jin-chain"):
        if num>100:
        await ctx.send("Please use a value less than 100")
        else:
            for i in range(num):
        
                await ctx.send('<:jinhappy1:835921639551008818>')

    else:   
        if num>25:
            await ctx.send("Please use a value less than 25")
        else:
            for i in range(num):
        
                await ctx.send('<:jinhappy1:835921639551008818>')


@client.command()
async def xbox(ctx):
    await ctx.send('better')
    

@client.command()
async def fortnite(ctx):
    await ctx.send('https://tenor.com/view/kratos-kratos-fortnite-fortnite-fortnite-dance-kratos-fortnite-dance-gif-19435698')
    
    
@client.command()
async def gamepass(ctx):
    await ctx.send('game pass has over 300 games to play at a low fee of $15 a month and your first 3 months are only a dollar for new members')
    


@client.command()
async def playstation(ctx):
    await ctx.send('<:sony:858204031067357195>')


@client.command()
async def rickroll(ctx):
    await ctx.send('https://tenor.com/view/dance-moves-dancing-singer-groovy-gif-17029825')
    
@client.command()
async def ratchetandclank(ctx):
    await ctx.send("They took the great story of the first game and completely cut out the interesting socioeconomic commentary and themes and satire of corporatism and shoved in the villain from the other franchise's games")

@client.command()
async def rule16(ctx):
    await ctx.send('https://tenor.com/view/dead-chat-passione-admin-passione-jojolion-gif-19211422')


@client.command()
async def welcome(ctx):
    await ctx.send(
        "<:Wjin:865274048988184588><:Ejin:865274113174405131><:Ljin:865274170157432843><:Cjin:865274259353370634><:Ojin:865274346129850408><:Mjin:865274436168450058><:Ejin:865274113174405131>")

@client.command()
async def electro(ctx):
    await ctx.send('https://tenor.com/view/amazing-spiderman2vomit-electro-amazing-spiderman2-spiderman-vomit-sex-gif-13866212')
    
@client.command()
async def freeping(ctx):
    await ctx.send(f"Here's your free ping! {ctx.author.mention}")


client.run('ODcyMTk0NzA3MTE0MDQ1NDQw.YQmUng.NX93HMWlDNvAmPPMQVqix1kasNg')
