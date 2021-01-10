def init(workbook, auto_cell_format, stockID):
	ws_Introduce = workbook.add_worksheet("财务数据 最新")
	ws_Introduce.set_column(0,0,100)
	
	ws_Introduce.write('A1', '绿色背景色信息为程序自动生成信息', auto_cell_format)
	ws_Introduce.write('A2', '重命名并存储，防止程序覆盖你的手工工作 !!!', auto_cell_format)