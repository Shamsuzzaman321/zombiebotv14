import sys
red = '\033[91m'
green = '\033[92m'
white = '\033[00m'

get = open(raw_input("Give Me List: "), "r").read().splitlines()

liste = []
try:
	for sites in get:
		dhon = sites
		sites = sites.replace("https://", "")
		sites = sites.replace("http://", "")
		sites = sites.replace("www.", "")
		sites = sites.split("/")
		sites = sites[0]
		if sites not in liste:
			liste.append(sites)
			open("Result/Cleannoduplacted.txt", "a").write('info@'+dhon + "\n")
			print("Finished, success , Thank you for using Viper1337 Tool --> Result/Cleannoduplacted")
except:
	pass