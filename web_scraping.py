import urllib2
import re

url = raw_input("Enter a URL: ")

#connect to a URL
website = urllib2.urlopen(url)

#read html code
html = website.read()

#use re.findall to get all the links
links = re.findall('"((http|ftp)s?://.*?)"', html)

for link in links:
    print link

print "Enter / Press any key to exit:"
raw_input()
