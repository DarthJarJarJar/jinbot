import discord
from discord.ext import commands, tasks
from discord.utils import get
from discord import asset
from discord.user import User
import levelsys
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import asyncio

import re
import functools
import itertools
import math
import random
import datetime
from discord_slash import SlashCommand,SlashContext, client,ComponentContext
import discord_slash
from discord_slash.utils.manage_commands import create_option
from discord_slash.utils.manage_components import create_button, create_actionrow
from discord_slash.model import ButtonStyle
import sys
from discord_slash.utils.manage_components import wait_for_component



from async_timeout import timeout
  

intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
client = commands.Bot(command_prefix='*', intents=intents)
slash = SlashCommand(client, sync_commands=True)
guilds = [826766972204744764]

welcome = "<:Wjin:865274048988184588><:Ejin:865274113174405131><:Ljin:865274170157432843><:Cjin:865274259353370634><:Ojin:865274346129850408><:Mjin:865274436168450058><:Ejin:865274113174405131>"


@client.event
async def on_ready():
    print('never gonna give you up')
    await client.change_presence(activity=discord.Game(name="Jin of Jinshima"))






cogs = [levelsys]

for i in range(len(cogs)):
    cogs[i].setup(client)



class Game:
    '''
    Class to hold the data for each game in the main psn profile trophy page
    '''

    def __init__(self, game_name, game_trophy_count, game_console, game_rank, game_bronze, game_silver, game_gold,
                 game_plat_rarity):
        self.game_name = game_name
        self.game_trophy_count = game_trophy_count
        self.game_console = game_console
        self.game_rank = game_rank
        self.game_bronze = game_bronze
        self.game_silver = game_silver
        self.game_gold = game_gold
        self.game_plat_rarity = game_plat_rarity

    def __str__(self):
        return f"{self.game_name} ({self.game_console}) [{self.game_plat_rarity}] - {self.game_trophy_count} - B({self.game_bronze}), S({self.game_silver}), G({self.game_gold})"


class Trophy:
    '''
    Class to hold trophies as objects.
    NOTE: trophy_type= 0-bronze, 1-silver, 2-gold, 3-platinum
    '''

    def __init__(self, trophy_name, trophy_game_name, trophy_type, trophy_percent, trophy_rarity, img_url):
        self.trophy_name = trophy_name
        self.trophy_game_name = trophy_game_name
        self.trophy_type = trophy_type
        self.trophy_percent = trophy_percent
        self.trophy_rarity = trophy_rarity
        self.trophy_image_url = img_url

    def __str__(self):
        return f"{self.trophy_game_name} - {self.trophy_name} ({self.trophy_percent} - {self.trophy_rarity}) [{self.trophy_type}]"


