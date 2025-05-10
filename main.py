import sys
from PyQt6.QtWidgets import QApplication
from MainWindow import MainWindow   # import your class

def run_sports_main():
    '''This runs the main GUI for the game car choice'''
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    run_sports_main()