import re
import webbrowser

from bs4 import BeautifulSoup as bs
from urllib import request

def getPage():
	with request.urlopen("https://en.wikipedia.org/wiki/Special:Random") as page:
		soup = bs(page.read(), features="lxml")

		topic = str(soup.title)[7:-20] #get rid of <title> tags and "- Wikipedia"
		print("Found this!\n")
		print(topic)
		print("\n")

		text = []
		c = 0
		paras = soup.find_all("p") #get all <p> elements

		while len(text) <= 3: #to avoid empty paras
			text = re.split("<[^>]*>", str(paras[c]))
			c += 1

		print("".join(text)) #make it presentable
		print("\n")
		#TODO: remove citations from the text
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