class PsnProfile:
    def __init__(self, profile_name):
        self.profile_name = profile_name
        self.plat_count = 0
        self.gold_count = 0
        self.silver_count = 0
        self.bronze_count = 0
        self.rare_trophies = []
        self.games = []
        self.profile_url = f"https://psnprofiles.com/{self.profile_name}"

    def scrape_psnprofile(self):
        checkParam = re.search("[~!#$%^&*()_+{}:;\\']", self.profile_name)
        assert checkParam == None, "Input psn profile parameter is invalid."
        foptions = webdriver.FirefoxOptions()
        foptions.binary_location = r'/app/vendor/firefox/firefox'
                

        foptions.add_argument('-headless')
        browser = webdriver.Firefox(executable_path=r"/app/vendor/geckodriver/geckodriver"
,
                                    options=foptions)
        browser.get(f"https://psnprofiles.com/{self.profile_name}")
        # Grabbing Rare Trophies
        rare_trophy_tr = browser.find_elements_by_xpath(
            "/html/body/div[6]/div[3]/div/div[2]/div[2]/div[4]/table/tbody/tr")
        for tr in rare_trophy_tr:
            tds = tr.find_elements_by_tag_name('td')
            trophyImgUrl = tds[0].find_element_by_tag_name("a").find_element_by_tag_name(
                "picture").find_element_by_tag_name("img").get_attribute("src")
            trophyName = tds[1].find_element_by_class_name("small-title").text
            trophyGameName = tds[1].find_elements_by_tag_name('div')[1].find_element_by_tag_name('a').text
            trophyPercent = tds[2].find_element_by_class_name("typo-top").text
            trophyRarity = tds[2].find_element_by_class_name("typo-bottom").text
            trophyURL = tds[3].find_element_by_tag_name('span').find_element_by_tag_name('img').get_attribute('src')
            trophyType = None
            if "bronze" in trophyURL:
                trophyType = "B"
            elif "silver" in trophyURL:
                trophyType = "S"
            elif "gold" in trophyURL:
                trophyType = "G"
            elif "platinum" in trophyURL:
                trophyType = "P"
            rtrophy = Trophy(trophyName, trophyGameName, trophyType, trophyPercent, trophyRarity, trophyImgUrl)
            self.rare_trophies.append(rtrophy)

        # Grabbing Top 10 games
        game_tr = browser.find_elements_by_xpath("/html/body/div[6]/div[3]/div/div[2]/div[1]/div[3]/table[2]/tbody/tr")
        count = 0
        for tr2 in game_tr:
            if count == 10:
                break
            tds = tr2.find_elements_by_tag_name('td')
            gameName = tds[1].find_element_by_class_name('title').text
            gameTrophyCount = tds[1].find_element_by_class_name('small-info').text.replace("<b>", " ").replace("</b>",
                                                                                                               " ")
            gameConsole = tds[2].find_element_by_class_name("platforms").find_element_by_tag_name("span").text
            gameRank = tds[3].find_element_by_class_name("game-rank").text
            trophyCountSpans = tds[4].find_element_by_class_name("trophy-count").find_elements_by_tag_name("span")
            gameBronze = trophyCountSpans[5].text
            gameSilver = trophyCountSpans[3].text
            gameGold = trophyCountSpans[1].text
            gamePlatRarity = trophyCountSpans[6].text
            newGame = Game(gameName, gameTrophyCount, gameConsole, gameRank, gameBronze, gameSilver, gameGold,
                           gamePlatRarity)
            self.games.append(newGame)
            count += 1
        browser.quit()

    def dbg_rare_trophies(self):
        print("Rare Trophies")
        print("--------------")
        for t in self.rare_trophies:
            print(t)

    def dbg_games(self):
        print("\nGames")
        print("--------------")
        for g in self.games:
            print(g)

    def get_profile(self):
        rareTrophyData = self.get_rare_trophies()
        profileGames = self.get_games()
        rareTrophies = ""
        finalMsg = ""
        rareTrophies += "**Rare Trophies**\n"
        rareTrophies += rareTrophyData + "\n"
        finalMsg += "**Game Trophies**\n"
        finalMsg += profileGames
        return finalMsg, rareTrophies

    def get_rare_trophies(self):
        finalMsg = ""
        for t in self.rare_trophies:
            finalMsg += str(t) + "\n"
        return finalMsg

    def get_games(self):
        finalMsg = ""
        for g in self.games:
            finalMsg += str(g) + "\n"
        return finalMsg
@client.command(name='psn', help="Grabs your profile data from Psnprofile")
async def get_psnprofile(ctx, profileName: str):
    if ctx.author == client.user:
        return
    newProfile = PsnProfile(profileName)
    msg1 = await ctx.channel.send("Please wait a moment...")
    newProfile.scrape_psnprofile()
    titleCard = profileName + "'s PSNProfile"
    gameData, rareData = newProfile.get_profile()
    newEmbed = discord.Embed(title=titleCard, url=newProfile.profile_url, description=gameData, color=0x2565c4)
    await msg1.edit(embed=newEmbed)







@client.event
async def on_member_join(member):
    print(f'welcome {member}')
    channel = client.get_channel(854247382086189066)
    jinchain = client.get_channel(834406006351462420)
    jinrules = client.get_channel(893929998614925322)
    await channel.send(
        "<:Wjin:865274048988184588><:Ejin:865274113174405131><:Ljin:865274170157432843><:Cjin:865274259353370634><:Ojin:865274346129850408><:Mjin:865274436168450058><:Ejin:865274113174405131>")
    embed1 = discord.Embed(title=f"Welcome {member}!", description=f"Contribute to {jinchain.mention} and check out {jinrules.mention} to get started! Remember to flame on and on and on and on")
    await channel.send(member.mention)
    await channel.send(embed=embed1)
    await channel.send('https://media.discordapp.net/attachments/826766972204744767/885951474109149274/tumblr_ovbx1zq11b1vo889bo8_400.gifv.gif')
    role = get(member.guild.roles, id=833781809128669265)
    await member.add_roles(role)






