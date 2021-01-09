import tuShareController

def init(workbook, auto_cell_format, stockID, today_year, today_month, howManyYears):
	###  接口名称，中文描述
	dataFields_Income_Api = [["f_ann_date","公布日期"], ["report_type","报表类型"], ["total_revenue","营业收入"], ["total_cogs","营业成本"]]



	ws_basic = workbook.add_worksheet("基础数据")
	mytuShare = tuShareController.Tushare()
	df = mytuShare.getProApi().income(ts_code=stockID, period=str(today_year-3)+'1231', fields='f_ann_date,report_type,total_revenue,revenue,total_cogs')

	print("1 ===")
	print(df["f_ann_date"])
	print("2 ===")
	print(df.f_ann_date[0])

	ws_basic.set_column(0, 0, 2)
	

	print("today_year is "+str(today_year))
	print("today_month is "+str(today_month))

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
		ws_basic.write(str(data_Column_ID)+"1", str(data_Year), auto_cell_format)


	#########  header column ####################
	ws_basic.merge_range('B2:B3', '1', merge_format)
	ws_basic.write('C2', "营业收入", auto_cell_format)
	ws_basic.write('C3', "同比增长", auto_cell_format)

	ws_basic.write('B5', "2", merge_format)
	ws_basic.write('C5', "毛利率", auto_cell_format)

	ws_basic.merge_range('B7:B8', '3', merge_format)
	ws_basic.write('C7', "销售费用", auto_cell_format)
	ws_basic.write('C8', "同比增长", auto_cell_format)


