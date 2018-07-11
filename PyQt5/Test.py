import sys
from PyQt5 import QtGui, QtWidgets, QtCore

class Window(QtWidgets.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle('Convert')
        self.setWindowIcon(QtGui.QIcon(r'C:\Users\corey\Corey-All-\R3dHand\redHand\Logo\R3dHand_Logo.png'))

        extractAction = QtWidgets.QAction("&Exit", self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip('Leave The App')
        extractAction.triggered.connect(self.close_application)

#S        openEditor = QtWidgets.QAction("&Editor", self)
#S        openEditor.setShortcut("Ctrl+E")
#S        openEditor.setStatusTip('Open Editor')
#S        openEditor.triggered.connect(self.editor)

        openFile = QtWidgets.QAction("&Open File", self)
        openFile.setShortcut("Ctrl+O")
        openFile.setStatusTip('Open File')
        openFile.triggered.connect(self.file_open)

        saveFile = QtWidgets.QAction("&Save File", self)
        saveFile.setShortcut("Ctrl+S")
        saveFile.setStatusTip('Save File')
        saveFile.triggered.connect(self.file_save)

        closeEditor = QtWidgets.QAction("&Close Editor", self)
        closeEditor.setShortcut("Ctrl+X")
        closeEditor.setStatusTip('Close Editor')
        closeEditor.triggered.connect(self.editor_close)

        self.statusBar()

        mainMenu = self.menuBar()
        
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extractAction)
        
        editorMenu = mainMenu.addMenu("&Editor")
#        editorMenu.addAction(openEditor)
        editorMenu.addAction(openFile)
        editorMenu.addAction(saveFile)
        editorMenu.addAction(closeEditor)

        self.home()

    def home(self):
        btn = QtWidgets.QPushButton("Convert", self)
        btn.clicked.connect(self.close_application)
        btn.resize(btn.minimumSizeHint())
        btn.move(0,100)

        extractAction = QtWidgets.QAction(QtGui.QIcon('run.jpg'), 'Exit', self)
        extractAction.triggered.connect(self.close_application)
        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractAction)

        fontChoice = QtWidgets.QAction('Font', self)
        fontChoice.triggered.connect(self.font_choice)
        #self.toolBar = self.addToolBar("Font")
        self.toolBar.addAction(fontChoice)

        color = QtGui.QColor(0, 0, 0)

        fontColor = QtWidgets.QAction('Font bg Color', self)
        fontColor.triggered.connect(self.color_picker)

        self.toolBar.addAction(fontColor)

        checkBox = QtWidgets.QCheckBox('Enlarge Window', self)
        checkBox.move(300, 25)
        checkBox.stateChanged.connect(self.enlarge_window)

        self.progress = QtWidgets.QProgressBar(self)
        self.progress.setGeometry(200, 80, 250, 20)

        self.btn = QtWidgets.QPushButton("Download",self)
        self.btn.move(200,120)
        self.btn.clicked.connect(self.download)

        #print(self.style().objectName())
        self.styleChoice = QtWidgets.QLabel("Windows Vista", self)

        comboBox = QtWidgets.QComboBox(self)
        comboBox.addItem("windowsvista")
        comboBox.addItem("Fusion")
        comboBox.addItem("Windows")        
        
        comboBox.move(50, 250)
        self.styleChoice.move(50,150)
        comboBox.activated[str].connect(self.style_choice)

#        cal = QtWidgets.QCalendarWidget(self)
#        cal.move(500,200)
#        cal.resize(200,200)
#
        self.show()

    def editor_close(self):
    	self.textEdit.close()


    def file_open(self):
        name = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File')
        file = open(name[0],'r')

        self.editor()

        with file:
            text = file.read()
            self.textEdit.setText(text)

    def file_save(self):
        name = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File')
        file = open(name,'w')
        text = self.textEdit.toPlainText()
        file.write(text)
        file.close()

    def color_picker(self):
        color = QtGui.QColorDialog.getColor()
        self.styleChoice.setStyleSheet("QWidget { background-color: %s}" % color.name())

    def editor(self):
        self.textEdit = QtWidgets.QTextBrowser()
        self.setCentralWidget(self.textEdit)


    def font_choice(self):
        font, valid = QtWidgets.QFontDialog.getFont()
        if valid:
            self.styleChoice.setFont(font)


    def style_choice(self, text):
        self.styleChoice.setText(text)
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create(text))


    def download(self):
        self.completed = 0

        while self.completed < 100:
            self.completed += 0.0001
            self.progress.setValue(self.completed)

    def enlarge_window(self, state):
        if state == QtCore.Qt.Checked:
            self.setGeometry(50,50, 1000, 600)
        else:
            self.setGeometry(50, 50, 500, 300)
        
    def close_application(self):
        choice = QtWidgets.QMessageBox.question(self, 'Extract!',
                                            'Are you sure you want to leave',
                                            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if choice == QtWidgets.QMessageBox.Yes:
            print("Extracting Naaaaaaoooww!!!!")
            sys.exit()
        else:
            pass
        
  
def run():
    app = QtWidgets.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()