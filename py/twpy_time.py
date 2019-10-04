def display_seconds(secondNum):
	"""根据秒数显示标准的时间间隔。

	Args:
		secondNum: 秒数，正整数。
	Returns:
		convertStr: 将秒数换算成易懂的时间间隔字符串。
	"""
	secondStr = str(secondNum % 60)[:5]
	convertStr = secondStr+'s '
	if secondNum > 59:
		minuteNum = secondNum // 60
		minuteStr = str(minuteNum % 60)
		convertStr = minuteStr + 'm ' + convertStr
		if minuteNum > 59:
			hourNum = minuteNum // 60
			hourStr = str(hourNum % 24)
			convertStr = hourStr + 'h ' + convertStr
			if hourNum > 23:
				dayNum = hourNum // 24
				convertStr = str(dayNum) + 'd ' + convertStr
	return convertStr
	
