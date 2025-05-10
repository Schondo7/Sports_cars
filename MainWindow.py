import os
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsPixmapItem
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from SportsCars.sports_gui import Ui_Sportscars

class MainWindow(QMainWindow, Ui_Sportscars):
    '''This Class defines the setup for the GUI interface and controls the inputs that are available'''
    def __init__(self):
        super().__init__()
        self.setupUi(self)


        self.Color.addItems(["Red", "Blue", "Green", "Yellow", 'Purple'])
        self.RacingStripe.addItems(["None", "White", "Black", "Red", "Blue"])
        self.Car.addItems(["Corvette", "Mustang", "Porsche", "Camaro"])


        self.Submit.clicked.connect(self.on_submit)

    def on_submit(self):
''' This function takes the choices made by the user and assigns it to a certain image'''
        selected_color = self.Color.currentText()
        selected_stripe = self.RacingStripe.currentText()
        selected_car = self.Car.currentText()

        image_name = f"{selected_car}_{selected_color}_{selected_stripe}.png"
        image_path = local_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(local_dir, "images", image_name)
# images were generated using chatgpt
        scene = QGraphicsScene()

        if os.path.exists(image_path):
            pixmap = QPixmap(image_path)
            item = QGraphicsPixmapItem(pixmap)
            scene.addItem(item)
            self.graphicsView.setScene(scene)
            self.graphicsView.fitInView(item, Qt.AspectRatioMode.KeepAspectRatio)
        print(f"image: {image_path}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())