from selenium import webdriver
import os
from webdriver_manager.chrome import ChromeDriverManager
import argparse
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import sys
from selenium.webdriver.chrome.options import Options


def banner():
    print('''
                  _______  __          __                             ____     ____    __  __   ____             
                 |__   __| \ \        / /                            |  _ \   / __ \  |  \/  | |  _ \      /\    
                    | |     \ \  /\  / /   ___    __ _   _ __        | |_) | | |  | | | \  / | | |_) |    /  \   
                    | |      \ \/  \/ /   / __|  / _` | | '__|       |  _ <  | |  | | | |\/| | |  _ <    / /\ \  
                    | |       \  /\  /    \__ \ | (_| | | |          | |_) | | |__| | | |  | | | |_) |  / ____ \    ☢️
                    |_|        \/  \/     |___/  \__,_| |_|          |____/   \____/  |_|  |_| |____/  /_/    \_\                                                                                          
                    
                                                      By: akshaykalucha3
                    Note : I won't be responsible for any damage caused by this script, Use at your own risk
    
    ''')

parser = argparse.ArgumentParser(description='Bomb twitter user with spam messages')

""" 4 Step: 

    1) run command python Twitter_bomber.py -u *your_twitter_username* -p *your_twitter_password*
    2) enter correct username of person you want to spam, make sure his twitter messages are open
    3) press 1 if you want to manually type the message you eant to send; or 2 if you want to export a file and extract message from there
    4) enter message count

"""

parser.add_argument('-u', '--username', type=str, required=True, help="twitter username @\ of user, can be his phone number or email")
parser.add_argument('-p', '--password', type=str, required=True, help="twitter password of the user")
args = parser.parse_args()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)    


def bombMsg(n, txt):
    for i in range(n):
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > section:nth-child(2) > div.css-1dbjc4n.r-1pz39u2.r-13awgt0 > div > div > div > div > aside > div.css-1dbjc4n.r-obd0qt.r-18u37iz.r-1uu6nss.r-13qz1uu > div.css-1dbjc4n.r-1kihuf0.r-16y2uox.r-1wbh5a2 > div > div > div > div > div.css-901oao.r-jwli3a.r-6koalj.r-16y2uox.r-1qd0xha.r-a023e6.r-16dba41.r-ad9z0x.r-bcqeeo.r-qvutc0 > div > div > div > div.DraftEditor-editorContainer > div > div > div > div'))).send_keys(txt)
        SendBtn = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/section[2]/div[2]/div/div/div/div/aside/div[2]/div[3]')
        SendBtn.click()
    print("Bombing Complete !!!")
    banner()


def attack():
    driver.get('https://twitter.com/login')
    userId = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input')
    userId.send_keys(args.username)
    userPass = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input')
    userPass.send_keys(args.password)

    loginBtn = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div')
    loginBtn.click()
    driver.minimize_window()

    name = input('Enter the twitter name of victim: ')
    if len(name) >= 3:
        pass
    else:
        name = input('Enter the name of victim correctly: ')

    ### GET VICTIM PROFILE PAGE ###
    driver.get(f'https://twitter.com/{name}')
    time.sleep(1)
    driver.maximize_window()


    ## GET MESSAGE INBOX ###
    messageLink = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[1]/div/div[1]/div/div[2]')
    messageLink.click()

    #### SEND MESSAGE IN VICTIMS INBOX ###

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/section[2]/div[2]/div/div/div/div/aside/div[2]/div[2]/div/div/div/div/div[1]/div'))).click()
    MsgBx = driver.find_element_by_css_selector('#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > section:nth-child(2) > div.css-1dbjc4n.r-1pz39u2.r-13awgt0 > div > div > div > div > aside > div.css-1dbjc4n.r-obd0qt.r-18u37iz.r-1uu6nss.r-13qz1uu > div.css-1dbjc4n.r-1kihuf0.r-16y2uox.r-1wbh5a2 > div > div > div > div > div.css-901oao.r-jwli3a.r-6koalj.r-16y2uox.r-1qd0xha.r-a023e6.r-16dba41.r-ad9z0x.r-bcqeeo.r-qvutc0 > div > div > div > div.DraftEditor-editorContainer > div > div > div > div')
    Ops = int(input("Select what form of messahe you would like to send: \n Enter [1] to send manual message Enter [2] to import a txt file: "))
    if Ops == 1:
        Content = input("Enter the message: ")
    elif Ops == 2:
        fileLoc = input("Enter the file location: ")
    instances = int(input("Enter total count: "))

    bombMsg(instances, Content)

attack()

