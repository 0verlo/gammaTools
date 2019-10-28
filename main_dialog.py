# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QFileDialog

from Ui_main_window import Ui_MainWindow
from func.GammaReader import gammaReader
import func.GammaFuncs as gammaFunc

class Dialog(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Dialog, self).__init__(parent)
        self.setupUi(self)
        self.mainGammaInput = None
        self.subGammaInput = None
        self.resultList = []

    @pyqtSlot()
    def on_pushButton_FileOpenMain_clicked(self):
        """
        Slot documentation goes here.
        """
        openFile=QFileDialog.getOpenFileName(self,"open","Z:\\tmp","(*.txt)")
        #print(openFile)
        if('' == openFile[0]):
            return
        self.mainGammaInput = gammaReader(openFile[0])
        
        textShow = ''
        for strContent in self.mainGammaInput.gammaList:
            textShow = textShow + strContent + "\n"
        self.textEdit_TextViewerMain.setPlainText(textShow)
        
        self.mainGammaInput.contentCheck()
        if(False == self.mainGammaInput.gammaDone):
            self.statusBar().showMessage("!Content of:\""+openFile[0]+"\" is not gamma")
        else:
            self.statusBar().showMessage("")

    @pyqtSlot()
    def on_pushButton_FileOpenSub_clicked(self):
        """
        Slot documentation goes here.
        """
        openFile=QFileDialog.getOpenFileName(self,"open","Z:\\tmp","(*.txt)")
        #print(openFile)
        if('' == openFile[0]):
            return
        self.subGammaInput = gammaReader(openFile[0])
        
        textShow = ''
        for strContent in self.subGammaInput.gammaList:
            textShow = textShow + strContent + "\n"
        self.textEdit_TextViewerSub.setPlainText(textShow)
        
        self.subGammaInput.contentCheck()
        if(False == self.subGammaInput.gammaDone):
            self.statusBar().showMessage("!Content of:\""+openFile[0]+"\" is not gamma")
        else:
            self.statusBar().showMessage("")

    @pyqtSlot()
    def on_toolButton_drawMain_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        pass
        
    @pyqtSlot()
    def on_toolButton_drawSub_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        pass
        
    @pyqtSlot()
    def on_toolButton_drawResult_clicked(self):
        """
        Slot documentation goes here.
        """
        if(None == self.mainGammaInput):
            pass
        elif((0 != self.mainGammaInput.gammaDone)&
            ([] != self.resultList)):
            self.statusBar().showMessage("Draw.")
            gammaFunc.draw(self.resultList, self.mainGammaInput.gammaList)
            return

        if(None == self.subGammaInput):
            pass
        elif((0 != self.subGammaInput.gammaDone)&
            ([] != self.resultList)):
            self.statusBar().showMessage("Draw.")
            gammaFunc.draw(self.resultList, self.subGammaInput.gammaList)
            return
            
        self.statusBar().showMessage("No gamma is ready.")
        
    @pyqtSlot()
    def on_pushButton_extend_clicked(self):
        """
        Slot documentation goes here.
        """           
        if(None == self.mainGammaInput):
            pass
        elif(0 != self.mainGammaInput.gammaDone):
            self.resultList = gammaFunc.extend(self.mainGammaInput.gammaList, 1025)
            self.statusBar().showMessage("GammaMain have been extended.")
            self.textEdit_result.setPlainText(gammaFunc.reform(self.resultList))
            return

        if(None == self.subGammaInput):
            pass
        elif(0 != self.subGammaInput.gammaDone):
            self.resultList = gammaFunc.extend(self.subGammaInput.gammaList, 1025)
            self.statusBar().showMessage("GammaSub have been extended.")
            self.textEdit_result.setPlainText(gammaFunc.reform(self.resultList))
            return
        self.statusBar().showMessage("No gamma is ready.")
    
    @pyqtSlot()
    def on_pushButton_balance_clicked(self):
        """
        Slot documentation goes here.
        """
        if((None == self.mainGammaInput)|
            (None == self.subGammaInput)):
                pass
        elif((0 != self.mainGammaInput.gammaDone)&
            (0 != self.subGammaInput.gammaDone)):
            self.statusBar().showMessage("Balance done.")
            self.resultList = gammaFunc.balance(self.mainGammaInput.gammaList, self.subGammaInput.gammaList)
            self.textEdit_result.setPlainText(gammaFunc.reform(self.resultList))
            return
                
        self.statusBar().showMessage("No gamma is ready.")

    
    @pyqtSlot()
    def on_pushButton_smooth_clicked(self):
        """
        Slot documentation goes here.
        """
         
        if(None == self.mainGammaInput):
            pass
        elif(0 != self.mainGammaInput.gammaDone):
            self.statusBar().showMessage("Smooth GammaMain.")
            self.resultList = gammaFunc.smooth(self.mainGammaInput.gammaList)
            self.textEdit_result.setPlainText(gammaFunc.reform(self.resultList))
            return

        if(None == self.subGammaInput):
            pass
        elif(0 != self.subGammaInput.gammaDone):
            self.statusBar().showMessage("Smooth GammaSub.")
            self.resultList = gammaFunc.smooth(self.subGammaInput.gammaList)
            self.textEdit_result.setPlainText(gammaFunc.reform(self.resultList))
            return
            
        self.statusBar().showMessage("No gamma is ready.")
        
    @pyqtSlot()
    def on_pushButton_reform_clicked(self):
        """
        Slot documentation goes here.
        """
        if(None == self.mainGammaInput):
            pass        
        elif(0 != self.mainGammaInput.gammaDone):
            self.statusBar().showMessage("Reform GammaMain.")
            self.resultList = self.mainGammaInput.gammaList
            self.textEdit_result.setPlainText(gammaFunc.reform(self.resultList))
            return

        if(None == self.subGammaInput):
            pass
        elif(0 != self.subGammaInput.gammaDone):
            self.statusBar().showMessage("Reform GammaSub.")
            self.resultList = gammaFunc.reform(self.subGammaInput.gammaList)
            self.textEdit_result.setPlainText(gammaFunc.reform(self.resultList))
            return
                
        self.statusBar().showMessage("No gamma is ready.")
        
    @pyqtSlot()
    def on_toolButton_copy_clicked(self):
        """
        Slot documentation goes here.
        """
        self.textEdit_result.selectAll()
        self.textEdit_result.copy()

if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec_())
