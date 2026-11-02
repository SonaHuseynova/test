N=19
self.ui.OK.clicked.connect(self.func)
def func(self):
    a=self.ui.textEdit.toPlainText()
    if int(a)==N:
        QMessageBox.warning(self,"Diqqet","Yes")
    else:
        QMessageBox.warning(self,"Diqqet","No")