import re
import webbrowser

from bs4 import BeautifulSoup as bs
from urllib import request

def getPage():
	with request.urlopen("https://en.wikipedia.org/wiki/Special:Random") as page:
		soup = bs(page.read(), features="lxml")
		topic = str(soup.title)[7:-20]
		print("Found this!\n")
		print(topic)
		print("\n")
		#firstPara = str(soup.p)
		text = []
		c = 0
		while not len(text):
			para = soup.find_all("p")
			text = re.split("<[^>]*>", str(para[c]))
			c += 1

		print("".join(text))
		print("\n")
		ch = input("Would you like to view this in your browser? Y/n\n")
		if ch == "Y" or ch == "y":
			webbrowser.open_new(page.geturl())


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