@client.event
async def on_member_remove(member):
    print(f'goodbye {member}')
    
    
    
@client.command()
async def jumbo(ctx, emoji: discord.Emoji):
    await ctx.send(emoji.url)
   


@client.command()
async def jin(ctx, num=1):
    if ctx.channel.name == ("jin-chain"):
        if num>25:
            await ctx.send("Please use a value less than 25")
        elif num<0:
            await ctx.send("Please use a positive value")
        else:
            for i in range(num):
                await ctx.send("<:jinhappy1:835921639551008818>")
    else:
        if num>5:
            await ctx.send("Please use a value less than 5")
        elif num<0:
            await ctx.send("Please use a positive value")
        else:
            for i in range(num):
                await ctx.send("<:jinhappy1:835921639551008818>")
                
                
 

        
     


@client.command()
async def xbox(ctx):
    await ctx.send('better')

@client.command()
async def regret(ctx):
    await ctx.send('Today I am filled with regret to inform that we have had to remove a member of our community due to leaking sensitive information.')

    

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
async def tasm2(ctx):
    await ctx.send("Some day, humanity will reach self individualization. Some day we'll move beyond petty scrabbles over the three poisons of life (greed, ignorance, and hatred). Some day, we will have reached a state where we're enlightened enough to watch TASM2 without calamity befalling us.")


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
async def mole(ctx):
    await ctx.send(" I'm going to reveal the truth.\n\n I am the mole.\n\n I in truth actually work with the aquatic animal in American spy ops to keep our country safe, and the government has declared this server a danger of the highest degree. It is to this end that I must monitor this server to make sure it doesn't invoke a third world war. It was for my country. It was for my duty.\n\nGod bless America.")

@client.command()
async def welcome(ctx):
    await ctx.send(
        "<:Wjin:865274048988184588><:Ejin:865274113174405131><:Ljin:865274170157432843><:Cjin:865274259353370634><:Ojin:865274346129850408><:Mjin:865274436168450058><:Ejin:865274113174405131>")

@client.command()
async def electro(ctx):
    await ctx.send('https://tenor.com/view/amazing-spiderman2vomit-electro-amazing-spiderman2-spiderman-vomit-sex-gif-13866212')
    
@client.command()
async def electrocursed(ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/826766972204744767/888332410046001182/resize.gif')
    
@client.command()
async def freeping(ctx):
    await ctx.send(f"Here's your free ping! {ctx.author.mention}")
    
@client.command()
async def language(ctx):
    await ctx.send("من فضلك لا تستخدم أي لغة أخرى غير Jin")
    
@client.command()
async def chatting(ctx):
    await ctx.send("Hey man, so I was thinking what if we make a server that is dedicated to chatting? As this one always seems to be dead :skull: @DarthJinJin")
    
    
@client.command()
async def flameon(ctx):
    await ctx.send("https://media.discordapp.net/attachments/826766972204744767/888296963517333564/flameon.gif")
    
@client.command()
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member : discord.Member):
    mutedrole = discord.utils.get(ctx.guild.roles, name="Mute")
    await member.add_roles(mutedrole)
    await ctx.send("User was muted")
    
@client.command()
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member : discord.Member):
    mutedrole = discord.utils.get(ctx.guild.roles, name="Mute")
    await member.remove_roles(mutedrole)
    await ctx.send("User was unmuted")

@client.command()
async def tsunami(ctx):
    await ctx.send(r"https://cdn.discordapp.com/attachments/826766972204744767/888799786818502656/ezgif-6-f8d0eca0573f.mp4")
                                         

        
@client.command()
async def avatar(ctx, avamember : discord.Member=None):
    if avamember == None:
      avamember = ctx.author
    userAvatarUrl = avamember.avatar_url
    await ctx.send(userAvatarUrl)        
        
                
@client.command(aliases=['lemons'])
async def lemon(ctx):
    await ctx.send("All right, I've been thinking when life gives you lemons, don't make lemonade! Make life take the lemons back! Get mad! I don't want your damn lemons! What am I supposed to do with these? Demand to see life's manager. Make life rue the day it thought it could give Cave Johnson lemons! Do you know who I am? I'm the man who's gonna burn your house down- with those lemons! I'm gonna get my engineers to invent a combustible lemon that burns down your house")        
        
                        
