import discord
from discord.ext import commands, tasks
from discord.utils import get
from discord import asset
from discord.user import User
import levelsys
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

import re

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
                
                
 
@client.command
@commands.has_any_role("Jinderator", "Adjin")
async def mute(ctx, ussr : discord.User):
    await ussr.add_roles(discord.utils.get(ussr.guild.roles, name="Mute"))
    await ctx.send("User was muted")
        
     


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
async def welcome(ctx):
    await ctx.send(
        "<:Wjin:865274048988184588><:Ejin:865274113174405131><:Ljin:865274170157432843><:Cjin:865274259353370634><:Ojin:865274346129850408><:Mjin:865274436168450058><:Ejin:865274113174405131>")

@client.command()
async def electro(ctx):
    await ctx.send('https://tenor.com/view/amazing-spiderman2vomit-electro-amazing-spiderman2-spiderman-vomit-sex-gif-13866212')
    
@client.command()
async def freeping(ctx):
    await ctx.send(f"Here's your free ping! {ctx.author.mention}")
    
@client.command()
async def language(ctx):
    await ctx.send("من فضلك لا تستخدم أي لغة أخرى غير Jin")


client.run('ODcyMTk0NzA3MTE0MDQ1NDQw.YQmUng.NX93HMWlDNvAmPPMQVqix1kasNg')
