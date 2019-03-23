# Author: o-o
# Date: 3/3/2019
# Description: A modified command-line parser.

import argparse

# Parse the command.
# Precondition: None.
# Postcondition: Start module.

def parse():

    try :

        # Create Object && Format.
        parser = argparse.ArgumentParser(add_help=False)

        # Group && Add Arguments.
        group1 = parser.add_argument_group("options")
        group2 = parser.add_argument_group("additional")
        group1.add_argument("-u","--url",metavar="",help=": Insert a url <www.facebook.com>")
        group1.add_argument("-o","--output",metavar="",help=": Dump to output file.")
        group2.add_argument("-h","--help",action="help",default=argparse.SUPPRESS,help=": Displays the usage screen.")

        # Join & Create Arguments.
        args = parser.parse_args()

        # If the Correct Command.
        if args.url and args.output:

            # Processing Data.
            data = metadata()
    
            # Output File.
            writer(args.output,data)

        else:
            parser.print_help()

    except Exception as e:
        print(e)

# ===================================================================

# Author: o-o
# Date: 3/3/2019
# Description: A file writer.

# Write the data to a file.
# Precondition: Tuple && Multi-dimensional List.
# Postcondition: Write the data to a file.

def writer(name,data):

    # Create the file.
    with open(name, "w") as profile:

        # Write the data to the file.
        for key, value in data:
            profile.write("%s,%s\n" % (key,value))

    # Close the file.
    profile.close()

# Execute the program.
if __name__ == "__main__":
    parse()
