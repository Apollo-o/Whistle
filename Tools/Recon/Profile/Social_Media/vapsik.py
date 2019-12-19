# Author: 0-0
# Date: 12.14.2019
# Description: A Profile finder.

import argparse
import requests

# =====================================================================================================

# Find Usernames.
# Precondition: One String.
# Postcondition: A File.
def connect(username):

    # Local Variables.
    keywords    = ("not found","Not Found","page you","not exist","error","cannot","couldn’t find","not valid")
    user_agent  = {"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A"}

    # Open File.
    reader   = open("sites.txt","r")
    elements = reader.read().split("\n")
    reader.close()

    # Create Dictionary.
    sites = {}
    index = 1
    for element in elements:
        middle       = element.find(":")
        start        = element[:middle].strip()
        end          = element[middle+1:].strip()
        sites[start] = end.format(username)

    # Find Usernames && Write to File.
    writer = open("profiles.txt","w")
    sessions = requests.session()
    for domain,url in sites.items():
        try:
            # Clear Cookies.
            sessions.cookies.clear()
            response   = sessions.get(url,headers=user_agent)  

            if response.status_code == 200 or (domain == "reddit.com" and response.status_code == 502):
                content = str(response.content)
                index = 0
                
                for keyword in keywords:
                    if keyword in content:
                        print("\033[1;33;20m[{}]".format(domain) + "\033[1;37;20m {}".format(url))
                        writer.write("{}\n".format(url))
                        break

                    elif index == len(keywords)-1:
                        print("\033[1;32;20m[{}]".format(domain) + "\033[1;37;20m {}".format(url))
                        writer.write("{}\n".format(url))

                    index += 1
            else:
                continue

        except (KeyboardInterrupt, Exception) as e:
            print(end="")
    
    # Close File.
    writer.close()

# =====================================================================================================

# Gets Arguments.
# Precondition: None.
# Postcondition: None.
def args():

    try:

        # Create Object && Format.
        parser = argparse.ArgumentParser(add_help=False)

        # Group && Add Arguments.
        group1 = parser.add_argument_group("options")
        group2 = parser.add_argument_group("additional")
        group1.add_argument("-u","--username",metavar="",help=": Insert a username.")
        group2.add_argument("-h","--help",action="help",default=argparse.SUPPRESS,help=": Display the usage screen.")

        # Join & Create Arguments.
        args = parser.parse_args()

        # If the Correct Command.
        if args.username:

            # Processing Data.
            connect(args.username)
    
        else:

            # Display Help.
            parser.print_help()

    except (KeyboardInterrupt, Exception) as e:
        print(str(e))

# Start's the program.
if __name__ == "__main__":
    args()
