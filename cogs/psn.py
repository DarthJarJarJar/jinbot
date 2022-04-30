import discord
from discord.ext import commands, tasks
from bs4 import BeautifulSoup
from selenium import webdriver
import re
'''from discord_slash import SlashCommand,SlashContext, client,ComponentContext
import discord_slash
from discord_slash.utils.manage_commands import create_choice, create_option
from discord_slash.utils.manage_components import create_button, create_actionrow
from discord_slash.model import ButtonStyle
from discord_slash.utils.manage_components import wait_for_component
from discord_slash.utils.manage_components import create_select, create_select_option, create_actionrow
from discord_slash import cog_ext, SlashContext'''
from selenium.webdriver.common.keys import Keys
guilds = [826766972204744764]


'''
contribution by habim#9767
'''

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
        checkParam = re.search("[~!#$%^&*()+{}:;\\']", self.profile_name)
        assert checkParam == None, "Input psn profile parameter is invalid."
        foptions = webdriver.FirefoxOptions()
        foptions.binary_location = r'/app/vendor/firefox/firefox'
                

        foptions.add_argument('-headless')
        browser = webdriver.Firefox(executable_path=r"/app/vendor/geckodriver/geckodriver"
,
                                    options=foptions)
        browser.get("https://psnprofiles.com/")

        sb = browser.find_element_by_css_selector("#psnId")



        sb.clear()
        sb.send_keys(self.profile_name)
        sb.send_keys(Keys.RETURN)
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
            if count == 15:
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




class psn(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self):
        print('never gonna make you cry')


    @commands.command(name='psn', help="Grabs your profile data from Psnprofile")
    async def get_psnprofile(self,ctx, profileName: str):
        
        newProfile = PsnProfile(profileName)
        msg1 = await ctx.channel.send("Please wait a moment...")
        newProfile.scrape_psnprofile()
        titleCard = profileName + "'s PSNProfile"
        gameData, rareData = newProfile.get_profile()
        newEmbed = discord.Embed(title=titleCard, url=newProfile.profile_url, description=gameData, color=0x2565c4)
        await msg1.edit(embed=newEmbed)


  

async def setup(client):
    await client.add_cog(psn(client))


