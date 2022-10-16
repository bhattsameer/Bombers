from selenium import webdriver
import os
from webdriver_manager.chrome import ChromeDriverManager  # 1st changer


def banner():
    print('''
		  ##              ##  =======     ####       ####    ####     =======
		  \ \    ####    / /  #      #  ##    ##    / /\ \  / /\ \    #      #
		   \ \  / /\ \  / /   #======   ##    ##   / /  \ \/ /  \ \   #====== 
		    \ \/ /  \ \/ /    #      #  ##    ##  / /    ####    \ \  #      #
		     ####    ####     =======     ####    ##              ##  =======
		''')


def main():
    driver = webdriver.Chrome(ChromeDriverManager().install())  # 2nd change
    driver.get('https://web.whatsapp.com/')

    name = input('Enter the name of user or group: ')
    msg = input('Enter your message: ')
    count = int(input('Enter the count: '))

    input('Enter any key after scanning QR code')

    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()

    # The classname of message box may vary.
    msg_box = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]')

    for i in range(count):
        msg_box.send_keys(msg)
        # The classname of send button may vary.
        button = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/div/div[2]/div[2]/button')
        button.click()
    print('Bombing Complete!!')


banner()
main()
