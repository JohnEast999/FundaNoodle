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

		self.entrythingy3 = tk.Entry()
		self.entrythingy3.pack()

		# Create the application variable.
		self.contents_token = tk.StringVar()
		self.contents_codeID = tk.StringVar()
		self.contents_whoManyYears = tk.StringVar()
		##############################################
		self.contents_token.set("7b0b361e9a9ecc76e360cfb5b9dd014a45a8138263a7b0c5f6cdfeb4")
		self.entrythingy["textvariable"] = self.contents_token

		self.contents_codeID.set("000001.SZ")
		self.entrythingy2["textvariable"] = self.contents_codeID

		self.contents_whoManyYears.set("7")
		self.entrythingy3["textvariable"] = self.contents_whoManyYears


		self.entrythingy.bind('<Key-Return>',
							 self.submit)
		self.entrythingy2.bind('<Key-Return>',
							 self.submit)
		self.entrythingy3.bind('<Key-Return>',
							 self.submit)


	def submit(self, event):
		token = self.contents_token.get()
		stockID = self.contents_codeID.get()
		howManyYears = int(self.contents_whoManyYears.get())

		generator = generate_excel.generator()
		generator.generateExcel(token, stockID, howManyYears)