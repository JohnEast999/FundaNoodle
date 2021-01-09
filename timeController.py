from datetime import date

class Mytime():
	@classmethod
	def init(cls):
		cls.today = date.today().strftime("%d/%m/%Y")
		cls.dateInfo = cls.today.split('/')
		cls.today_year = cls.dateInfo[2]
		cls.today_month = cls.dateInfo[1]
		cls.today_day = cls.dateInfo[0]
		
	@classmethod
	def getTodayYear(cls):
		return cls.today_year
	@classmethod
	def getTodayMonth(cls):
		return cls.today_month
	@classmethod
	def getTodayDay(cls):
		return cls.today_day