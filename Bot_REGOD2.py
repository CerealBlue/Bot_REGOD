"""Bot_REdditGathererOfData = Bot_REGOD
created by:
u/RosonTech
on:
shit, what's today's date?
....umm....
Oh yesh!
2018-March-2. 19:56"""

"""import praw"""
import time

#Functions:
def popularity(ups, downs, numComments):
    if ((ups+downs) > numComments):
        return ups+downs
    return numComments

def delayFunc():
    time.sleep(35.5)


#Declaring the Bot to Reddit:
#bot = I ain't putting this here


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
#Close File
fileObj.close()

dictionaryBuffer = {}

#Create Dictionary Buffer's File/Open it
fileObj2 = open("dictionaryBufferFile", 'w+')
fileObj2.seekg(0)
character1 = fileObj.read(1)

#This is the first time the program is ever running
if not character1:
    fileObj2.seekg(0)
    for i in subredditsList:
        count = 0
        for post in bot.subreddit(i).top('hour'):
            count += 1
            postVariables = vars(post)
            displayValue = popularity(int(postVariables['ups']), int(postVariables['downs']), int(postVariables['num_comments']))
            #SubR, CurrentTime, ID, Popularity 
            fileObj2.write(str(i), str(time.asctime(time.localtime( time.time() ) )), str(postVariables['id']), str(displayValue), "\n",  sep="/")
            if (count > 5):
                break
            delayFunc()
        print ("1.Finish:\t", str(i))
    print ("Finish First Analysis")
