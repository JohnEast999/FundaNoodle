import UI
import tkinter as tk


def main():
	# generate UI
	root = tk.Tk()
	myapp = UI.App(root)
	myapp.mainloop()

if __name__ == "__main__":
    main()