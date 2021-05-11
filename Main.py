# Import
import requests  # Downloads Required Stock Data
import json # stores UserData and others
import os
from os import path
from time import sleep
import random
import string

global url
url = ''
global ticker
ticker = []
global user_info
user_info = []


class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


UserChoice = ''

intro_program_message = """
                                """+ Color.YELLOW + """------- + Investo by SebasJin + -------""" + Color.END + """
                                       
            Investo is a free collection of services to help you obtain valuable data on investing 
            FYI, Investo has not been ported to windows and only works on most linux distributions

            This service doesn't mean to serve as investment advice, and is ONLY for Educational purposes 
            * In order to begin this program, you must obtain a free Alphavantage api key and setup a Username *
            * This must be done by going to the website  https://www.alphavantage.co/support/#api-key *

            """ + Color.RED + """ULTRA IMPORTANT, This program can be read by anyone, There is NO ENCRYPTION Or Password System, and
            Only one user is supported, so copy this program into others home directory if they want to use it. \n\n\n""" + Color.END



def intro():  # checks to see if userdata is placed, and if not, then run through a intro process, else, pass
    if path.exists("userdata.json"):
        with open('userdata.json') as fp:
            user_info = json.load(fp)
        print(intro_program_message)
        print('\n\n ' + Color.CYAN + 'You are being logged in as ' + user_info[0],
              'and with an api key of ' + user_info[1] + Color.END)

        if not path.exists('tmpdata'):
            os.mkdir('tmpdata')

    else:  # gives info, sets up username and api key, load to file for persistence
        print(intro_program_message)
        user_info = []
        usernameinput = input(
            '\nBy creating a username you have acknowledged the terms: ')
        user_info.append(usernameinput)
        print('\n' * 90 + '        Hello ' + user_info[0])

        print("""
        As mentioned before, please go to https://www.alphavantage.co/support/#api-key and get a free API key
        Please type it in correctly, if not please delete the file userdata.txt and create a username again
        """)

        apikey = input('\nPlease Enter your api key: ')
        user_info.append(apikey)

        endintromssg = """
        This is your given user info is {0} and an api key of {1}
        In 5 seconds this program will end, please run it once more it to use it.
        """
        fp = open('userdata.json', 'w')
        json.dump(user_info, fp)
        fp.close()

        if not path.exists('tmpdata'):
            os.mkdir('tmpdata')

        print(endintromssg.format(user_info[0], user_info[1]))
        sleep(5)
        quit()


def informational_message():  ## Need to optimize message (the bold things), use {} and .format along with print(' ' *40 to make spaces)
    print("""                                   
    |----------------------------------------------------------------------------------------------------------------------|
    |                                                  """ + Color.BOLD + Color.GREEN + Color.UNDERLINE + """-INFO-""" + Color.END +
          """                                                              |
    |----------------------------------------------------------------------------------------------------------------------|
    With your API key, you may now begin to gather financial date. Note: You may request data only up to 5 times per minute

    Here is a list of the programs built-in functions.

    Typing in 'help' will show more information on this program, check it out if you are new. 

    Typing in 'q' or 'quit' will end the program. You can also use the  Control + c command if something wacky happens

    Typing in 'stocklookup' will prompt you to enter in a stock ticker which will give a brief summary of it's fundamentals 
    and provide a json file which can be used for more thorough analysis. Typing in a '-m' after 'stocklookup' will now 
    print more of the json file of fundamentals onto your console screen. 

    Typing in 'stockprice' will prompt you to enter a stock ticker and give you it's current/last price. That's all
    
    NOTE: MORE FUNCTIONALITY WILL BE ADDED LATER, and when entering a ticker symbol, uppercase is not required
    |----------------------------------------------------------------------------------------------------------------------|
    |----------------------------------------------------------------------------------------------------------------------|\n\n\n
    """)


def stocklookup():
    with open('userdata.json') as fp:
        user_info = json.load(fp)
    stockstart()
    url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol=' + ticker[0] + '&apikey=' + user_info[1]
    downloader(url)
    print(Color.RED + '\nYou are obtaining stock fundamentals for ' + ticker[0] +
          '. Please ensure that your internet is functional.' + Color.END)


def stockprice():
    with open('userdata.json') as fp:
        user_info = json.load(fp)
    stockstart()
    url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol=' + ticker[0] + '&apikey=' + user_info[1]
 
    # NEED TO CHANGE URL
    downloader(url)
    print('You are obtaining stock fundamentals for ' + ticker[0] +
          '. Please ensure that your internet is functional.')
    pass

def stockstart():
    tempticker = input(Color.BLUE + 'Enter Your Desired Ticker Symbol: ' + Color.END)
    tempticker = tempticker.upper()
    ticker.append(tempticker)
    filetype()


def filetype():
    global filename
    tempfilename = []
    x = [1,2,3]
    tempfilename.append(str(random.randint(1, 10)))
    for i in x:
        tempfilename.append(random.choice(string.ascii_letters))
    filename = ''.join(tempfilename)


def downloader(url):
    print('\n\nYour url is' + url)
    request = requests.get(url, allow_redirects=True)
    print(request.headers.get('content-type'))
    myfile = requests.get(url)
    open(os.getcwd() + '/tmpdata/data-' + filename + '.json', 'wb').write(myfile.content)


intro()


while True:
    informational_message()
    UserChoice = input(Color.BLUE + 'Enter Your desired command, exculde the ticker symbol: ' + Color.END)
    if UserChoice == 'stocklookup':
        stocklookup()
    if UserChoice == 'quit':
        quit()
    if UserChoice == 'q':
        quit()
    if UserChoice == 'help':
        print("""For Further Information, look for the file README.md and open it up.
            If you don\'t have it, go to https://github.com/SebasJin/Investo, and read the README.md file. """)

    # NEED TO ADD MORE FUNCTIONALITY, 


"""
NEAR GOALS (kinda like a roadmap?): ADD MORE COMMANDS,
: GET THE TYPE OFF FILE TO BE DISPLAYED IN NAME OF FILES (EX. A FILE WHICH HAS A TYPE OF OVERVIEW,
WOULD HAVE THAT IN IT'S TITLE)
: GET FILETYPE TO DISPLAY THE TICKER OF IT, ALONG WITH THE DATE.
: ADD METHOD OF GETTING STOCK PRICE EASILY

MIDDLE GOALS:
: ADD METHOD OF OPENING DOWNLOADED FILES, AND DISPLAYING LITLE PORTIONS OF IT AS A PREVIEW
EX: IF I WERE TO TYPE IN stocklookup, AND THEN ENTER IN ibm AS MY TICKER, I WOULD LIKE FOR THE PROGRAM TO 
PRINT OUT INFORMATION SUCH AS THE PE RATION/EPS/ETC IN LITTLE BITE SIZED PEICES.
: GET PROPER DOCUMENTATION
"""
