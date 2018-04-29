import sys
from datetime import datetime as dt

sys.path.append("/home/CerealBlue/Desktop/Bot_REGOD/Bot_REGOD/FunctionsThatCompensate/CompensateData/CompensateExecute")

from CompensateExecute import compensateExecute

#__START__(compensateData)
def compensateData(previousTime, previousSubRNumber, previousCount):
	FMT = '%Y-%m-%d %H:%M:%S.%f'

	previousSubRNumberConst = previousSubRNumber

	nowTime = dt.now()
	timeDiff = nowTime - dt.strptime(previousTime, FMT)

	trailBy = (timeDiff/35.5) + 1
	remainTime = timeDiff % 35.5

	compensateList = []

	#If the previous count is less than 3, we've got to extract data for the previousSubR again
	if (previousCount < 3):
		trailBy += 1
		compensateList.append(previousSubRNumber)
	#If the previous count is less than 3, we've got to extract data for the previousSubR again
	bufferSubRNumber = 1
	timeExecute = 0

	#If the SubR's lost could be retrived within the amount of time left for the next data extraction
	if ( (remainTime/(trailBy)) > 5.25):
		timeExecute = float("{0:.2f}".format(remainTime/trailBy))
		while (trailBy > 0):
			compensateList.append(previousSubRNumber + bufferSubRNumber)
			bufferSubRNumber += 1
			trailBy -= 1
		#COMPENSATE LIST IS EXECUTED
		compensateExecute(compensateList, timeExecute)
		print ("CompensateLayer1 Over. Proceed to INfINLOUP")
		return True
	#If the SubR's lost could be retrived within the amount of time left for the next data extraction

	chkCurExec = 0 #Current SubR to be Executed has been datacized - checker
	remainTimeVar = remainTime

	#Prgm Opens, but very less time to compensate, hence is required to keep on track
	if (remainTime < 5.25):
		if (previousCount < 3):
			compensateExecute(trailBy - 1, remainTime)
		else:
			compensateExecute(trailBy, remainTime)
		chkCurExec = 1
		remainTimeVar = 35.5
	#Prgm Opens, but very less time to compensate, hence is required to keep on track

	trailByCounter = trailBy
	trailByRealTimeDetect = 0 #during the process, if a current SubR is going to be interrupted, It needs to be added to the list

	#Now, the rest begins:
	while (True):
		if ( (previousSubRNumber + bufferSubRNumber) > 99):
			previousSubRNumber = 0
		compensateList.append(previousSubRNumber + bufferSubRNumber)
		bufferSubRNumber += 1
		trailByCounter -= 1
		remainTimeVar -= 5

		if (remainTimeVar < 10.5):
			if (chkCurExec == 1):
				if ( (previousSubRNumber + bufferSubRNumber) > 99):
					if (previousSubRNumber != previousSubRNumberConst):
						compensateList.append(previousSubRNumberConst + bufferSubRNumber)
					else:
						previousSubRNumber = 0
						compensateList.append(previousSubRNumber + bufferSubRNumber)
				bufferSubRNumber += 1
				trailByCounter -= 1
			else:
				deletor = 0
				if ( (previousSubRNumber + trailBy + trailByRealTimeDetect) > 99):
					deletor = 100
				compensateList.append(previousSubRNumber + trailBy + trailByRealTimeDetect - deletor)
				trailByRealTimeDetect += 1

			timeExecute = 5
			compensateExecute(compensateList, timeExecute)
			remainTimeVar = 35.5
			compensateList = []
			if (trailByCounter == 0):
				print ("Completed CompensateData")
				return
		#Loup Exiting eef Condizion
		if (trailByCounter == 0):
			compensateList.append(previousSubRNumber + trailBy + trailByRealTimeDetect)
			timeExecute = float("{0:.2f}".format(remainTimeVar/(len(compensateList))
			compensateExecute(compensateList, timeExecute)
			print ("Completed CompensateData")
			return
#__ENDIF__(compensateData)
