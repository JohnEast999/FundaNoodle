import xlsxwriter
import general_sheet
import customInput as ci




########### excel part ################
# Create the workbook
wbName = str(ci.codeNumber)+'_autoData.xlsx'

# existingWorksheet = xlsxwriter.workbook.get_worksheet_by_name(wbName) 
workbook = xlsxwriter.Workbook(wbName)

#########  default format ##############
auto_cell_format = workbook.add_format()
auto_cell_format.set_bg_color('#A5E080')
auto_cell_format.set_text_wrap()
auto_cell_format.set_align('vcenter')
auto_cell_format.set_align('left')

######################################################





##########  write worksheet functions ############
######################### 介绍 #############################
def write_Introduce():
	ws_Introduce.write('A1', '绿色背景色信息为程序自动生成信息', auto_cell_format)
	ws_Introduce.write('A2', '重命名并存储，防止程序覆盖你的手工工作 !!!', auto_cell_format)

######################### 概览 #############################




	
######################## 历史估值 ##############################
def write_Price_History():
	# df = pro.query('daily', ts_code=codeNumber, trade_date='20180717')
	# stockPrice = df.close[0]
	# print(stockPrice)

	# totalShare = pro.daily_basic(ts_code=codeNumber, trade_date='20180717',fields='total_share')
	# print(totalShare)

	# ws_Price_History.write('E1', '股价', auto_cell_format)
	# ws_Price_History.write('F1', '股本', auto_cell_format)
	# ws_Price_History.write('G1', '市值（亿）', auto_cell_format)
	pass



######################################################
def write_Finance_Basic():
	ws_Finance_Basic.write('A1', 'No more information', auto_cell_format)



def write_Finance_Recent():
	ws_Finance_Recent.write('A1', 'No more information')

def write_Different_Depart():
	ws_Different_Depart.write('A1', 'No more information')
def write_Receivable_Quality():
	ws_Receivable_Quality.write('A1', 'No more information')
def write_Operation_Compare():
	ws_Operation_Compare.write('A1', 'No more information')
def write_Produce_Ability():
	ws_Produce_Ability.write('A1', 'No more information')
def write_Controller_and_Cs():
	ws_Controller_and_Cs.write('A1', 'No more information')
def write_Holder_Orgnisation():
	ws_Holder_Orgnisation.write('A1', 'No more information')
def write_Holder_Stuff():
	ws_Holder_Stuff.write('A1', 'No more information')
def write_Increase_Issues():
	ws_Increase_Issues.write('A1', 'No more information')
def write_Repurchase():
	ws_Repurchase.write('A1', 'No more information')
def write_Convertible_Bond():
	ws_Convertible_Bond.write('A1', 'No more information')
def write_Stock_Incentive():
	ws_Stock_Incentive.write('A1', 'No more information')

######################################################

######################################################
#############  Create and Write worksheets      ############
######################################################
ws_Introduce = workbook.add_worksheet("介绍")
ws_Introduce.set_column(0,0,100)
write_Introduce()

# ws_General = workbook.add_worksheet("公司概览")
general_sheet.init(workbook, auto_cell_format)

ws_Price_History = workbook.add_worksheet("估值历史")
write_Price_History()
ws_Finance_Basic = workbook.add_worksheet("基础数据")
write_Finance_Basic()
ws_Finance_Recent = workbook.add_worksheet("财务最新")
write_Finance_Recent()
ws_Different_Depart = workbook.add_worksheet("分部报告")
write_Different_Depart()
ws_Receivable_Quality = workbook.add_worksheet("应收质量对比")
write_Receivable_Quality()
ws_Operation_Compare = workbook.add_worksheet("经营指标对比")
write_Operation_Compare()
ws_Produce_Ability = workbook.add_worksheet("产能分析")
write_Produce_Ability()
ws_Controller_and_Cs = workbook.add_worksheet("实控人及高管")
write_Controller_and_Cs()
ws_Holder_Orgnisation = workbook.add_worksheet("机构")
write_Holder_Orgnisation()
ws_Holder_Stuff = workbook.add_worksheet("员工持股")
write_Holder_Stuff()
ws_Increase_Issues = workbook.add_worksheet("增发")
write_Increase_Issues()
ws_Repurchase = workbook.add_worksheet("回购")
write_Repurchase()
ws_Convertible_Bond = workbook.add_worksheet("可转债")
write_Convertible_Bond()
ws_Stock_Incentive = workbook.add_worksheet("股权激励")
write_Stock_Incentive()
######################################################
######################################################
######################################################




# close
workbook.close()