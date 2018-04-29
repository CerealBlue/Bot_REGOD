import sys

sys.path.append("/home/CerealBlue/Desktop/Bot_REGOD/Bot_REGOD/FunctionsWithPRAW")
sys.path.append("/home/CerealBlue/Desktop/Bot_REGOD/Bot_REGOD/FunctionsWithTime/DelayFunc")

from GrabData import grabData
from DelayFunc import delayFunc

#__START__(firstTime)
def firstTime():
	mainFileObjT1 = open("MainDataTrack", "w+")
	mainFileObjT1.write("$TIME1$\n")
	mainFileObjT1.close()

	for i in range(0,100,1):

		grabData(i, 1)
		delayFunc()

		print ("Finished Subreddit:\t", subR, "\n")

	print ("\nFinished TIME#1\n")
#__ENDIF__(firstTime)
