from da import DA
from widget import App
from PyQt5.QtWidgets import QApplication
import sys

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = App()
	ex.show()
	sys.exit(app.exec())
 

