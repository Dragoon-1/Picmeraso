
from PyQt6 import QtCore, QtGui, QtWidgets
import exifread,piexif,sys


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(770, 438)
        Form.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(-126, -162, 1290, 725))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("assets/loading.gif"))
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


        self.movie = QtGui.QMovie("assets/loading.gif")
        self.label.setMovie(self.movie)
        self.movie.start()

        QtCore.QTimer.singleShot(7000, Form.close)
        
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

    def startAnimation(self):
        self.movie.start()
        

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setAutoFillBackground(True)
        self.centralwidget.setStyleSheet("background-image:url(./assets/bg.png)")
        self.centralwidget.setObjectName("centralwidget")
        self.choosebtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.choosebtn.setGeometry(QtCore.QRect(40, 70, 191, 31))
        self.choosebtn.setObjectName("choosebtn")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(250, 70, 521, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.listWidget = QtWidgets.QListWidget(parent=self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(50, 200, 431, 381))
        self.listWidget.setObjectName("listWidget")
        self.showbtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.showbtn.setGeometry(QtCore.QRect(200, 160, 131, 31))
        self.showbtn.setObjectName("showbtn")
        self.delmd = QtWidgets.QPushButton(parent=self.centralwidget)
        self.delmd.setGeometry(QtCore.QRect(580, 300, 151, 41))
        self.delmd.setObjectName("delmd")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.choosebtn.clicked.connect(self.choose_file)
        self.showbtn.clicked.connect(self.showmd)
        self.delmd.clicked.connect(self.delmdta)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.choosebtn.setText(_translate("MainWindow", "Choose File"))
        self.showbtn.setText(_translate("MainWindow", "Show Metadata"))
        self.delmd.setText(_translate("MainWindow", "Delete Metadata"))


    def choose_file(self):
        
        try:            
            self.file_path, _ = QtWidgets.QFileDialog.getOpenFileName(
                self.MainWindow,
                "Select Image",
                "",
                "Images (*.png *.jpg *.jpeg)"
            )
            if self.file_path:
                self.lineEdit.setText(self.file_path)
        except Exception as e:
            QtWidgets.QMessageBox.critical(self.MainWindow, "Error", f"An error occurred:\n{e}")

    def showmd(self):
        
        if not hasattr(self, "file_path") or not self.file_path:
            QtWidgets.QMessageBox.warning(
                self.MainWindow,
                "No File Selected",
                "Please select an image file first."
            )
            return

        self.listWidget.clear()

        try:
            with open(self.file_path, 'rb') as f:
                tags = exifread.process_file(f)

            if not tags:
                QtWidgets.QMessageBox.warning(
                    self.MainWindow,
                    "Metadata",
                    "No metadata found in this image."
                )
                return

            info_list = [f"{x}: {y}" for x, y in tags.items()]
            self.listWidget.addItems(info_list)

        except Exception as e:
            QtWidgets.QMessageBox.warning(
                self.MainWindow,
                "Error",
                f"Failed to read metadata:\n{e}"
            )
    def delmdta(self):
        if not hasattr(self, "file_path") or not self.file_path:
            QtWidgets.QMessageBox.warning(
                self.MainWindow,
                "No File Selected",
                "Please select an image file first."
            )
            return
        try:
            piexif.remove(self.file_path)
            QtWidgets.QMessageBox.warning(
                self.MainWindow,
                "successful",
                "Metadata is removed successfully! you can recheck by clicking show Metadata!"
            )
            return
            
        except:
            QtWidgets.QMessageBox.warning(
                self.MainWindow,
                "Error",
                "Something went wrong Pls try again!"
            )
            return
        
        
        

if __name__ == "__main__":
    

    app = QtWidgets.QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)

    #Ss
    splash = QtWidgets.QWidget()
    splash_ui = Ui_Form()
    splash_ui.setupUi(splash)
    splash.show()

    #mw
    main_window = QtWidgets.QMainWindow()
    main_window.setAttribute(QtCore.Qt.WidgetAttribute.WA_DeleteOnClose)

    main_ui = Ui_MainWindow()
    main_ui.setupUi(main_window)
    main_window.destroyed.connect(app.quit)
    def show_main():
        main_window.show()

        screen = QtWidgets.QApplication.primaryScreen().availableGeometry()
        geo = main_window.frameGeometry()
        geo.moveCenter(screen.center())
        main_window.move(geo.topLeft())

        splash.close()
        
    QtCore.QTimer.singleShot(7000, show_main)

    sys.exit(app.exec())
