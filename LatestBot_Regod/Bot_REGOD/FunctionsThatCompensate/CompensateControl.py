import sys

sys.path.append("/home/CerealBlue/Desktop/Bot_REGOD/Bot_REGOD/FunctionsThatCompensate/CalculateTimeDiff")
sys.path.append("/home/CerealBlue/Desktop/Bot_REGOD/Bot_REGOD/FunctionsThatCompensate/CompensateData")
sys.path.append("/home/CerealBlue/Desktop/Bot_REGOD/Bot_REGOD/FunctionsWithTime/DelayFunc")

from CalculateTimeDiff import calculateTimeDiff as cTD
from CompensateData import compensateData as cD
from DelayFunc import delayFunc

#__START__(TimeLag)
def compensateControl():
	#To Get Last Recorded Time
	#Cond1: If firstTime() has not been completed
	mainFileObj = open("MainDataTrack", "r")
	previousData = mainFileObj.read()
	mainFileObj.close()

	#TIME ONE DIDN'T DELETE
	if (previousData[0:7] == "$TIME1$"):
		print ("ERROR#1:\tHAVEN'T COLLECTED ONE DATA AFTER TIME1. MUST RESTART")
		quit()

	#TIME ONE DIDN'T COMPLETE
	if (previousData[0:4] == "$T1$"):
		print ("ERROR#2:\tDATA SET:\"TIME1\" IS INCOMPLETE. MUST RESTART")
		quit()

	#<Previous Data Holders>
	dataSetBuffer = []
	previousSubRNumber = []
	previousTime = []
	previousCount = []
	loopCounter = 0
	#Extract Data To <Previous Data Holders>
	for character in previousData:
		if (character != '$'):
			dataSetBuffer.append(character)
		else:
			if (len(dataSetBuffer) != 0):
				if (loopCounter == 0):
					previousSubRNumber = ''.join(dataSetBuffer)
					loopCounter += 1
					dataSetBuffer = []
				elif (loopCounter == 1):
					previousTime = ''.join(dataSetBuffer)
					loopCounter += 1
					dataSetBuffer = []
				else:
					previousCount = ''.join(dataSetBuffer)
					break

	previousSubRNumber = int(previousSubRNumber)
	previousCount = int(previousCount)

	proceed = cTD(previousTime)

	if (proceed == False):
		cD(previousTime, previousSubRNumber, previousCount)
	else:
		delayFunc(proceed)

#__ENDIF__(TimeLag)
