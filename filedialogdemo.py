# filedialogdemo.py
# author: Eric Perry 10/19/20

from breezypythongui import EasyFrame
import tkinter.filedialog

class FileDialogDemo(EasyFrame):
	# demonstrated the use of a file dialog.
	def __init__(self):
		# sets up the window and the widget
		EasyFrame.__init__(self, title = "File Dialog Demo")
		self.outputArea = self.addTextArea(text = "", row = 0, column = 0, width = 80, height = 15)
		self.addButton(text = "Open", row = 1, column = 0, command = self.openFile)

	# event handling method
	def openFile(self):
		# pops up an open file dialog, and if a file is selected, displays its text in the text are and its path name in the title bar of the window.
		fList = [("Python files", "*.py"), ("Text files", "*.txt")]
		fileName = tkinter.filedialog.askopenfilename(parent = self, filetypes = fList)

		# if the filename is NOT just an empty string, open the file contents, set the text of the text area and update the title of the window
		if fileName != "":
			file = open(fileName, "r")
			text = file.read()
			file.close()
			self.outputArea.setText(text)
			self.setTitle(fileName)

# definition of the main() function
def main():
	FileDialogDemo().mainloop()

main()