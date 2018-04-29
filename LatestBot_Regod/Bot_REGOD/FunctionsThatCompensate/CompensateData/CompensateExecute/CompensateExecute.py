import sys

sys.path.append("/home/CerealBlue/Desktop/Bot_REGOD/Bot_REGOD/FunctionsWithPRAW")
sys.path.append("/home/CerealBlue/Desktop/Bot_REGOD/Bot_REGOD/FunctionsWithTime/DelayFunc")

from GrabData import grabData
from DelayFunc import delayFunc

#__START__(compensateExecute)
def compensateExecute(compensateList, timeExecute):
	for subRNum in compensateList:
		grabData(subRNum)
		delayFunc(timeExecute-0.25)
#__ENDIF__(compensateExecute)
