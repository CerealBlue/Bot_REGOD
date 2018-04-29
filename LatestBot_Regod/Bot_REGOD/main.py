
import sys

sys.path.append("/home/sudheendra_raghav/Desktop/Bot_REGOD/Bot_REGOD/FirstTimeDataCollect")
sys.path.append("/home/sudheendra_raghav/Desktop/Bot_REGOD/Bot_REGOD/FunctionsThatCompensate")

from FirstTime import firstTime
from CompensateControl import compensateControl as compensate

def main():
	fileObj1 = open("filesREGOD/dataREGOD", "r") #change to mainDataTrack
	fileObj1.seekg(0)
	firstChar = fileObj.read(1)
	fileObj1.close()

	if not firstChar:
		firstTime()
		InfinLoup()

	compensate()
	InfinLoup()
