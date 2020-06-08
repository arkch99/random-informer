import re

from bs4 import BeautifulSoup as bs
from urllib import request

def getPage():
	with request.urlopen("https://en.wikipedia.org/wiki/Special:Random") as page:
		soup = bs(page.read(), features="lxml")
		topic = str(soup.title)[7:-20]
		print("Found this!")
		print(topic)
		firstPara = str(soup.p)
		text = re.split("<[^>]*>", firstPara)
		print("".join(text))
		print()

getPage()
while True:
	ch = input("Want another page? Y/n \n")
	if ch == "Y" or ch == "y":
		getPage()
	elif ch == "N" or ch == "n":
		print("Thank you, have a nice day :)")
		break
	else:
		print("Sorry, that doesn't make sense. Please enter again.")
