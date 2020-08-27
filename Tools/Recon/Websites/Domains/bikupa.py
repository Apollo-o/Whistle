# Author: o-o
# Date: 8/22/2020
# Description: Find Random Domains.

import argparse
import grequests
import requests
import re
import time

# Generate Domains.
# Precondition: A String.
# Postcondition: Display Domains.
def domains(option,filename):

    try:

        # Local Variables.
        start_time        = time.time()
        orange            = "\033[1;33;20m"
        default           = "\033[0;0;0m"
        spaces            = 60
        header            = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.103 Safari/537.36"}
        print("\n{}{}{} {} | {}{}{}".format(orange,"DOMAINS",default,(spaces-len("DOMAINS")) * " ",orange,"TITLE",default))

        # Script Options.
        urls = []
        if option == 1:

            # Read the File.
            reader          = open(filename,"r")
            responses_1     = reader.read().split("\n")
            reader.close()

            # Generate Domains.
            for response in responses_1:
                if response != "" and response.isalnum():
                    urls.append("https://"+ response.lower() + ".com/")

        elif option == 2:

            # GET WORDS.
            amount            = 100
            requests_1        = (grequests.get(link,headers=header,timeout=10) for link in ["https://randomword.com/"] * amount)
            responses_1       = grequests.imap(requests_1, grequests.Pool(amount))

            # Generate Domains.
            for response in responses_1:
               urls.append("https://" + str(response.content).split("id=\"random_word\">")[1].split("<")[0].strip() + ".com/")

        # Check Domains && Title.
        url = sorted(list(set(urls)))
        if option == 1 or option == 2:

            # Check Domains.
            requests_2        = (grequests.get(url,headers=header,timeout=10) for url in urls)
            responses_2       = grequests.imap(requests_2, grequests.Pool(len(urls)))

            for response in responses_2:

                # Find Title.
                title   = re.findall("<title[^>]*>(.*?)</title>",str(response.content))

                # Format Domain.
                domain = response.url.strip("https:").strip("/")
                if domain.find("/") > -1:
                    domain = domain.split("/")[0].strip()
                if domain.find("www.") > -1:
                    domain = domain.split("www.")[1].strip()

                # Display Data.
                if len(title) == 1:
                    print("{} {} | {}".format(domain, (spaces-len(domain)) * " ",title[0].strip()))
                else:
                    print("{} {} | {}".format(domain, (spaces-len(domain)) * " ",""))

        # Duration.
        duration = time.time() - start_time
        print("{}{}{} {} | {}{}:{}{}\n".format(orange,"DURATION",default,(spaces-len("DURATION")) * " ",orange,int(duration/60),int(duration % 60),default))

    except (Exception,KeyboardInterrupt) as e:
        print(str(e))

# Parse the Command.
# Precondition: None.
# Postcondition: Start Module.
def parse():

    try :

        # Create Object && Format.
        parser = argparse.ArgumentParser(add_help=False)

        # Group && Add Arguments.
        group1 = parser.add_argument_group("options")
        group2 = parser.add_argument_group("additional")
        group1.add_argument("-f",metavar="",help=": Find Domains <filename.txt>")
        group1.add_argument("-g",action="store_true",help=": Find Domains <generate>")
        group2.add_argument("-h",action="help",default=argparse.SUPPRESS,help=": Displays the usage screen.")

        # Join & Create Arguments.
        args = parser.parse_args()

        # If the Correct Command.
        if args.f:

            # Processing Data.
            domains(1,args.f)

        elif args.g:

            # Processing Data.
            domains(2,"")

        else:

            # Display Usage Screen.
            parser.print_help()

    except Exception as e:
        print(str(e))

# Execute the Program.
if __name__ == "__main__":
    parse()
