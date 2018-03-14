import bs4
from urllib import urlopen as uReq
from bs4 import BeautifulSoup as Bsoup

my_url = 'https://www.redditmetrics.com/top '

#List of the subreddits
subreddits = []

#Opening the connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
#Connection Closed

#Parsing the HTML Reddit/Subreddit
soup = Bsoup(page_html, 'html.parser')
paras = soup.find(attrs= {'table'})
count = 0

print paras
paras2 = str(paras)

file_obj = open("Params", 'w')
file_obj.write(paras2)
file_obj.close()

fileObj = open("Params", 'r')
params = fileObj.read()
i = 0
listo = []

for i in range(0,len(params),1):
	if (params[i] == ">"):
		if (params[i+1:i+4] == "/r/"):
			count += 1
			countiz = i+3
			tempolisto = []
			while (params[countiz] != "<"):
				countiz += 1
				tempolisto.append(params[countiz])
			tempolisto.remove("<")
			stri = ''.join(tempolisto)
			stri = stri.lower()
			listo.append(stri)

fileObj.close()
print listo
print str(count)+"\n\n\n"

newFile = open("Subreddits", 'w')

for i in listo:
	print i
	newFile.write(str(i)+"\n")

#END
