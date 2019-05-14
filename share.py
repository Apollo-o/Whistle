import urllib

reader = open("domains.txt","r")
domain_list = [domain_name.strip() for domain_name in reader]

TLDS = (".com",".org",".edu",".gov",".uk",".net",".ca",".de",".jp",".fr",".au",".us",".ru",".ch",".it",".nl",".se",".no",".es",".mil")
