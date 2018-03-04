"""Bot_REdditGathererOfData = Bot_REGOD
created by:
u/RosonTech
on:
shit, what's today's date?
....umm....
Oh yesh!
2018-March-2. 19:56"""
"""import praw
import time
"""

#Declaring the Bot to Reddit:
#bot =

#Open File:
fileObj = open("Subreddits", 'r')
subredditsBuffer = fileObj.read()
subredditsList = []
listBuffer = []
for i in subredditsBuffer:
	if (i == '\n'):
		subredditAppender = ''.join(listBuffer)
		subredditsList.append(subredditAppender)
		listBuffer = []
	else:
		listBuffer.append(i)
#A list called subredditsList has been created that has the list of the top 100 subreddits

dictionaryBuffer = 