@client.command()
async def ill(ctx):
    await ctx.send(r'https://cdn.discordapp.com/attachments/316188354255519744/891745760406814720/unknown.png')        
        
        
@client.command()
async def jin34(ctx):
    await ctx.send("did you know that in ghost of tsushima, the game engine renders the main character, jin sakai at 34 fps but renders the rest of the game world at 30 fps? the reason this was implemented was because gameplay felt much smoother when the player character was rendered at a higher framerate than the rest of the game world. to learn more google 'jin sakai rule 34' ")

@client.command(aliases=['colour'])
@commands.has_any_role('Gold 1', 'Gold 2', 'Gold 3', 'Platinum', 'Jin Booster')
async def color(ctx, color = None):
    colorlist = ['blue','green','purple','orange','vomit']
    if color == None:
        await ctx.send(f"Please specify a valid color. Available colors: {colorlist}")
    else:
        #checking the color argument
        if color not in colorlist:
            await ctx.send(f"Please specify a valid color. Available colors: {colorlist}")
        else:
            #checking if author already has a color role
            for role in ctx.author.roles:
                for i in colorlist:
                    current_color_role = discord.utils.get(ctx.guild.roles, name=i)
                    if role == current_color_role:
                        await ctx.author.remove_roles(current_color_role)
                        break


            
            color_role = discord.utils.get(ctx.guild.roles, name=color)
            await ctx.author.add_roles(color_role)
            await ctx.send(f'Colors updated. Set color to {color}')
                

@client.command()
async def eldenring(ctx):
  
  delta = datetime.datetime(2022,2,25,0,0)-datetime.datetime.now()
  eldendays=str(delta.days)+" days "
  count = 0
  for i in range(len(str(delta))-1):
      if str(delta)[i]==",":
          count = i+2
  x=str(delta)[count:]
  y=x.split(":")

  eldenhours = f"{y[0]} hours {y[1]} minutes {round(float(y[2]))} seconds"
  eldentime=eldendays+eldenhours
 
  await ctx.send(f"Time until Elden Ring: {eldentime}")
  
  
  


@client.command()
async def countdown(ctx,yy,m,d):
  
  delta = datetime.datetime(int(yy),int(m),int(d),0,0)-datetime.datetime.now()
  eldendays=str(delta.days)+" days "
  count = 0
  for i in range(len(str(delta))-1):
      if str(delta)[i]==",":
          count = i+2
  x=str(delta)[count:]
  y=x.split(":")

  eldenhours = f"{y[0]} hours {y[1]} minutes {round(float(y[2]))} seconds"
  eldentime=eldendays+eldenhours
 
  await ctx.send(fr"Time until {yy}/{m}/{d}: {eldentime}")
 
@client.command()
async def jincast(ctx,flag=True):
    if flag==True:
      jincast = discord.utils.get(ctx.guild.roles, name="Jincast Follower")
      if jincast in ctx.author.roles:
        await ctx.send("You already have the Jincast Follower role")
      else:
        await ctx.author.add_roles(jincast)
        await ctx.send("Added the Jincast Follower role")
    elif flag=="remove":
      jincast = discord.utils.get(ctx.guild.roles, name="Jincast Follower")
      if jincast in ctx.author.roles:
        await ctx.author.remove_roles(jincast)
        await ctx.send("Removed the Jincast Follower role")
      else:
        await ctx.send("You don't have the Jincast Follower role")
    else:
      await ctx.send("Enter a valid argument")
        
    
  
        
 ######SLASH COMMANDS#######

@slash.slash(name="echo", description="echoes what you said", guild_ids=guilds,options=[create_option(name="text", description='text you wish to echo',required=True,option_type=3)])
async def echo(ctx : SlashCommand, text : str):
    await ctx.send(text)




@slash.slash(name="button", description="buttons test", guild_ids=guilds)
async def button(ctx:SlashContext):
    buttons = [
        create_button(style=ButtonStyle.blue, label="Electro",custom_id="electrovomit"),
        create_button(style=ButtonStyle.red, label="Flame on",custom_id="flameonandon")
        
    ]
    action_row = create_actionrow(*buttons)
    await ctx.send("Choose one",components=[action_row])
    while True:
        button_ctx: ComponentContext = await wait_for_component(client, components=action_row)
        if button_ctx.custom_id=="electrovomit":
            await button_ctx.edit_origin(content="https://tenor.com/view/amazing-spiderman2vomit-electro-amazing-spiderman2-spiderman-vomit-sex-gif-13866212")
        elif button_ctx.custom_id=="flameonandon":
            await button_ctx.edit_origin(content="https://media.discordapp.net/attachments/826766972204744767/888296963517333564/flameon.gif")


