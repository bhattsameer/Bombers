# Discord: TiMoFey#5066
# Github: https://github.com/timofey260/pyspam
# site: https://timofey26s.tilda.ws
# import______________________________________________
import codecs
import pyautogui
from os import system  # system use for clear messages
from time import sleep  # sleep block on load{wait...}
from colorama import Fore, init  # for colored text

# inits________________________________________________
init(Fore)  # colorama init
uns = ''  # unuse str. uses for def error()
# colors_______________________________________________
rr = Fore.RED
rg = Fore.GREEN
rc = Fore.CYAN
ry = Fore.YELLOW
# vars_______________________________________
x = 6
modes = 3
v = "1.2.5"
run = True
# banners____________________________________________
log = ('1.2.5:\n'
       '-interval added\n')
b = ('_____   +                       |||||||||||||||||| \n'
     '  |           /\\      /\\        |||||(0)|||(0)|||| \n'
     '  |     |    /  \\    /  \\       |||||||||||||||||| \n'
     '  |     |   /    \\  /    \\      ||||0\\|||||||/0||| \n'
     '  |     |  /      \\/      \\     ||||\\00000000/|||| \n'
     '========spam_programm===========|||||||||||||||||| \n')  # menu
cr = (rg + ' ________________________________________________ \n'
           '|-------------------Made by Timofey--------------|\n'
           '|Discord: TiMoFey#5066                           |\n'
           '|Github: https://github.com/timofey260/pyspam    |\n'
           '|site: https://timofey26s.tilda.ws               |\n'
           '|________________________________________________|\n')
err = (rr + ' _________________________________________________________ \n'
            '|---------------------------Errors------------------------|\n'
            '|1. FileError: file not found!                            |\n'
            '|2. NumError: {str} not a number!                         |\n'
            '|3. IndexError: index out of range!                       |\n'
            '|4. TypeError: {str} is not 1 - %1s!                        |\n'
            '|5. ListError: Error not found! correct def error()       |\n'
            '|_________________________________________________________|\n' % (x))


# deffs___________________________________________
def error(value, result, ver):  # errors: easy moding
    if value == 1:
        print('FileError: %1s file not found!' % result)

    elif value == 2:
        print('NumError: %1s not a number!' % result)

    elif value == 3:
        print('IndexError: index out of range!')

    elif value == 4:
        print('TypeError: %1s is not 1 - %1s!' % (result, ver))

    else:
        print('ListError: Error not found! correct def error()')
    input()
    exit()

def menud(pa1, pa2):
    print(ry + "[" + rc + str(pa1) + ry + "] " + pa2)


def menu():
    print(rr + b)
    menud(1, 'mode')  # menu text
    menud(2, 'credits')
    menud(3, 'Errorlist')
    menud(4, 'exit')
    menud(5, 'version')
    menud(6, 'log')
import pyperclip, keyboard

def paste(text):
    pyperclip.copy(text)
    keyboard.press_and_release('ctrl + v')


