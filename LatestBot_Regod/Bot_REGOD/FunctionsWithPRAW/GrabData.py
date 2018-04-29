import sys
#import PRAW
from datetime import datetime as dt



#__START__(grabData)
def grabData(subRNum, firstTimeChk = None):
	"""
	declare Bot to Reddit

	"""
	count = 0

	for post in bot.subreddit(subRList[subRNum]).top('hour'):
		count += 1
		postVars = vars(post)
		CurrentTime = dt.now()

		popularity = popularityIndex(int(postVars['ups']), int(postVars['downs']), int(postVars['num_comments']))

		subRFileObj = open("SubredditData/"+str(subRNum), "a")

		"""
		$CurTime.postID.popularity$
		"""
		subRFileObj.write("$"+str(CurrentTime) +"."+ str(postVars['id']) +"."+ str(popularity) + "$\n")
		# $CurTime.postID.popularity$ #
		subRFileObj.close()

		os.remove("MainDataTrack")
		mainFileObj = open("MainDataTrack", "w+")
		"""
		$	~T1$~
		SubRedditNumber
		CurrentTime
		Count
		$
		"""
		if (firstTimeChk != None):
			mainFileObj.write("$T1$\n"+str(subRCounter)+"\n"+str(CurrentTime)+"\n"+str(count)+"\n$")
		else:
			mainFileObj.write("$\n"+str(subRCounter)+"\n"+str(CurrentTime)+"\n"+str(count)+"\n$")
		mainFileObj.close()

		if (count>5):
			return
#__ENDIF__(grabData)
