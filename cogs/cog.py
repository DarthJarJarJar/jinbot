import discord
from discord import app_commands
from discord.ext import commands
from dateutil import tz
from datetime import datetime
from googlesearch import search
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

guild_id = 826766972204744764

TOKEN = "OTcwMDI4Nzc5MjAyMzEwMTk0.G5r3CH.m-YD7lDpP5y6ixblZfq0xpJ6aqt0EQJFgzlI0A"
MY_GUILD_ID = discord.Object(guild_id)
CHROMEDRIVER_PATH = r"/app/.chromedriver/bin/chromedriver"


class PersistentView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label='Announcements', style=discord.ButtonStyle.green, custom_id='Annoucements')
    async def a(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('Added the announcements role', ephemeral=True)
        await interaction.user.add_roles(discord.utils.get(interaction.guild.roles, name="Announcements"))

    @discord.ui.button(label='Movies', style=discord.ButtonStyle.green, custom_id='Movies')
    async def m(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('Added the movies role', ephemeral=True)
        await interaction.user.add_roles(discord.utils.get(interaction.guild.roles, name="Movies"))

    @discord.ui.button(label='Games', style=discord.ButtonStyle.green, custom_id='Games')
    async def g(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('Added the games role', ephemeral=True)
        await interaction.user.add_roles(discord.utils.get(interaction.guild.roles, name="Games"))

    @discord.ui.button(label='Polls', style=discord.ButtonStyle.green, custom_id='Polls')
    async def p(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('Added the polls role', ephemeral=True)
        await interaction.user.add_roles(discord.utils.get(interaction.guild.roles, name="Polls"))

    @discord.ui.button(label='Fortnite', style=discord.ButtonStyle.green, custom_id='Fortnite')
    async def f(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('Added the fortnite role', ephemeral=True)
        await interaction.user.add_roles(discord.utils.get(interaction.guild.roles, name="Fortnite"))


class SelectColor(discord.ui.Select):

    def __init__(self):

        options = [
            discord.SelectOption(label="Blue", description="Adds the Blue color role!"),
            discord.SelectOption(label="Green", description="Adds the Green color role!"),
            discord.SelectOption(label="Vomit", description="Adds the Vomit color role!"),
            discord.SelectOption(label="Orange", description="Adds the Orange color role!"),
            discord.SelectOption(label="Purple", description="Adds the Purple color role!"),
            discord.SelectOption(label="Blurple", description="Adds the Blurple color role!"),
            discord.SelectOption(label="Peach", description="Adds the Peach color role!"),
            discord.SelectOption(label="Dark Red", description="Adds the Dark Red color role!"),
            discord.SelectOption(label="Black", description="Adds the Black color role!"),
            discord.SelectOption(label="Remove", description="Remove any color roles that you have!"),

        ]

        super().__init__(placeholder="Select an option", max_values=1, min_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == "Remove":
            colorlist = ["Blue", "Green", "Orange", "Purple", "Blurple", "Black", "Peach", "Dark Red", "Vomit"]
            for color in colorlist:
                temprole = discord.utils.get(interaction.guild.roles, name=color)
                await interaction.user.remove_roles(temprole)
                await interaction.message.edit(content=f"Removed your color role!", view=None)


        else:
            colorlist = ["Blue", "Green", "Orange", "Purple", "Blurple", "Black", "Peach", "Dark Red", "Vomit"]
            for color in colorlist:
                temprole = discord.utils.get(interaction.guild.roles, name=color)
                await interaction.user.remove_roles(temprole)
            colorrole = discord.utils.get(interaction.guild.roles, name=self.values[0])
            await interaction.user.add_roles(colorrole)
            await interaction.message.edit(content=f"Added the {self.values[0]} color role!", view=None)


class SelectView(discord.ui.View):
    def __init__(self, *, timeout=180):
        super().__init__(timeout=timeout)
        self.add_item(SelectColor())


class Button5(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label='1', style=discord.ButtonStyle.green)
    async def opt1(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 1
        self.stop()

    @discord.ui.button(label='2', style=discord.ButtonStyle.green)
    async def opt2(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 2
        self.stop()

    @discord.ui.button(label='3', style=discord.ButtonStyle.green)
    async def opt3(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 3
        self.stop()

    @discord.ui.button(label='4', style=discord.ButtonStyle.green)
    async def opt4(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 4
        self.stop()

    @discord.ui.button(label='5', style=discord.ButtonStyle.green)
    async def opt5(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 5
        self.stop()


class Button4(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label='1', style=discord.ButtonStyle.green)
    async def opt1(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 1
        self.stop()

    @discord.ui.button(label='2', style=discord.ButtonStyle.green)
    async def opt2(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 2
        self.stop()

    @discord.ui.button(label='3', style=discord.ButtonStyle.green)
    async def opt3(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 3
        self.stop()

    @discord.ui.button(label='4', style=discord.ButtonStyle.green)
    async def opt4(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 4
        self.stop()


class Button3(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label='1', style=discord.ButtonStyle.green)
    async def opt1(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 1
        self.stop()

    @discord.ui.button(label='2', style=discord.ButtonStyle.green)
    async def opt2(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 2
        self.stop()

    @discord.ui.button(label='3', style=discord.ButtonStyle.green)
    async def opt3(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 3
        self.stop()


class Button2(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label='1', style=discord.ButtonStyle.green)
    async def opt1(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 1
        self.stop()

    @discord.ui.button(label='2', style=discord.ButtonStyle.green)
    async def opt2(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 2
        self.stop()


class ButtonTest(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label='420', style=discord.ButtonStyle.green)
    async def opt1(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 420
        self.stop()

    @discord.ui.button(label='9211', style=discord.ButtonStyle.green)
    async def opt2(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 9211
        self.stop()


class Button1(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label='1', style=discord.ButtonStyle.green)
    async def opt1(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 1
        self.stop()


def format_timestamp(timestring: str):
    time_num_str = ""
    time_unit = ""
    for char in timestring:
        if char in "123456789":
            time_num_str += char
        else:
            time_unit += char
    time_num = int(time_num_str)
    timestamp_dict = {
        "year": 0,
        "month": 0,
        "day": 0,
        "hour": 0,
        "minute": 0,
        "second": 0,
    }
    if time_unit.lower() == "y":
        timestamp_dict["year"] = time_num
    elif time_unit.lower() == "mo":
        timestamp_dict["month"] = time_num
    elif time_unit.lower() == "d":
        timestamp_dict["day"] = time_num
    elif time_unit.lower() == "h":
        timestamp_dict["hour"] = time_num
    elif time_unit.lower() == "m":
        timestamp_dict["minute"] = time_num
    elif time_unit.lower() == "s":
        timestamp_dict["second"] = time_num
    tzinfo = tz.gettz('America/Toronto')
    now = datetime.now().astimezone(tz=tzinfo)

    t_dict = timestamp_dict

    newtime = datetime(year=now.year + t_dict["year"], month=now.month + t_dict["month"], day=now.day + t_dict["day"],
                       hour=now.hour + t_dict["hour"], minute=now.minute + t_dict["minute"],
                       second=now.second + t_dict["second"], ).astimezone(tz=tzinfo)

    return newtime


class cog(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('never gonna let you down')

    @commands.hybrid_command(description="Replies with pongs")
    @app_commands.guilds(guild_id)
    async def pings(self, ctx):
        await ctx.send('pongs')

    @commands.hybrid_command()
    @app_commands.guilds(guild_id)
    async def mute(self, ctx, member: discord.Member, time: str = None, reason: str = None):
        await member.timeout(format_timestamp(time), reason=reason)
        embed = discord.Embed(title=f"Muted {member.name}", color=discord.Color.green())

        embed.add_field(name="Time until unmute: ", value=time)
        embed.add_field(name="Muted by: ", value=ctx.author.mention)
        embed.add_field(name="Reason: ", value=reason)
        await ctx.send(embed=embed)

    @commands.hybrid_command()
    @app_commands.guilds(guild_id)
    async def jin(self, ctx):
        await ctx.send('happy')

    @commands.hybrid_command()
    @app_commands.guilds(MY_GUILD_ID)
    async def hello(self, ctx):
        await ctx.send('there')

    @commands.hybrid_command()
    @app_commands.guilds(MY_GUILD_ID)
    async def flame(self, ctx):
        await ctx.send('on')

    @commands.hybrid_command()
    @app_commands.guilds(MY_GUILD_ID)
    async def unmute(self, ctx, member: discord.Member):
        await member.timeout(None)
        await ctx.send(f"{member.name} was unmuted")

    @commands.command()
    async def jumbo(self, ctx, emoji: discord.Emoji):
        await ctx.send(emoji.url)

    @commands.hybrid_command()
    @app_commands.guilds(MY_GUILD_ID)
    @commands.has_permissions(manage_messages=True)
    async def ban(self, ctx, member: discord.Member, reason: str = None):
        name = member.name
        await member.ban()
        embed = discord.Embed(title=f"Banned {name}", color=discord.Color.green())

        embed.add_field(name="Banned by: ", value=ctx.author.mention)

        embed.add_field(name="Reason: ", value=reason)
        await ctx.send(embed=embed)

    @commands.hybrid_command()
    @app_commands.guilds(MY_GUILD_ID)
    @commands.has_permissions(manage_messages=True)
    async def unban(self, ctx, member: discord.Member, reason: str = None):
        await member.unban()
        embed = discord.Embed(title=f"Unbanned user", color=discord.Color.green())
        embed.add_field(name="Unbanned by: ", value=ctx.author.mention)
        embed.add_field(name="Reason: ", value=reason)
        await ctx.send(embed=embed)

    @commands.hybrid_command()
    @app_commands.guilds(MY_GUILD_ID)
    async def avatar(self, ctx, member: discord.Member = None):
        if member is None:
            member = ctx.author
        await ctx.send(member.avatar.url)

    @commands.hybrid_command()
    @app_commands.guilds(MY_GUILD_ID)
    async def color(self, ctx):
        view = discord.ui.View().add_item(SelectColor())
        await ctx.send("Menus!", view=view)

    @commands.hybrid_command()
    @app_commands.guilds(MY_GUILD_ID)
    async def countdown(self, ctx, yy, mm, dd):

        delta = datetime(int(yy), int(mm), int(dd), 0, 0) - datetime.now()
        eldendays = str(delta.days) + " days "
        count = 0
        for i in range(len(str(delta)) - 1):
            if str(delta)[i] == ",":
                count = i + 2
        x = str(delta)[count:]
        y = x.split(":")

        eldenhours = f"{y[0]} hours {y[1]} minutes {round(float(y[2]))} seconds"
        eldentime = eldendays + eldenhours

        await ctx.send(fr"Time until {yy}/{mm}/{dd}: {eldentime}")

    @commands.hybrid_command()
    @app_commands.guilds(MY_GUILD_ID)
    async def convert(self, ctx, first_currency: str, second_currency: str, amount):
        am = amount
        c1 = first_currency
        c2 = second_currency
        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')

        driver = webdriver.Chrome(CHROMEDRIVER_PATH, chrome_options=chrome_options)

        driver.get(
            fr"https://www.google.com/search?q={am}+{c1}+to+{c2}&rlz=1C5CHFA_enCA983CA983&oq={am}+{c1}+&aqs=chrome.0.69i59j69i57j0i67l8.1146j0j7&sourceid=chrome&ie=UTF-8")
        driver.implicitly_wait(10)
        elem = driver.find_element_by_css_selector(
            "#knowledge-currency__updatable-data-column > div.b1hJbf > div.dDoNo.ikb4Bb.gsrt > span.DFlfde.SwHCTb")
        val = elem.get_attribute("data-value")
        answer = f"{am} {c1.upper()} is {val} {c2.upper()}"
        await ctx.send(answer)
        driver.close()

    @commands.hybrid_command()
    @app_commands.guilds(MY_GUILD_ID)
    async def game(self, ctx, *, name: str):
        query = f"{name} metacritic"
        message: discord.Message = await ctx.send("<a:loading:920845271892643861>")

        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument("start-maximized")
        chrome_options.add_argument('--disable-dev-shm-usage')

        driver = webdriver.Chrome(CHROMEDRIVER_PATH, chrome_options=chrome_options)

        for j in search(query, tld="ca", num=10, stop=10, pause=2):
            driver.get(j)
            result = j
            break

        driver.implicitly_wait(5)

        elem = driver.find_element_by_css_selector(".xlarge > span:nth-child(3)")
        ms = elem.text
        link = driver.find_element_by_css_selector("div.must_play > img:nth-child(1)")
        val = link.get_attribute("src")
        print(val)

        title = driver.find_element_by_css_selector("a.hover_none > h1:nth-child(1)")
        print(title.text)
        try:
            element = driver.find_element_by_css_selector(
                ".product_summary > span:nth-child(2) > span:nth-child(1) > span:nth-child(4)")
            driver.execute_script("arguments[0].click();", element)
            fulldesc = driver.find_element_by_css_selector(".inline_expanded > span:nth-child(2)")
        except NoSuchElementException:
            fulldesc = driver.find_element_by_css_selector(
                ".product_summary > span:nth-child(2) > span:nth-child(1)")

        if "playstation" in result:
            print("yes")
            new_query = f"{name} ps store"

            for j in search(new_query, tld="com", num=10, stop=10, pause=2):
                storelink = j
                break
            view = discord.ui.View()
            style = discord.ButtonStyle.link
            item = discord.ui.Button(style=style, label="PS Store", url=result)
            view.add_item(item=item)

            embed = discord.Embed(title=title.text, colour=discord.Color.green(), url=result)
            embed.set_thumbnail(url=val)
            if len(fulldesc.text) > 1000:
                embed.add_field(name="Game Description: ", value=f"{fulldesc.text[:1000]}...", inline=False)

            else:
                embed.add_field(name="Game Description: ", value=fulldesc.text, inline=False)

            embed.add_field(name="Metacritic Score: ", value=f"**{ms}**", inline=False)
            driver.implicitly_wait(15)
            driver.quit()

            await message.edit(content=None, embed=embed, view=view)



        else:
            print("no")
            embed = discord.Embed(title=title.text, colour=discord.Color.green(), url=result)
            embed.set_thumbnail(url=val)
            if len(fulldesc.text) > 1000:
                embed.add_field(name="Game Description: ", value=f"{fulldesc.text[:1000]}...", inline=False)

            else:
                embed.add_field(name="Game Description: ", value=fulldesc.text, inline=False)

            embed.add_field(name="Metacritic Score: ", value=f"**{ms}**", inline=False)
            # flameonandon

            driver.implicitly_wait(15)
            driver.quit()

            await message.edit(content=None, embed=embed)

    @commands.hybrid_command()
    @app_commands.guilds(MY_GUILD_ID)
    async def kino(self, ctx, *, film_name: str):

        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        message = await ctx.send("please wait....")
        driver = webdriver.Chrome(CHROMEDRIVER_PATH, options=options)

        search_url = fr"https://letterboxd.com/search/films/{film_name}/"
        driver.get(search_url)
        driver.implicitly_wait(10)
        numberof = driver.find_element_by_css_selector(".col-17 > h2:nth-child(1)").text
        numberofkino = numberof.split()
        num = numberofkino[1]

        if num == "4":
            result_1 = driver.find_element_by_css_selector(
                ".results > li:nth-child(1) > div:nth-child(2) > h2:nth-child(1) > span:nth-child(1) > a:nth-child(1)").text
            result_2 = driver.find_element_by_css_selector(
                ".results > li:nth-child(2) > div:nth-child(2) > h2:nth-child(1) > span:nth-child(1) > a:nth-child(1)").text
            result_3 = driver.find_element_by_css_selector(
                ".results > li:nth-child(3) > div:nth-child(2) > h2:nth-child(1) > span:nth-child(1) > a:nth-child(1)").text
            result_4 = driver.find_element_by_css_selector(
                ".results > li:nth-child(4) > div:nth-child(2) > h2:nth-child(1) > span:nth-child(1) > a:nth-child(1)").text
            # result_5 = driver.find_element_by_css_selector(".results > li:nth-child(5) > div:nth-child(2) > h2:nth-child(1) > span:nth-child(1) > a:nth-child(1)").text

            year_1 = driver.find_element_by_css_selector(
                ".results > li:nth-child(1) > div:nth-child(2) > h2:nth-child(1) > span:nth-child(1) > small:nth-child(2) > a:nth-child(1)").text
            year_2 = driver.find_element_by_css_selector(
                ".results > li:nth-child(2) > div:nth-child(2) > h2:nth-child(1) > span:nth-child(1) > small:nth-child(2) > a:nth-child(1)").text
            year_3 = driver.find_element_by_css_selector(
                ".results > li:nth-child(3) > div:nth-child(2) > h2:nth-child(1) > span:nth-child(1) > small:nth-child(2) > a:nth-child(1)").text
            year_4 = driver.find_element_by_css_selector(
                ".results > li:nth-child(4) > div:nth-child(2) > h2:nth-child(1) > span:nth-child(1) > small:nth-child(2) > a:nth-child(1)").text
            # year_5 = driver.find_element_by_css_selector(".results > li:nth-child(5) > div:nth-child(2) > h2:nth-child(1) > span:nth-child(1) > small:nth-child(2) > a:nth-child(1)").text

            view = Button4()

            embed = discord.Embed(title=f"Search Results for {film_name} ", color=discord.Color.green())
            embed.add_field(name=f"1. {result_1} ({year_1})", value="---", inline=False)
            embed.add_field(name=f"2. {result_2} ({year_2})", value="---", inline=False)
            embed.add_field(name=f"3. {result_3} ({year_3})", value="---", inline=False)
            embed.add_field(name=f"4. {result_4} ({year_4})", value="---", inline=False)

            message: discord.Message = await ctx.send(embed=embed, view=view)
            await view.wait()
            opt = view.value

            if opt == 1:
                driver.get(driver.find_element_by_css_selector(
                    ".results > li:nth-child(1) > div:nth-child(2) > h2:nth-child(1) > span:nth-child(1) > a:nth-child(1)").get_attribute(
                    "href"))
            if opt == 2:
                driver.get(driver.find_element_by_css_selector(
                    ".results > li:nth-child(2) > div:nth-child(2) > h2:nth-child(1) > span:nth-child(1) > a:nth-child(1)").get_attribute(
                    "href"))
            if opt == 3:
                driver.get(driver.find_element_by_css_selector(
                    ".results > li:nth-child(3) > div:nth-child(2) > h2:nth-child(1) > span:nth-child(1) > a:nth-child(1)").get_attribute(
                    "href"))
            if opt == 4:
                driver.get(driver.find_element_by_css_selector(
                    ".results > li:nth-child(4) > div:nth-child(2) > h2:nth-child(1) > span:nth-child(1) > a:nth-child(1)").get_attribute(
                    "href"))

            driver.implicitly_wait(10)

            print(driver.find_element_by_css_selector(".headline-1").text)
            kino_year = driver.find_element_by_css_selector(".number > a:nth-child(1)").text
            kino_director = driver.find_element_by_css_selector("span.prettify").text
            print(driver.find_element_by_css_selector(".truncate > p:nth-child(1)").text)
            print(driver.find_element_by_css_selector(".display-rating").text)
            print(driver.find_element_by_css_selector(
                "div.react-component:nth-child(1) > div:nth-child(1) > img:nth-child(1)").get_attribute("src"))

            embed = discord.Embed(title=driver.find_element_by_css_selector(".headline-1").text,
                                  description=f"Directed by {kino_director}, **{kino_year}**",
                                  colour=discord.Color.green())
            embed.set_thumbnail(url=driver.find_element_by_css_selector(
                "div.react-component:nth-child(1) > div:nth-child(1) > img:nth-child(1)").get_attribute("src"))
            embed.add_field(name="Kino Description: ",
                            value=driver.find_element_by_css_selector(".truncate > p:nth-child(1)").text, inline=False)
            embed.add_field(name="Average Rating: ", value=driver.find_element_by_css_selector(".display-rating").text,
                            inline=False)

            driver.quit()

            await message.edit(content=None, embed=embed, view=None)

        if num == "3":
            result_1 = driver.find_element_by_css_selector(
                ".results > li:nth-child(1) > div:nth-child(2) > h2:nth-child(1) > span:nth-child(1) > a:nth-child(1)").text
            result_2 = driver.find_element_by_css_selector(
                ".results > li:nth-child(2) > div:nth-child(2) > h2:nth-child(1) > span:nth-child(1) > a:nth-child(1)").text
            result_3 = driver.find_element_by_css_selector(
                ".results > li:nth-child(3) > div:nth-child(2) > h2:nth-child(1) > span:nth-child(1) > a:nth-child(1)").text
            ## result_5 = driver.find_element_by_css_selector(".results > li:nth-child(5) > div:nth-child(2) > h2:nth-child(1) > span:nth-child(1) > a:nth-child(1)").text

            year_1 = driver.find_element_by_css_selector(
                ".results > li:nth-child(1) > div:nth-child(2) > h2:nth-child(1) > span:nth-child(1) > small:nth-child(2) > a:nth-child(1)").text
            year_2 = driver.find_element_by_css_selector(
                ".results > li:nth-child(2) > div:nth-child(2) > h2:nth-child(1) > span:nth-child(1) > small:nth-child(2) > a:nth-child(1)").text
            year_3 = driver.find_element_by_css_selector(
                ".results > li:nth-child(3) > div:nth-child(2) > h2:nth-child(1) > span:nth-child(1) > small:nth-child(2) > a:nth-child(1)").text
            # year_4 = driver.find_element_by_css_selector(".results > li:nth-child(4) > div:nth-child(2) > h2:nth-child(1) > span:nth-child(1) > small:nth-child(2) > a:nth-child(1)").text
            # year_5 = driver.find_element_by_css_selector(".results > li:nth-child(5) > div:nth-child(2) > h2:nth-child(1) > span:nth-child(1) > small:nth-child(2) > a:nth-child(1)").text

            view = Button3()

            embed = discord.Embed(title=f"Search Results for {film_name} ", color=discord.Color.green())
            embed.add_field(name=f"1. {result_1} ({year_1})", value="---", inline=False)
            embed.add_field(name=f"2. {result_2} ({year_2})", value="---", inline=False)
            embed.add_field(name=f"3. {result_3} ({year_3})", value="---", inline=False)
            #  embed.add_field(name=f"4. {result_4} ({year_4})",value="---",inline= False)
            # embed.add_field(name=f"5. {result_5} ({year_5})",value="---", inline= False)

            message = await ctx.send(embed=embed, view=view)
            await view.wait()
            opt = view.value

            if opt == 1:
                driver.get(driver.find_element_by_css_selector(
                    ".results > li:nth-child(1) > div:nth-child(2) > h2:nth-child(1) > span:nth-child(1) > a:nth-child(1)").get_attribute(
                    "href"))
            if opt == 2:
                driver.get(driver.find_element_by_css_selector(
                    ".results > li:nth-child(2) > div:nth-child(2) > h2:nth-child(1) > span:nth-child(1) > a:nth-child(1)").get_attribute(
                    "href"))
            if opt == 3:
                driver.get(driver.find_element_by_css_selector(
                    ".results > li:nth-child(3) > div:nth-child(2) > h2:nth-child(1) > span:nth-child(1) > a:nth-child(1)").get_attribute(
                    "href"))

            driver.implicitly_wait(10)

            print(driver.find_element_by_css_selector(".headline-1").text)
            kino_year = driver.find_element_by_css_selector(".number > a:nth-child(1)").text
            kino_director = driver.find_element_by_css_selector("span.prettify").text
            print(driver.find_element_by_css_selector(".truncate > p:nth-child(1)").text)
            print(driver.find_element_by_css_selector(".display-rating").text)
            print(driver.find_element_by_css_selector(
                "div.react-component:nth-child(1) > div:nth-child(1) > img:nth-child(1)").get_attribute("src"))

            embed = discord.Embed(title=driver.find_element_by_css_selector(".headline-1").text,
                                  description=f"Directed by {kino_director}, **{kino_year}**",
                                  colour=discord.Color.green())
            embed.set_thumbnail(url=driver.find_element_by_css_selector(
                "div.react-component:nth-child(1) > div:nth-child(1) > img:nth-child(1)").get_attribute("src"))
            embed.add_field(name="Kino Description: ",
                            value=driver.find_element_by_css_selector(".truncate > p:nth-child(1)").text, inline=False)
            embed.add_field(name="Average Rating: ", value=driver.find_element_by_css_selector(".display-rating").text,
                            inline=False)

            driver.quit()
            await message.edit(content=None, embed=embed, view=None)

        if num == "2":
            result_1 = driver.find_element_by_css_selector(
                ".results > li:nth-child(1) > div:nth-child(2) > h2:nth-child(1) > span:nth-child(1) > a:nth-child(1)").text
            result_2 = driver.find_element_by_css_selector(
                ".results > li:nth-child(2) > div:nth-child(2) > h2:nth-child(1) > span:nth-child(1) > a:nth-child(1)").text

            year_1 = driver.find_element_by_css_selector(
                ".results > li:nth-child(1) > div:nth-child(2) > h2:nth-child(1) > span:nth-child(1) > small:nth-child(2) > a:nth-child(1)").text
            year_2 = driver.find_element_by_css_selector(
                ".results > li:nth-child(2) > div:nth-child(2) > h2:nth-child(1) > span:nth-child(1) > small:nth-child(2) > a:nth-child(1)").text

            view = Button2()

            embed = discord.Embed(title=f"Search Results for {film_name} ", color=discord.Color.green())
            embed.add_field(name=f"1. {result_1} ({year_1})", value="---", inline=False)
            embed.add_field(name=f"2. {result_2} ({year_2})", value="---", inline=False)

            message = await ctx.send(embed=embed, view=view)
            await view.wait()
            opt = view.value
            await message.edit(content="please wait...", embed=None, view=None)

            if opt == 1:
                driver.get(driver.find_element_by_css_selector(
                    ".results > li:nth-child(1) > div:nth-child(2) > h2:nth-child(1) > span:nth-child(1) > a:nth-child(1)").get_attribute(
                    "href"))
            if opt == 2:
                driver.get(driver.find_element_by_css_selector(
                    ".results > li:nth-child(2) > div:nth-child(2) > h2:nth-child(1) > span:nth-child(1) > a:nth-child(1)").get_attribute(
                    "href"))

            driver.implicitly_wait(10)

            print(driver.find_element_by_css_selector(".headline-1").text)
            kino_year = driver.find_element_by_css_selector(".number > a:nth-child(1)").text
            kino_director = driver.find_element_by_css_selector("span.prettify").text
            print(driver.find_element_by_css_selector(".truncate > p:nth-child(1)").text)
            print(driver.find_element_by_css_selector(".display-rating").text)
            print(driver.find_element_by_css_selector(
                "div.react-component:nth-child(1) > div:nth-child(1) > img:nth-child(1)").get_attribute("src"))

            embed = discord.Embed(title=driver.find_element_by_css_selector(".headline-1").text,
                                  description=f"Directed by {kino_director}, **{kino_year}**",
                                  colour=discord.Color.green())
            embed.set_thumbnail(url=driver.find_element_by_css_selector(
                "div.react-component:nth-child(1) > div:nth-child(1) > img:nth-child(1)").get_attribute("src"))
            embed.add_field(name="Kino Description: ",
                            value=driver.find_element_by_css_selector(".truncate > p:nth-child(1)").text, inline=False)
            embed.add_field(name="Average Rating: ", value=driver.find_element_by_css_selector(".display-rating").text,
                            inline=False)

            driver.quit()
            await message.edit(content=None, embed=embed, view=None)

        if num == "1":
            result_1 = driver.find_element_by_css_selector(
                ".results > li:nth-child(1) > div:nth-child(2) > h2:nth-child(1) > span:nth-child(1) > a:nth-child(1)").text

            year_1 = driver.find_element_by_css_selector(
                ".results > li:nth-child(1) > div:nth-child(2) > h2:nth-child(1) > span:nth-child(1) > small:nth-child(2) > a:nth-child(1)").text

            embed = discord.Embed(title=f"Search Results for {film_name} ", color=discord.Color.green())
            embed.add_field(name=f"1. {result_1} ({year_1})", value=" ", inline=False)
            view = Button1()

            message = await ctx.send(embed=embed, view=view)
            await view.wait()

            opt = view.value
            await message.edit(content="please wait...", embed=None, view=None)

            if opt == 1:
                driver.get(driver.find_element_by_css_selector(
                    ".results > li:nth-child(1) > div:nth-child(2) > h2:nth-child(1) > span:nth-child(1) > a:nth-child(1)").get_attribute(
                    "href"))

            driver.implicitly_wait(10)

            print(driver.find_element_by_css_selector(".headline-1").text)
            kino_year = driver.find_element_by_css_selector(".number > a:nth-child(1)").text
            kino_director = driver.find_element_by_css_selector("span.prettify").text
            print(driver.find_element_by_css_selector(".truncate > p:nth-child(1)").text)
            print(driver.find_element_by_css_selector(".display-rating").text)
            print(driver.find_element_by_css_selector(
                "div.react-component:nth-child(1) > div:nth-child(1) > img:nth-child(1)").get_attribute("src"))

            embed = discord.Embed(title=driver.find_element_by_css_selector(".headline-1").text,
                                  description=f"Directed by {kino_director}, **{kino_year}**",
                                  colour=discord.Color.green())
            embed.set_thumbnail(url=driver.find_element_by_css_selector(
                "div.react-component:nth-child(1) > div:nth-child(1) > img:nth-child(1)").get_attribute("src"))
            embed.add_field(name="Kino Description: ",
                            value=driver.find_element_by_css_selector(".truncate > p:nth-child(1)").text, inline=False)
            embed.add_field(name="Average Rating: ", value=driver.find_element_by_css_selector(".display-rating").text,
                            inline=False)

            driver.quit()
            await message.delete()
            await ctx.send(content=None, embed=embed)

        if num == "RESULTS":
            embed = discord.Embed(title="No Results", description="No search results.", color=discord.Color.green())
            await ctx.send(embed=embed)


        else:

            result_1 = driver.find_element_by_css_selector(
                ".results > li:nth-child(1) > div:nth-child(2) > h2:nth-child(1) > span:nth-child(1) > a:nth-child(1)").text
            result_2 = driver.find_element_by_css_selector(
                ".results > li:nth-child(2) > div:nth-child(2) > h2:nth-child(1) > span:nth-child(1) > a:nth-child(1)").text
            result_3 = driver.find_element_by_css_selector(
                ".results > li:nth-child(3) > div:nth-child(2) > h2:nth-child(1) > span:nth-child(1) > a:nth-child(1)").text
            result_4 = driver.find_element_by_css_selector(
                ".results > li:nth-child(4) > div:nth-child(2) > h2:nth-child(1) > span:nth-child(1) > a:nth-child(1)").text
            result_5 = driver.find_element_by_css_selector(
                ".results > li:nth-child(5) > div:nth-child(2) > h2:nth-child(1) > span:nth-child(1) > a:nth-child(1)").text

            year_1 = driver.find_element_by_css_selector(
                ".results > li:nth-child(1) > div:nth-child(2) > h2:nth-child(1) > span:nth-child(1) > small:nth-child(2) > a:nth-child(1)").text
            year_2 = driver.find_element_by_css_selector(
                ".results > li:nth-child(2) > div:nth-child(2) > h2:nth-child(1) > span:nth-child(1) > small:nth-child(2) > a:nth-child(1)").text
            year_3 = driver.find_element_by_css_selector(
                ".results > li:nth-child(3) > div:nth-child(2) > h2:nth-child(1) > span:nth-child(1) > small:nth-child(2) > a:nth-child(1)").text
            year_4 = driver.find_element_by_css_selector(
                ".results > li:nth-child(4) > div:nth-child(2) > h2:nth-child(1) > span:nth-child(1) > small:nth-child(2) > a:nth-child(1)").text
            year_5 = driver.find_element_by_css_selector(
                ".results > li:nth-child(5) > div:nth-child(2) > h2:nth-child(1) > span:nth-child(1) > small:nth-child(2) > a:nth-child(1)").text

            director_1 = "---"
            director_2 = "---"
            director_3 = "---"
            director_4 = "---"
            director_5 = "---"

            view = Button5()

            embed = discord.Embed(title=f"Search Results for {film_name} ", color=discord.Color.green(), )
            embed.add_field(name=f"1. {result_1} ({year_1})", value=director_1, inline=False)
            embed.add_field(name=f"2. {result_2} ({year_2})", value=director_2, inline=False)
            embed.add_field(name=f"3. {result_3} ({year_3})", value=director_3, inline=False)
            embed.add_field(name=f"4. {result_4} ({year_4})", value=director_4, inline=False)
            embed.add_field(name=f"5. {result_5} ({year_5})", value=director_5, inline=False)

            await message.edit(content=None, embed=embed, view=view)
            await view.wait()
            opt = view.value
            await message.edit(content="please wait...", embed=None, view=None)

            if opt == 1:
                kino_url = driver.find_element_by_css_selector(
                    ".results > li:nth-child(1) > div:nth-child(2) > h2:nth-child(1) > span:nth-child(1) > a:nth-child(1)").get_attribute(
                    "href")
                driver.get(driver.find_element_by_css_selector(
                    ".results > li:nth-child(1) > div:nth-child(2) > h2:nth-child(1) > span:nth-child(1) > a:nth-child(1)").get_attribute(
                    "href"))
            if opt == 2:
                kino_url = driver.find_element_by_css_selector(
                    ".results > li:nth-child(2) > div:nth-child(2) > h2:nth-child(1) > span:nth-child(1) > a:nth-child(1)").get_attribute(
                    "href")
                driver.get(driver.find_element_by_css_selector(
                    ".results > li:nth-child(2) > div:nth-child(2) > h2:nth-child(1) > span:nth-child(1) > a:nth-child(1)").get_attribute(
                    "href"))
            if opt == 3:
                kino_url = driver.find_element_by_css_selector(
                    ".results > li:nth-child(3) > div:nth-child(2) > h2:nth-child(1) > span:nth-child(1) > a:nth-child(1)").get_attribute(
                    "href")
                driver.get(driver.find_element_by_css_selector(
                    ".results > li:nth-child(3) > div:nth-child(2) > h2:nth-child(1) > span:nth-child(1) > a:nth-child(1)").get_attribute(
                    "href"))
            if opt == 4:
                kino_url = driver.find_element_by_css_selector(
                    ".results > li:nth-child(4) > div:nth-child(2) > h2:nth-child(1) > span:nth-child(1) > a:nth-child(1)").get_attribute(
                    "href")
                driver.get(driver.find_element_by_css_selector(
                    ".results > li:nth-child(4) > div:nth-child(2) > h2:nth-child(1) > span:nth-child(1) > a:nth-child(1)").get_attribute(
                    "href"))
            if opt == 5:
                kino_url = driver.find_element_by_css_selector(
                    ".results > li:nth-child(5) > div:nth-child(2) > h2:nth-child(1) > span:nth-child(1) > a:nth-child(1)").get_attribute(
                    "href")
                driver.get(driver.find_element_by_css_selector(
                    ".results > li:nth-child(5) > div:nth-child(2) > h2:nth-child(1) > span:nth-child(1) > a:nth-child(1)").get_attribute(
                    "href"))

            driver.implicitly_wait(10)

            title = driver.find_element_by_css_selector(".headline-1").text
            year = driver.find_element_by_css_selector(".number > a:nth-child(1)").text
            director = driver.find_element_by_css_selector("span.prettify").text
            description = driver.find_element_by_css_selector(".truncate > p:nth-child(1)").text
            rating = driver.find_element_by_css_selector(".display-rating").text
            thumbnail = driver.find_element_by_css_selector(
                "div.react-component:nth-child(1) > div:nth-child(1) > img:nth-child(1)").get_attribute("src")
            print(title, year, director, description, rating, thumbnail)

            embed = discord.Embed(title=title,
                                  description=f"Directed by {director}, **{year}**",
                                  colour=discord.Color.green(), url=kino_url)
            try:
                embed.set_thumbnail(url=thumbnail)
            except:
                print("no url")
            embed.add_field(name="Kino Description: ",
                            value=description, inline=False)
            embed.add_field(name="Average Rating: ", value=rating,
                            inline=False)

            driver.quit()

            await message.edit(content=None, embed=embed, view=None)

        driver.close()

    @commands.hybrid_command()
    @app_commands.guilds(MY_GUILD_ID)
    async def button(self, ctx):
        view = ButtonTest()
        m = await ctx.send("Hello", view=view)

        await view.wait()
        opt = view.value
        await m.edit(content=f"You chose {opt}", view=None)

    @commands.hybrid_command()
    @app_commands.guilds(MY_GUILD_ID)
    async def prepare(self, ctx: commands.Context):
        embed = discord.Embed(title="Self Roles",
                              description="**Announcements:** Get notified for server announcements!\n**Movies:** Get "
                                          "notified when we're watching a movie!\n**Games:** Get notified when we're "
                                          "trying to play a game together!\n**Polls:** Get notified for "
                                          "polls!\n**Fortnite:** Get notified when we're playing Fortnite!")
        await ctx.send(embed=embed, view=PersistentView())

    @commands.hybrid_command()
    @app_commands.guilds(MY_GUILD_ID)
    async def pingping(self, ctx: commands.Context):
        await ctx.send("pongpong")

    async def cog_load(self):
        ...


async def setup(client):
    await client.add_cog(cog(client))
