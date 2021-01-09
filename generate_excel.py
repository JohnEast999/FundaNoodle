import xlsxwriter
import tuShareController
import timeController
import general_sheet
import introduce_sheet
import basic_financial_sheet

##123
# 介绍
# 公司概览  
# 估值历史
# 基础数据
# 财务最新
# 分部报告
# 应收质量对比
# 经营指标对比
# 产能分析
# 实控人及高管
# 机构
# 员工持股
# 增发
# 回购
# 可转债
# 股权激励
##


class generator():
	def generateExcel(self, token, stockID, howManyYears):
		######## login Tushare  ################
		myTushare = tuShareController.Tushare()
		myTushare.login(token)

		####### init time ###################
		myTime = timeController.Mytime()
		myTime.init()
		today_year = int(myTime.getTodayYear())
		today_month = int(myTime.getTodayMonth())

		######## generate book ###################
		wbName = str(stockID)+'_autoData.xlsx'
		workbook = xlsxwriter.Workbook(wbName)
		auto_cell_format = workbook.add_format()
		auto_cell_format.set_bg_color('#A5E080')
		auto_cell_format.set_text_wrap()
		auto_cell_format.set_align('vcenter')
		auto_cell_format.set_align('left')

		######### generate sheets  ########################
		introduce_sheet.init(workbook, auto_cell_format, stockID) # 介绍
		general_sheet.init(workbook, auto_cell_format, stockID)   # 公司概览
		pass 														  # 估值历史
		basic_financial_sheet.init(workbook, auto_cell_format, stockID, today_year, today_month, howManyYears) # 基础数据


		

		######################################################
		######
		######
		######   close workbook ########
		workbook.close()