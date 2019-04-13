import os
import time
from termcolor import colored

def screen():
    
    color = "cyan"
    color2 = "grey"

    print(colored("\n          .::^; .,", color2, attrs=['blink']))
    print(colored("         :;i   :i", color, attrs=['blink']))
    print(colored("        ::i  :;i", color, attrs=['blink']))
    print(colored("  ..::i :;:i:;i", color, attrs=['blink']))
    print(colored(" ,i", color2, attrs=['blink']), end="")
    print(colored("  :i::::::i", color, attrs=['blink']))
    print(colored("     ;;::;;:;;", color, attrs=['blink']))
    print(colored("     : o   o :", color2, attrs=['blink']))
    print(colored("     :.  n  .:", color2, attrs=['blink']))
    print(colored("       ( x )", color2, attrs=['blink']))
    print(colored("        ^^^", color2, attrs=['blink']))

    print("\n Options:\n\n 1. Encrypt \n 2. Decrypt")


def encrypt(arg):
    key = "abcdefghijklmnopqrstuvwxyz~`}{:;?/><.,|!+c)#($*%&^=-ABCDEFGHIJKLMNOPQRSTUVWXYZ6789012345"
    iv = "nopqrstuvwxyzabcdefghijklm!+c)#($*%&^=-~`}{:;?/><.,|SPIDERZABCFGHJKLMNOQTUVWXY1234567890"

    cipher = ""
    word = ""

    if arg == "1":

        file2 = open("Encrypt.pgp", "w")
        pin = input("\n Create Key: ")

        for k in pin:
            index = key.find(k)
            if index > -1:
                word += iv[index]
            else:
                word += k

        file2.write(word + "\n")

        user_input = input("\n Message: ")

        for i in user_input:
            index = key.find(i)
            if index > -1:
                cipher += iv[index]
            else:
                cipher += i

        file2.write(cipher)
        file2.close()

        dir_path = os.path.dirname(os.path.realpath(__file__))
        print("\n Location:", dir_path + "\\Encrypt.pgp")
        print("\n Apollo © 2018\n")
        time.sleep(3)


def decrypt(arg):
    global file

    color_end = "cyan"

    key = "abcdefghijklmnopqrstuvwxyz~`}{:;?/><.,|!+c)#($*%&^=-ABCDEFGHIJKLMNOPQRSTUVWXYZ6789012345"
    iv = "nopqrstuvwxyzabcdefghijklm!+c)#($*%&^=-~`}{:;?/><.,|SPIDERZABCFGHJKLMNOQTUVWXY1234567890"

    plaintext = ""
    word = ""

    if arg == "2":

        count = 0
        check = False

        while count != 2:

            user_input = input("\n File Path: ")

            try:
                file = open(user_input, "r")
                check = True
            except Exception as e:
                print()
                print(" " + colored(e, "red", attrs=['blink']))
                check = False

            if check:
                break

            count += 1

            if count == 2:
                print("\n" + colored(" Restart the Program.", color_end, attrs=['blink']) + "\n")
                time.sleep(3)

        if check:

            pin = input(" Enter Key: ")
            pin2 = file.readline()

            for k in pin2:
                index = iv.find(k)
                if index > -1:
                    word += key[index]
                else:
                    word += k

            word = word.strip(" ")
            word = word.strip("\n")

            times = 0

            while pin != word:

                print("\n" + colored(" Incorrect Password.", "red", attrs=['blink']) + "\n")
                pin = input(" Enter Key: ")

                if pin == word:
                    break

                elif times == 1:
                    print("\n" + colored(" Restart the Program.", color_end, attrs=['blink']) + "\n")
                    time.sleep(3)
                    break
                times += 1

            if pin == word:
                for line in file:
                    for i in line:

                        index = iv.find(i)
                        if index > -1:
                            plaintext += key[index]
                        else:
                            plaintext += " "

                print("\n Message >> " + plaintext)
                print("\n" + colored(" Press Enter to Exit: ", color_end, attrs=['blink']), end="")
                input("")

            file.close()


def main():
    color_end = "cyan"

    count = 0
    screen()

    user_response = input("\n >> ")

    while user_response > "2" or user_response < "1":
        print("\n" + colored(" Invalid Option.", "red", attrs=['blink']))
        user_response = input("\n >> ")

        if user_response == "1" or user_response == "2":
            break

        elif count == 1:
            print("\n" + colored(" Restart the Program.", color_end, attrs=['blink']) + "\n")
            time.sleep(3)
            break
        count += 1

    if user_response == "1" or user_response == "2":
        encrypt(user_response)
        decrypt(user_response)
        
main()
