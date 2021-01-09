import tuShareController

def init(workbook, auto_cell_format, stockID, today_year, today_month, howManyYears):

	dataNeed = [
	# api, field, chinese,
		["income","f_ann_date","公布日期"],
		["income","report_type","报表类型"],
		["income","total_revenue","营业收入"],
		["income","total_cogs","营业成本"],
	]

	incomeFields = ""
	for item in dataNeed:
		if(item[0]=="income"):
			incomeFields = incomeFields + item[1] + ","
	incomeFields = incomeFields[0:-1]

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
	ws_basic.set_column(2, 2, 12)
	ws_basic.set_column(3, 30, 17)

	#################################################
	for i in range(0,howManyYears):
		data_Year = today_year-howManyYears+i+1
		data_Column_ID = chr(ord('D') + i)
		data_Line_Number = 1

		# write the year at the top
		ws_basic.write(str(data_Column_ID)+str(data_Line_Number), str(data_Year), auto_cell_format)
		data_Line_Number += 1

		df_income = mytuShare.getProApi().income(ts_code=stockID, period=str(data_Year)+'1231', fields=incomeFields)

		# write the information from tushare
		print("-----------------------")
		print("year is :"+str(data_Year))
		for item in dataNeed:
			####### header, if the first year ######
			print(item)
			if(i==0):
				ws_basic.write("C"+str(data_Line_Number), str(item[2]), auto_cell_format)


			thisBoxData = 0
			if(item[0]=="income"):
				try:
					thisBoxData = df_income[item[1]][0]
				except:
					pass

			print("this box data is :"+str(thisBoxData))
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


