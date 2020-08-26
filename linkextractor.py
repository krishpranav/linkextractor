#!usr/bin/env/python

import sys
import os
import time
import requests
from bs4 import BeautifulSoup

def banner():
	os.system("figlet LINKINWEB")

banner()

try:

	link = input("\033[33mEnter Your Target Website To Discover Links: ")

	start1 = link.startswith('http')
	start2 = link.startswith('https')
	if(start1 == False or start2 == False):
		link2 = ("https://" + link)
		if(len(link) == 0):
			print(" \n \033[33m Url Undefined")

		else:
			response = requests.get(link2)
			content = response.content
			soup = BeautifulSoup(content, "lxml")
			links = soup.find_all('a')
			for link in links:
				href = link.get('href')
				print("\n\033[91m  Link Found: " + str(href))
				time.sleep(1)

except KeyboardInterrupt as exit:
		sys.exit()
