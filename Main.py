# Import
import requests  # Downloads Required Stock Data
import pickle  # stores UserData and others
import json
import os
from os import path
from time import sleep
import random
import string

global url
url = ''
global ticker
ticker = 'BHLB'
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
                                ------- + Investo by SebasJin + -------
                                       
            Investo is a free collection of services to help you obtain valuable data on investing 
            FYI, Investo has not been ported to windows and only works on most linux distributions

            This service doesn't mean to serve as investment advice, and is ONLY for Educational purposes 
            * In order to begin this program, you must obtain a free Alphavantage api key and setup a Username**
            * This must be done by going to the website  https://www.alphavantage.co/support/#api-key**

            ULTRA IMPORTANT, This program can be read by anyone, There is NO ENCRYPTION Or Password System, and
            Only one user is supported, so copy this program into others home directory if they want to use it.
            """
""""
userdata=['SebasJin','FFG80DUAQ25JOM2R']
# Opening JSON file
# SebasJin
# FFG80DUAQ25JOM2R
fp=open('userdata.json','w')
json.dump(userdata,fp)
fp.close()
"""


def intro(
):  # checks to see if userdata is placed, and if not, then run through a intro process, else, pass
    if path.exists("userdata.json"):
        with open('userdata.json') as fp:
            user_info = json.load(fp)
        print('You are being logged in as ' + user_info[0],
              'and with an api key of ' + user_info[1])

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


def informational_message(
):  ## Need to optimize message (the bold things), use {} and .format along with print(' ' *40 to make spaces)
    print("""                                   
    |----------------------------------------------------------------------------------------------------------------------|
    |                                               """ + Color.BOLD +
          """   -INFO-""" + Color.END +
          """                                                              |
    |----------------------------------------------------------------------------------------------------------------------|
    With your API key, you may now begin to gather financial date. Note that you may request data up to 5 times per minute

    Here is a list of the programs built-in functions.

    Typing in 'stocklookup' will prompt you to enter in a stock ticker which will give a brief summary of it's fundamentals 
    and provide a json file which can be used for more thorough analysis. Typing in a '-m' after 'stocklookup' will now 
    print more of the json file of fundamentals onto your console screen. 

    Typing in 'stockprice' will prompt you to enter a stock ticker and give you it's current/last price. That's all
    
    Typing in i will show more information within this program

    NOTE: MORE FUNCTIONALITY WILL BE ADDED LATER, and when entering a ticker symbol, uppercase is not required
    |----------------------------------------------------------------------------------------------------------------------|
    |----------------------------------------------------------------------------------------------------------------------|\n\n
    """)


def stocklookup():
    with open('userdata.json') as fp:
        user_info = json.load(fp)
    stockstart()
    url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol=' + ticker + '&apikey=' + user_info[
        1]
    downloader(url)
    print('You are obtaining stock fundamentals for ' + ticker +
          '. Please ensure that your internet is functional.')


def stockprice():
    with open('userdata.json') as fp:
        user_info = json.load(fp)
    stockstart()
    url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol=' + ticker + '&apikey=' + user_info[1]
    print(user_info)
    print(url)
    print(ticker)
    request = requests.get(url, allow_redirects=True)
    print(request.headers.get('content-type'))
    myfile = requests.get(url)
    open(os.getcwd() + '/tmpdata/data.json', 'wb').write(myfile.content)


def stockstart():
    ticker = input('Enter Your Desired Ticker Symbol: ')
    ticker = ticker.upper()


def filetype(type):
    filename = []
    filename.append(type)
    filename.append(random.randint(1, 10))
    for i in filename:
        filename.append(random.choice(string.ascii_letters))
    ''.join(filename)


def downloader(url):
    print(url)
    request = requests.get(url, allow_redirects=True)
    print(request.headers.get('content-type'))
    myfile = requests.get(url)
    open(os.getcwd() + '/tmpdata/data.json', 'wb').write(myfile.content)


intro()

while True:
    # need to read pickle file for api key and data
    informational_message()
    UserChoice = input(
        'Enter your desired command, exclude the ticker symbol: ')
    if UserChoice == 'stocklookup':
        stocklookup()
    # NEED TO ADD MORE FUNCTIONAclear
