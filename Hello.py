import re
import requests
urls = ["https://engineering.buffalo.edu/computer-science-engineering/people/faculty-directory.html",
        "https://engineering.buffalo.edu/computer-science-engineering/people/faculty-directory.adjunct.html",
        "https://engineering.buffalo.edu/computer-science-engineering/people/faculty-directory.affiliated.html",
        "https://engineering.buffalo.edu/computer-science-engineering/people/faculty-directory.emeriti.html",
        ]
mails=[]
for url in urls:
    regex = r"[a-z]+?\.?[a-z0-9]+@[a-z]+\.[a-z]+"
    r = requests.get(url)
    for re_match in re.findall(regex,r.text):
        if re_match not in mails:
            mails.append(re_match)
for i in mails:
    print(i)
    