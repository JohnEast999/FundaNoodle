
import tushare as ts

class Tushare():
	@classmethod
	def login(cls, token):
		# print("tusare login once!!!")
		ts.set_token(token)
		cls.pro = ts.pro_api(token)
		
	@classmethod
	def getProApi(cls):
		return cls.pro

	