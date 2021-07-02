import os
import colorama
from colorama import Fore, Style, init
import time
import urllib.request
import re

red = Fore.LIGHTRED_EX
cyan = Fore.LIGHTCYAN_EX
magenta = Fore.MAGENTA
blue = Fore.LIGHTBLUE_EX
yellow = Fore.YELLOW
dblue = Fore.BLUE
GREEN = Fore.GREEN
white = Fore.WHITE
colorama.init(autoreset=True)

banner = f"""
{red}
 ██░ ██  ██▓▓█████▄ ▓█████     ██▓███   ██░ ██  ██▓  ██████  ██░ ██ 
▓██░ ██▒▓██▒▒██▀ ██▌▓█   ▀    ▓██░  ██▒▓██░ ██▒▓██▒▒██    ▒ ▓██░ ██▒
▒██▀▀██░▒██▒░██   █▌▒███      ▓██░ ██▓▒▒██▀▀██░▒██▒░ ▓██▄   ▒██▀▀██░
{white}░▓█ ░██ ░██░░▓█▄   ▌▒▓█  ▄    ▒██▄█▓▒ ▒░▓█ ░██ ░██░  ▒   ██▒░▓█ ░██ 
░▓█▒░██▓░██░░▒████▓ ░▒████▒   ▒██▒ ░  ░░▓█▒░██▓░██░▒██████▒▒░▓█▒░██▓
 ▒ ░░▒░▒░▓   ▒▒▓  ▒ ░░ ▒░ ░   ▒▓▒░ ░  ░ ▒ ░░▒░▒░▓  ▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒
 ▒ ░▒░ ░ ▒ ░ ░ ▒  ▒  ░ ░  ░   ░▒ ░      ▒ ░▒░ ░ ▒ ░░ ░▒  ░ ░ ▒ ░▒░ ░
{red} ░  ░░ ░ ▒ ░ ░ ░  ░    ░      ░░        ░  ░░ ░ ▒ ░░  ░  ░   ░  ░░ ░
 ░  ░  ░ ░     ░       ░  ░             ░  ░  ░ ░        ░   ░  ░  ░                                             
"""
print(banner)
print("version 2.0 \ndeveloper - thelinuxuser-choice\ncredits - t0a5ted [v1]" + "\n\n\n")

# collect user input for url


def askforurl():
	global url
	website_is_up = ""
	longurl = input("Enter URL to Hide: ")
	print(Style.RESET_ALL)
	try:
		global status_code
		status_code = urllib.request.urlopen(longurl).getcode()
	except:
		print(f"\n{yellow}URL Does Not Exist or Website Not Online\n")
		askforurl()

	else:
		website_is_up = status_code == 200

	if any(i in longurl for i in ('https://', 'http://', ' ')) == False or website_is_up == "False":
		print(Fore.RED + "\nNot a Valid URL (Add \"https://\" or \"http://\" if you haven't) OR URL Host Not Online\n\n")
		print(Style.RESET_ALL)
		askforurl()
	else:
		print(Fore.GREEN + "\nValid URL!")
		print(Style.RESET_ALL)
		global url
		url = longurl

askforurl()
#global keywords
#keywords = keywords

keywords = input("Enter Key Words [to add end of url] (Seperate Key Words with \"-\" [10 words only]): ")
		
def shortenurl2():
	print(Fore.GREEN + "\n\n-----------SUCCESSFUL-----------")
	print(Style.RESET_ALL)
	result = os.popen('curl da.gd/s/?url=' + url).read()
	print("\nNew Hidden URL: " + result)

def shortenurl():
	global url
#global keywords
	print(Fore.GREEN + "\n\n-----------SUCCESSFUL-----------")
	print(Style.RESET_ALL)
	newurl = os.popen('curl \"da.gd/s/?url=' + url + "&shorturl=" + keywords + "\"").read()
	print("\nNew Hidden URL: " + newurl)

askforkeywords = input("Do you want to add Key Words? (y/n): ")
if askforkeywords == "y":
    #shortenurl()
    print(f"\n{blue}[/]{GREEN}Ok going on next section")
elif askforkeywords == "n":
		#shortenurl2()
    print(f"\n{blue}[/]{GREEN}Ok going on next section")
else:
		print(Fore.RED + "\n\nType \"y\" for yes and \"n\" for no....its not that hard")
		print(Style.RESET_ALL)

q1 = input("Do you want to hide more like a pro? (y/n): ")

if q1 == "y":
    website = input("Enter url to mask the phishing url 'ex[https://google.com , http://real.web.lk]' ---> ")
    sc = input("Enter social engineering words\n[!] Donot use space use '-' between social engineering words\n --->")
    print("Generating the link ... \n")
    newurl = os.popen('curl \"da.gd/s/?url=' + url + "&shorturl=" + keywords + "\"").read()
    result = os.popen('curl da.gd/s/?url=' + url).read()
    result1 = newurl.replace('https://', '')
    result2 = result.replace('https://', '')
    print("\nHere is the advanced hideurl_1 ----> "+website+'-'+sc+"@"+result1)
    print("Here is the advanced hideurl_2 ----> "+website+'-'+sc+"@"+result2)
    
elif q1 == "n":
	shortenurl2()
    
else:
		print(Fore.RED + "\n\nType \"y\" for yes and \"n\" for no....its not that hard")
		print(Style.RESET_ALL)