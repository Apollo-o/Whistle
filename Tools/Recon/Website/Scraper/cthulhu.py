# Author: o-o
# Date: 11/28/2019
# Description: A simple web scraper.

from collections import OrderedDict
import argparse
import requests

# Parse the data.
# Precondition: A String.
# Postcondition: A List.
def parse(contents,keyword_1,keyword_2):

    temp = []
    for content in contents:
        if keyword_1 in content and keyword_2 in content:
	    ostring = content[content.find(keyword_2):]
            start   = ostring.find(keyword_2[-1])
            nstring = ostring[start+1:]
            end     = nstring.find(keyword_2[-1])
            if end == -1:
		temp.append(nstring.strip())
            else:
		temp.append(nstring[:end].strip())
    return temp

# Start's the program.
# Precondition: Three Strings.
# Postcondition: A File.
def connect(url,key1,key2,output):

    try:

        # Get HTML Content.
        response     = requests.get(url)

        # If 200 OK Proceed.
        if response.status_code == 200:
            content  = str(response.content).split("<")
            elements = OrderedDict.fromkeys(parse(content,key1,key2))
            
            # Save the data to a file.
            with open(output,"a") as writer:
                for element in elements:
                    writer.write(element + "\n")
    
    except (KeyboardInterrupt, Exception) as e:
        print(str(e))

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
        group1.add_argument("-u","--url",metavar="",help=": Insert a url <https://www.example.com/>")
        group1.add_argument("-k1","--keyword_1",metavar="",help=r': Insert a keyword <"keyword\r\n">')
        group1.add_argument("-k2","--keyword_2",metavar="",help=r': Insert a keyword <"keyword\t\n">')
        group1.add_argument("-o","--output",metavar="",help=": Save the output to a file.")
        group2.add_argument("-h","--help",action="help",default=argparse.SUPPRESS,help=": Displays the usage screen.")

        # Join & Create Arguments.
        args = parser.parse_args()

        # If the Correct Command.
        if (args.url and args.output) and (args.keyword_1 and args.keyword_2):

            # Processing Data.
            data = connect(args.url,args.keyword_1,args.keyword_2,args.output)

        else:

            # Display Help.
            parser.print_help()

    except (KeyboardInterrupt, Exception) as e:
        print(str(e))

# Start's the program.
if __name__ == "__main__":
    args()
