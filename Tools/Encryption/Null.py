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

