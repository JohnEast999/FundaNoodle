import tkinter as tk
import generate_excel

class App(tk.Frame):
	def __init__(self, master):
		super().__init__(master)
		self.pack()

		self.entrythingy = tk.Entry()
		self.entrythingy.pack()

		self.entrythingy2 = tk.Entry()
		self.entrythingy2.pack()

		# Create the application variable.
		self.contents_token = tk.StringVar()
		self.contents_codeID = tk.StringVar()
		##############################################
		self.contents_token.set("e28c79162bc5a6fd505e5183c7d9fe45ef6fb84c2eef01b8b25bf5")
		self.entrythingy["textvariable"] = self.contents_token

		self.contents_codeID.set("000001.SZ")
		self.entrythingy2["textvariable"] = self.contents_codeID


		self.entrythingy.bind('<Key-Return>',
							 self.submit)
		self.entrythingy2.bind('<Key-Return>',
							 self.submit)


	def submit(self, event):
		token = self.contents_token.get()
		stockID = self.contents_codeID.get()
		print("token is "+str(token))
		print("stockID is "+str(stockID))

		generator = generate_excel.generator()
		generator.generateExcel(token, stockID)