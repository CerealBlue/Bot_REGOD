from datetime import datetime as dt

#__START__(calculateTimeDiff)
def calculateTimeDiff(lastTime):
	FMT ='%Y-%m-%d %H:%M:%S.%f'

	nowTime = dt.now()
	timeDiff = nowTime - dt.strptime(lastTime, FMT)

	print ("\nSince last time, '", str(timeDiff), "' time has been elapsed.\n")

	if ( int(timeDiff.total_seconds()) <= 35.5 ):
		return (35.5 - (int(timeDiff.total_seconds()) )
	else:
		return (False)
#__ENDIF__(calculateTimeDiff)
