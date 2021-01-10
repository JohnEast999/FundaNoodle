import tuShareController

def init(workbook, auto_cell_format, stockID, today_year, today_month, howManyYears):

	dataNeed = [
	# api, field, chinese,

		# ["income","f_ann_date","公布日期"],
		# ["income","report_type","报表类型"],
		# ["income","total_revenue","营业收入"],
		# ["income","total_cogs","营业成本"],
		# ["income","sell_exp","销售费用"],
		# ["income","admin_exp","管理费用"],
		["income","fin_exp","财务费用"],
		# ["fina_indicator","rd_exp","研发费用"],
		# ["income","n_income","净利润"],
		# ["fina_indicator","profit_dedt","扣非净利润"],
		# ["cashflow","n_cashflow_act","经营活动产生现金流"],
		# ["cashflow","c_paid_goods_s","购买商品、接受劳务支付的现金"],
		# ["cashflow","c_paid_to_for_empl","为职工支付的现金"],
		# ["cashflow","c_paid_for_taxes","支付的各项税费"],
		# ["fina_audit","audit_result","审计结果"],
		# ["fina_audit","audit_fees","审计总费用"],
		["fina_audit","audit_agency","会计事务所"],
		["fina_audit","audit_sign","签字会计师"],
	]

	incomeFields = ""
	fina_indicatorFields = ""
	cashflowFields = ""
	balancesheetFields = ""
	fina_auditFields = ""

	for item in dataNeed:
		if(item[0]=="income"):
			incomeFields = incomeFields + item[1] + ","
		elif(item[0] == "fina_indicator"):
			fina_indicatorFields = fina_indicatorFields + item[1] + ","
		elif(item[0] == "cashflow"):
			cashflowFields = cashflowFields + item[1] + ","
		elif(item[0] == "balancesheet"):
			balancesheetFields = balancesheetFields + item[1] + ","
		elif(item[0] == "fina_audit"):
			fina_auditFields = fina_auditFields + item[1] + ","

	incomeFields = incomeFields[0:-1]
	fina_indicatorFields = fina_indicatorFields[0:-1]
	cashflowFields = cashflowFields[0:-1]
	balancesheetFields = balancesheetFields[0:-1]
	fina_auditFields = fina_auditFields[0:-1]

	ws_basic = workbook.add_worksheet("基础数据")
	mytuShare = tuShareController.Tushare()

	ws_basic.set_column(0, 0, 2)

	merge_format = workbook.add_format({
		'bold':     True,
		'border':   6,
		'align':    'center',
		'valign':   'vcenter',
		'fg_color': '#D7E4BC',
	})
	
	######### column width ###########
	ws_basic.set_column(1, 1, 3)
	ws_basic.set_column(2, 2, 20)
	ws_basic.set_column(3, 30, 20)

	#################################################
	for i in range(0,howManyYears):
		data_Year = today_year-howManyYears+i+1
		data_Column_ID = chr(ord('D') + i)
		data_Line_Number = 1

		# write the year at the top
		ws_basic.write(str(data_Column_ID)+str(data_Line_Number), str(data_Year), auto_cell_format)
		data_Line_Number += 1

		####################################################
		df_income = []
		if(incomeFields!=""):
			df_income = mytuShare.getProApi().income(ts_code=stockID, period=str(data_Year)+'1231', fields=incomeFields)

		df_fina_indicator = []
		if(fina_indicatorFields!=""):
			df_fina_indicator = mytuShare.getProApi().query('fina_indicator', ts_code=stockID, period=str(data_Year)+'1231', fields=fina_indicatorFields)

		df_cashflow = []
		if(cashflowFields!=""):
			df_cashflow = mytuShare.getProApi().cashflow(ts_code=stockID, period=str(data_Year)+'1231', fields=cashflowFields)

		df_balancesheet = []
		if(balancesheetFields!=""):
			df_balancesheet = mytuShare.getProApi().balancesheet(ts_code=stockID, period=str(data_Year)+'1231', fields=balancesheetFields)

		df_fina_audit = []
		if(fina_auditFields!=""):
			df_fina_audit = mytuShare.getProApi().fina_audit(ts_code=stockID, period=str(data_Year)+'1231', fields=fina_auditFields)
		####################################################

		# write the information from tushare
		for item in dataNeed:
			####### header, if the first year ######
			if(i==0):
				ws_basic.write("C"+str(data_Line_Number), str(item[2]), auto_cell_format)


			thisBoxData = 0
			item_Api = item[0]
			df_choose = []

			if(item_Api=="income"):
				df_choose = df_income
			elif(item_Api=="fina_indicator"):
				df_choose = df_fina_indicator
			elif(item_Api=="cashflow"):
				df_choose = df_cashflow
			elif(item_Api=="balancesheet"):
				df_choose = df_balancesheet
			elif(item_Api=="fina_audit"):
				df_choose = df_fina_audit
			
			try:
				thisBoxData = df_choose[item[1]][0]
			except:
				thisBoxData = "No Data"
				
			ws_basic.write(str(data_Column_ID)+str(data_Line_Number), thisBoxData, auto_cell_format)
			data_Line_Number += 1




	# #########  header column ####################
	# ws_basic.merge_range('B2:B3', '1', merge_format)
	# ws_basic.write('C2', "营业收入", auto_cell_format)
	# ws_basic.write('C3', "同比增长", auto_cell_format)

	# ws_basic.write('B5', "2", merge_format)
	# ws_basic.write('C5', "毛利率", auto_cell_format)

	# ws_basic.merge_range('B7:B8', '3', merge_format)
	# ws_basic.write('C7', "销售费用", auto_cell_format)
	# ws_basic.write('C8', "同比增长", auto_cell_format)


