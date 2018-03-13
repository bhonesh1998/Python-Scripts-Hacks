import requests
import re
url = input('Enter a URL (include `http://`): ') # get url from user
website = requests.get(url)  # connecting to the URL
html = website.text # reading html code of web page
links = re.findall('"((http|ftp)s?://.*?)"', html) # grab all the links
for link in links:
    print(link[0]) # printing all the links