# programms__________________________________________________
while run:

    menu()
    name = input('>>> ')  # name(int)
    if name == '1':
        menud(1, 'file')  # menu text
        menud(2, 'message')
        menud(3, 'num_message')
        name = input('>>> ')
        if name == '1':

            f = input("file name: ")  # f - filename(str)
            print(rg + 'num of messages(you can use"all"): ' + rr)

            n = input()  # n - num of messages(int or str('all'))
            try:
                inte = int(input("interval[sec]: "))

            except:
                error(2, inte, ver)
            if n == 'all':
                num = 0  # num - index of file(int)
                fil = f + ".txt"  # file.txt
                try:  # errorfind
                    file = codecs.open(fil, 'r', encoding='utf-8').readlines()  # open file for 'all'
                except:
                    error(1, fil, x)
                filew = file
                le = len(filew)
            elif n != 'all':

                try:  # errorfind
                    n = int(n)  # n - num of messages(int or str('all'))
                except:
                    error(2, n, x)
                num = 0
                fil = f + ".txt"
                try:  # errorfind
                    file = codecs.open(fil, 'r', encoding='utf-8').readlines()  # open file for 'slice'
                    filew = file[:n]  # slice of file
                except:
                    error(1, fil, x)
                le = len(filew)
                if n > len(filew):
                    error(3, uns, x)

            elif n == "":
                error(2, n, x)
            sleep(4)  # wait...
            system('cls||clear')  # cls

            print(ry + b + "\nwait.  ")
            sleep(0.5)
            system('cls||clear')

            print(ry + b + "\nwait.. ")
            sleep(0.5)
            system('cls||clear')

            print(ry + b + "\nwait...")
            system('cls||clear')
            for a in filew:  # spam messages in file
                sleep(inte)
                print(rg + '%1d message send!' % (num + 1))  # print messages in screen
                paste(a)
                num = num + 1
                pyautogui.press('enter')
            print('=====process=====#file')
            pyautogui.alert('succefuly send %2d messages!' % (le))  # result
        elif name == '2':
            print(rr + b)
            print(rg + 'text: ' + rr)
            g = input()
            print(rg + 'num of messages(0 = inf.): ' + rr)
            try:
                inte = int(input("interval[sec]: "))

            except:
                error(2, inte, ver)
            try:  # errorfind
                n = int(input())
            except:

                error(2, n, x)
            sleep(4)  # wait...
            f = range(n)
            system('cls||clear')  # cls

            print(ry + b + "\nwait.  ")
            sleep(0.5)
            system('cls||clear')

            print(ry + b + "\nwait.. ")
            sleep(0.5)
            system('cls||clear')

            print(ry + b + "\nwait...")
            system('cls||clear')

            print('=====process=====#message')
            print(b, '\nmessage: %1s\ntimes: %1s' % (g, n))
            if n != 0:
                for i in f:  # spam messages
                    sleep(inte)
                    print(rg + '%1d message send!' % (i + 1))  # print messages in screen
                    paste(g)
                    pyautogui.press('enter')
            elif n == 0:
                r = True
                i = 0
                while r:
                    i = i + 1
                    sleep(inte)
                    print(rg + '%1d message send!' % (i))
                    paste(g)
                    pyautogui.press('enter')

            pyautogui.alert('succefuly send %2d messages!' % n)  # result
        elif name == '3':
            print(rr + b)
            print(rg + 'prefix: ' + rr)
            g = str(input())

            print(rg + 'suffix: ' + rr)
            su = str(input())
            print(rg + 'num of messages(0 = inf.): ' + rr)
            try:
                inte = int(input("interval[sec]: "))

            except:
                error(2, inte, ver)
            try:  # errorfind
                n = input()
                n = int(n)
            except:

                error(2, n, x)
            sleep(4)  # wait...
            f = range(n)
            system('cls||clear')  # cls

            print(ry + b + "\nwait.  ")
            sleep(0.5)
            system('cls||clear')

            print(ry + b + "\nwait.. ")
            sleep(0.5)
            system('cls||clear')

            print(ry + b + "\nwait...")
            system('cls||clear')

            print('=====process=====num_message')
            print(b, '\nprefix: %1s\nsuffix %1s\ntimes: %1s' % (g, su, n))
            if n != 0:
                for i in f:  # spam messages
                    sleep(inte)
                    print(rg + '%1d message send!' % (i + 1))  # print messages in screen
                    fo = ('%1s %1s %1s' %(g, str(i), su))
                    paste(g)
                    pyautogui.press('enter')
                    i = i + 1
            elif n == 0:
                r = True
                i = 0
                while r:
                    sleep(inte)
                    i = i + 1
                    print(rg + '%1d message send!' % (i))
                    fo =('%1s %1s %1s' %(g, str(i), su))
                    paste(g)
                    pyautogui.press('enter')

        else:
            error(4, name, modes)
    elif name == '2':  # credits
        system('cls||clear')  # cls
        print(cr)
        input()

    elif name == '3':  # errorlist
        system('cls||clear')  # cls
        print(err)
        input()

    elif name == '4':  # exit
        run = False

    elif name == '5':  # exit
        system('cls||clear')  # cls
        print(v)
        input()
    elif name == '6':  # exit
        system('cls||clear')  # cls
        print(log)
        input()
    else:
        error(4, name, x)
