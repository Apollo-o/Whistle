def encrypt(message):

    key = "abcdefghijklmnopqrstuvwxyz~`}{:;?/><.,|!+c)#($*%&^=-ABCDEFGHIJKLMNOPQRSTUVWXYZ6789012345"
    iv = "nopqrstuvwxyzabcdefghijklm!+c)#($*%&^=-~`}{:;?/><.,|SPIDERZABCFGHJKLMNOQTUVWXY1234567890"
    cipher = ""
    user_input = message

    for i in user_input:
        index = key.find(i)
        if index > -1:
            cipher += iv[index]
        else:
            cipher += i

    return cipher

def decrypt(filePath):
    key = "abcdefghijklmnopqrstuvwxyz~`}{:;?/><.,|!+c)#($*%&^=-ABCDEFGHIJKLMNOPQRSTUVWXYZ6789012345"
    iv = "nopqrstuvwxyzabcdefghijklm!+c)#($*%&^=-~`}{:;?/><.,|SPIDERZABCFGHJKLMNOQTUVWXY1234567890"
    plaintext = ""
    try:
        file = open(filePath, "r")
        for line in file:
            for i in line:
                index = iv.find(i)
                if index > -1:
                    plaintext += key[index]
                else:
                    plaintext += i
        file.close()

        fileWriter = open("o-o..txt", "w")
        fileWriter.write(plaintext)
        fileWriter.close()
    except Exception as e:
        print("\n\t" + str(e))

def run():

    decrypt("o-o.txt")
    print("Success o-o")

run()
