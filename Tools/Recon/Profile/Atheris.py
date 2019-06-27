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
    urls = ["https://whocalld.com/+1{}{}{}",
            "https://www.whoeasy.com/pni/q/{}-{}-{}",

            "https://www.freephonetracer.com/fcpt.aspx?_act=Free&_pho={}-{}-{}",
            "https://www.reversephonelookup.com/number/{}{}{}/",
            "https://www.ussearch.com/search/phone/{}-{}-{}",

            "https://johndoe.com/phones/{}{}{}",
            "https://thatsthem.com/phone/{}-{}-{}",
            "https://www.thecallerguide.com/caller/{}-{}-{}",
            "https://www.truepeoplesearch.com/results?name={}{}{}",
            "https://www.whitepages.com/phone/1-{}-{}-{}",
            "https://www.zabasearch.com/phone/{}{}{}",

            "https://www.advancedbackgroundchecks.com/{}-{}-{}",
            "https://www.mylife.com/pub-multisearch.pubview?whyReg=Identity&ab_cid=seoIdentityReg&skipToRedirect=%2FssSubscription.do&search={}-{}-{}",
            
            "https://www.google.com/search?OxIUXfn7H8LU0gKLt53gAw&q={}{}{}",
            "https://www.bing.com/search?q={}{}{}",
            "https://duckduckgo.com/html?q={}{}{}"]

    # Launch URLS.
    event = 0
    for url in urls:
        webbrowser.open_new_tab(url.format(area,prefix,line))

        # Display Five Webpages.
        event += 1
        if event == 5:
            input(".....")
            event = 0

# Start Program.
# Precondition: A String.
# Postcondition: None.
def main(phone_number):

    # If 10 Digits | Invalid Phone Number.
    if len(phone_number) == 10 and phone_number.isdigit():
        generate_urls(str(phone_number))
    else:
        print("Invalid Phone Number.")

# Run Program.
# input("Phone Number: ")
main(input("Phone Number: "))
