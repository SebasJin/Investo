# Investo Intro and Important Info
***************************************************************************************************************************************
   ONLY WORKS ON LINUX (cuz windows given me admin problems)   

Just a program that I use to gather data on stocks. Less of an investing program, meant to be used to gather data on how companies of 
different types react to different events. Kinda like a web crawler or somethin. Not Financial advice, meant for educational uses only.

IMPORTANT INFO: None of the data in the program is encrypted nor protected, and it shouldn't be, as all of it with the exception of your
api key (learn about that later) is publicly available. This is just a tool for getting public data faster. ONLY WORKS ON LINUX.
***************************************************************************************************************************************

_____________________________________________________________________________________________________________________________________
# Investo Basic StartUp Guide

1. Move the entire file to your desired location, usually under /home or somewhere to your liking.

3. Open up the terminal by pressing control + alt + t and navigate to within the investo directory. (if ya need help pay attention to 5)

4. Skip part 5 if you know ur linux commands, navigate to investo directory 
  
5. If you need help navigating to the right director, take note of the directory in which the file is in. So let's say that the file   
is located in   /home/urusername/investo   If my username was SebasJin, the file would be in    /home/SebasJin/investo     
So, what you would do is  open up your termina (control alt t) if you closed it, and type in     cd /home/SebasJin/inevsto

6. From there, type in    python3 main.py

7. Investo will run once, and ask for your desired Username, type it in and press enter
Invest will now ask you for an api key, which you can get by going to https://www.alphavantage.co/support/#api-key
where you can get a free api key. Once you run through the process, take your api key and type it in.

8. type in   python3 main.py    once again, and Investo will display a messagec

NOTE: If you type anything incorrectly such as your api key, delete the file userdata.json, and run the command 
python3 main.py 
________________________________________________________________________________________________________________________________________
