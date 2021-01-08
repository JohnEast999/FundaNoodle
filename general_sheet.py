import tuShareLogIn as tsInfo
import customInput as ci


def init(workbook, auto_cell_format):
	ws_General = workbook.add_worksheet("公司概览")
	
	ws_General.set_column(0, 0, 20)
	ws_General.set_column(1, 1, 100)

	df = tsInfo.pro.stock_company(ts_code=ci.codeNumber, fields='exchange,chairman,manager,province, city, introduction, website, employees, main_business, business_scope')
	#exchange = df.exchange[0]

	ws_General.write('A1', '法人', auto_cell_format)
	ws_General.write('B1', df.chairman[0], auto_cell_format)

	ws_General.write('A2', '总经理', auto_cell_format)
	ws_General.write('B2', df.manager[0], auto_cell_format)

	ws_General.write('A3', '省', auto_cell_format)
	ws_General.write('B3', df.province[0], auto_cell_format)

	ws_General.write('A4', '市', auto_cell_format)
	ws_General.write('B4', df.city[0], auto_cell_format)

	ws_General.write('A5', '介绍', auto_cell_format)
	ws_General.write('B5', df.introduction[0], auto_cell_format)

	ws_General.write('A6', '网站', auto_cell_format)
	ws_General.write('B6', df.website[0], auto_cell_format)

	ws_General.write('A7', '员工数', auto_cell_format)
	ws_General.write('B7', df.employees[0], auto_cell_format)

	ws_General.write('A8', '主营业务', auto_cell_format)
	ws_General.write('B8', df.main_business[0], auto_cell_format)

	ws_General.write('A9', '经营范围', auto_cell_format)
	ws_General.write('B9', df.business_scope[0], auto_cell_format)