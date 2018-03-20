"""Bot_REdditGathererOfData = Bot_REGOD
created by:
u/RosonTech
on:
shit, what's today's date?
....umm....
Oh yesh!
2018-March-2. 19:56"""

"""import praw"""
def main():
	fileObj1 = open("~~~dataREGOD~~~~", "r")
	fileObj1.seekg(0)
	firstChar = fileObj.read(1)

	skip = 0

	if not firstChar:
		firstTime()
		skip = 1
	fileObj1.close()

	if (skip == 0):
		TimeLag()



#__START__(firstTime)
def firstTime(subRList):
	dataREGODFileObj = open("~~~dataREGOD~~~", "w+")
	
	for subR in subRList:
		subRCounter = 0
		
		for post in bot.subreddit(subR).top('hour'):
			subRCounter += 1
			postVars = vars(post)

			popularity = popularityIndex(int(postVars['ups']), int(postVars['downs']), int(postVars['num_comments']))

			# $SubR.CurTime.postID.popularity$ #
			dataREGODFileObj.write("$" + str(i) + "." + str(timeNow()) +"." + str(postVars['id']) +"." + str(popularity) + "$\n")

			if (count>5):
				break
			
			delayFunc()
		
		print ("Finished Subreddit:\t", subR, "\n")

	print ("Finished TIME#1")
	dataREGODFileObj.close()
#__ENDIF__(firstTime)

#__START__(TimeLag)
def TimeLag():	
	dataREGODFileObj = open("~~~dataREGOD~~~", "a")	
	
	#To Get Last Recorded Time
	condition = True
	counter = 0

	while (condition):
		dataREGODFileObj.seekg(-2)
		char= dataREGODFileObj.read(1)

		if(char == '.'):
			counter += 1

		if (counter == 3):
			condition = False

	condition = True
	previousTimeList = []

	while (condition):
		char = dataREGODFileObj.read(1)

		if (char == '.'):
			condition = False
			break

		previousTimeList.append(char)

	dataREGODFileObj.close()
	
	previousTime = ''.join(previousTimeList)
	
	proceed = calculateTimeDiff(previousTime)

	if (proceed == False):
		compensateData()
	else:
		delayFunc(proceed)
		#MAKe InfIn Looup hear		
		

#__ENDIF__(TimeLag)

#__START__(calculateTimeDiff)
def calculateTimeDiff(lastTime):
	FMT ='%Y-%m-%d %H:%M:%S.%f'
	
	nowTime = timeNow()
	timeDiff = nowTime - datetime.datetime.strptime(lastTime, FMT)
	
	print ("\nSince last time, '", str(timeDiff), "' time has been elapsed.\n")

	if ( int(timeDiff.total_seconds()) <= 35.5 ):
		return (35.5 - (int(timeDiff.total_seconds()) )
	else:
		return (False)
#__ENDIF__(calculateTimeDiff)

#__START__(compensateData)
def compensateData(lastTime, subRList):
	FMT = '%Y-%m-%d %H:%M:%S.%f'
	
	nowTime = timeNow()
	timeDiff = nowTime - datetime.datetime.strptime(lastTime, FMT)

	trailBy = timeDiff/35.5
	remainTime = timeDiff % 35.5

	#If the SubR's lost could be retrived within the amount of time left for the next data extraction
	if ( (remainTime/(trailBy+1)) > 5.25):
		compensateList = []
		dataREGODFileObj = open("~~~DataREGOD~~~", "r")
		
	


#__ENDIF__(compensateData)






if __name__ == "__main__": main()
