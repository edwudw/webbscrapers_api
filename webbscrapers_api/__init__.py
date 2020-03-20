import requests
from datetime import datetime
from typing import List

def getReports(startDateTime: datetime, endDateTime: datetime, keyTerms: List[str]=[], location: str='', timezone: str=None):
	newStartTime = datetime(startDateTime.year, startDateTime.month, startDateTime.day, startDateTime.hour, startDateTime.minute, startDateTime.second)
	newEndTime = datetime(endDateTime.year, endDateTime.month, endDateTime.day, endDateTime.hour, endDateTime.minute, endDateTime.second)
	payload = {
		'startDateTime': newStartTime.isoformat(),
		'endDateTime': newEndTime.isoformat(),
		'keyTerms': ','.join(keyTerms),
		'location': location,
		'timezone': timezone
	}
	return requests.get('https://webbscrapers.live/reports', params=payload).json()