@slash.slash(name="jin", description="sends jins", guild_ids=guilds,options=[create_option(name='number', description='number of jins', required=True, option_type=4)])
async def jin(ctx:SlashContext,number):
    if number>5:
        await ctx.send("Please use a value less than 5", hidden=True)
    elif number<0:
        await ctx.send("Please enter a valid number", hidden=True)
    else:
        for i in range(number):
            await ctx.send('<:jinhappy1:835921639551008818>')
    

@slash.slash(name='xbox',guild_ids=guilds)
async def xbox(ctx):
    await ctx.send('better')

@slash.slash(name='regret',guild_ids=guilds)
async def regret(ctx):
    await ctx.send('Today I am filled with regret to inform that we have had to remove a member of our community due to leaking sensitive information.')

    

@slash.slash(name='fortnite',guild_ids=guilds)
async def fortnite(ctx):
    await ctx.send('https://tenor.com/view/kratos-kratos-fortnite-fortnite-fortnite-dance-kratos-fortnite-dance-gif-19435698')
    
    
@slash.slash(name='gamepass',guild_ids=guilds)
async def gamepass(ctx):
    await ctx.send('game pass has over 300 games to play at a low fee of $15 a month and your first 3 months are only a dollar for new members')
    
@slash.slash(name='tasm2',guild_ids=guilds)
async def tasm2(ctx):
    await ctx.send("Some day, humanity will reach self individualization. Some day we'll move beyond petty scrabbles over the three poisons of life (greed, ignorance, and hatred). Some day, we will have reached a state where we're enlightened enough to watch TASM2 without calamity befalling us.")

@slash.slash(name='rickroll',guild_ids=guilds)
async def rickroll(ctx):
    await ctx.send('https://tenor.com/view/dance-moves-dancing-singer-groovy-gif-17029825')
    
@slash.slash(name='ratchetandclank',guild_ids=guilds)
async def ratchetandclank(ctx):
    await ctx.send("They took the great story of the first game and completely cut out the interesting socioeconomic commentary and themes and satire of corporatism and shoved in the villain from the other franchise's games")

@slash.slash(name='rule16',guild_ids=guilds)
async def rule16(ctx):
    await ctx.send('https://tenor.com/view/dead-chat-passione-admin-passione-jojolion-gif-19211422')
@slash.slash(name='mole',guild_ids=guilds)
async def mole(ctx):
    await ctx.send(" I'm going to reveal the truth.\n\n I am the mole.\n\n I in truth actually work with the aquatic animal in American spy ops to keep our country safe, and the government has declared this server a danger of the highest degree. It is to this end that I must monitor this server to make sure it doesn't invoke a third world war. It was for my country. It was for my duty.\n\nGod bless America.")

@slash.slash(name='electro',guild_ids=guilds)
async def electro(ctx):
    await ctx.send('https://tenor.com/view/amazing-spiderman2vomit-electro-amazing-spiderman2-spiderman-vomit-sex-gif-13866212')
    
@slash.slash(name='electrocursed',guild_ids=guilds)
async def electrocursed(ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/826766972204744767/888332410046001182/resize.gif')
    
@slash.slash(name='freeping',guild_ids=guilds)
async def freeping(ctx):
    await ctx.send(f"Here's your free ping! {ctx.author.mention}")
    
@slash.slash(name='language',guild_ids=guilds)
async def language(ctx):
    await ctx.send("من فضلك لا تستخدم أي لغة أخرى غير Jin")
    
@slash.slash(name='chatting',guild_ids=guilds)
async def chatting(ctx):
    await ctx.send("Hey man, so I was thinking what if we make a server that is dedicated to chatting? As this one always seems to be dead :skull: @DarthJinJin")
    
    
@slash.slash(name='flameon',description="Flame on and on and on and on!",guild_ids=guilds)
async def flameon(ctx):
    await ctx.send("https://media.discordapp.net/attachments/826766972204744767/888296963517333564/flameon.gif")
    

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
                                 
client.run('ODcyMTk0NzA3MTE0MDQ1NDQw.YQmUng.NX93HMWlDNvAmPPMQVqix1kasNg')
