# Author: O-O
# Date: 6/23/2019
# Description: A Simple Reverse Lookup Program.

import webbrowser

# Generates URLS.
# Precondition: A String.
# Postcondition: Web-Browser Controller (Opens URLS)
def generate_urls(phone_number):

    # Phone Number.
    area,prefix,line = phone_number[:3], phone_number[3:6], phone_number[6:]

    # Generate URLS.
    urls = ["https://www.truepeoplesearch.com/results?phoneno=({}) {}-{}",
             "https://www.reversephonelookup.com/number/{}{}{}/",
             "https://www.whitepages.com/phone/1-{}-{}-{}",
             "https://www.zabasearch.com/phone/{}{}{}"]

    # Launch URLS.
    event = 0
    for url in urls:
        webbrowser.open_new_tab(url.format(area,prefix,line))

        # Display Five Webpages.
        event += 1
        if event == 5:
            input(".....")

# Start Program.
# Precondition: A String.
# Postcondition: None.
def main(phone_number):

    # If 10 Digits | Invalid Phone Number.
    if len(phone_number) == 10:
        generate_urls(str(phone_number))
    else:
        print("Invalid Phone Number.")

# Run Program.
main(input("Phone Number: "))
