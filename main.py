import sys
from PyQt5 import QtCore,uic,QtWebEngineWidgets 
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget,QMainWindow
from PyQt5.QtWidgets import QApplication as app
import charts_generation

import Window_main
#调试uic新生成的py文件
# import window as Window_main

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        #图表类型
        self.charts_styles=['柱状图','折线图','散点图','作者博客']
        # # 使用ui文件导入定义界面类
        # self.ui = Window_main.Ui_WebShow()
        self.main=QWidget()
        self.ui = Window_main.Ui_WebShow()
        self.ui.setupUi(self.main)
        self.ui.retranslateUi(self.main)
        self.is_fitted=False
        #设置icon
        self.main.setWindowIcon(QIcon('./images/logo.ico'))
        #表格内容
        self.chart_title=''        
        self.dataname=''
        self.data_y=[]
        self.data_x=[]
        # 初始化界面
        
        #选项栏
        self.ui.comboBox_ChartsStyles.addItems(self.charts_styles)
        self.ui.comboBox_ChartsStyles.currentIndexChanged.connect(self.template_charts_show)
        #勾选栏
        self.ui.checkBox_is_fitted.stateChanged.connect(self.fitted)
        self.ui.checkBox_is_fitted.setVisible(False)
        #web
        self.widget_web=QtWebEngineWidgets.QWebEngineView(self.ui.frame_web)
        self.widget_web.setGeometry(0,0,700,700)
        self.widget_web.load(QtCore.QUrl.fromLocalFile(r'D:/share_ubuntu/FreeCharts/results/result.html'))
        # 设置下载行为
        profile = QtWebEngineWidgets.QWebEngineProfile.defaultProfile()
        profile.downloadRequested.connect(self.download)
        #输入栏
        self.ui.lineEdit_X.setPlaceholderText('以逗号分隔和结尾！')
        self.ui.lineEdit_Y.setPlaceholderText('以逗号分隔和结尾！')
        self.ui.lineEdit_X.returnPressed.connect(self.get_data_x)
        self.ui.lineEdit_Y.returnPressed.connect(self.get_data_y)
        self.ui.lineEdit_Title.returnPressed.connect(self.get_title)
        self.ui.lineEdit_DataName.returnPressed.connect(self.get_dataname)
        self.div=[',','，',' ','\n']
        #生成键
        self.ui.pushButton_Generate.clicked.connect(self.generate)

    def template_charts_show(self):
        self.widget_web.setGeometry(0,0,700,700)
        style=self.ui.comboBox_ChartsStyles.currentText()
        # match style:
        #     case self.charts_styles[0]:
        #         self.widget_web.load(QtCore.QUrl.fromLocalFile(r'D:/share_ubuntu/FreeCharts/render.html'))
        if style==self.charts_styles[0]:
            self.ui.checkBox_is_fitted.setVisible(False)
            self.widget_web.load(QtCore.QUrl.fromLocalFile(r'D:/share_ubuntu/FreeCharts/template/bar_template.html'))
        elif style==self.charts_styles[1]:
            self.ui.checkBox_is_fitted.setVisible(False)
            self.widget_web.load(QtCore.QUrl.fromLocalFile(r'D:/share_ubuntu/FreeCharts/template/line_template.html'))
        elif style==self.charts_styles[2]:
            self.ui.checkBox_is_fitted.setVisible(True)
            self.widget_web.load(QtCore.QUrl.fromLocalFile(r'D:/share_ubuntu/FreeCharts/template/scatter_template.html'))
        elif style==self.charts_styles[3]:
            self.ui.checkBox_is_fitted.setVisible(False)
            self.widget_web.load(QtCore.QUrl('https://wenshijian.site/'))
        

    def get_data_x(self):
        data=[]
        temp=''
        string=self.ui.lineEdit_X.text()
        for _ in string:
            if _ in self.div:

                data.append(temp)
                temp=''
            else:
                temp+=_
                # print(temp)
        self.data_x=data
        

    
    def get_data_y(self):
        data=[]
        temp=''
        string=self.ui.lineEdit_Y.text()
        for _ in string:
            if _ in self.div:
                data.append(temp)
                temp=''
            else:
                temp+=_
        
        self.data_y=data

    def get_title(self):
        self.chart_title=self.ui.lineEdit_Title.text()
        # print(self.chart_title)
    def get_dataname(self):
        self.dataname=self.ui.lineEdit_DataName.text()
        if self.dataname is None:
            self.dataname=''
    def fitted(self):
        self.is_fitted=self.ui.checkBox_is_fitted.isChecked()
    def generate(self):
        self.get_data_x()
        self.get_data_y()
        self.get_title()
        self.get_dataname()
        self.widget_web.setGeometry(0,0,700,700)
        style=self.ui.comboBox_ChartsStyles.currentText()

        if style==self.charts_styles[0]:
            self.result = charts_generation.bar_generation(self.chart_title,self.data_x,self.data_y,self.dataname).result
            
        elif style==self.charts_styles[1]:
            self.result = charts_generation.line_generation(self.chart_title,self.data_x,self.data_y,self.dataname).result

        elif style==self.charts_styles[2]:
            self.result = charts_generation.scatter_generation(self.chart_title,self.data_x,self.data_y,self.dataname,self.is_fitted).result

        
        self.widget_web.load(QtCore.QUrl.fromLocalFile(self.result))

    def download(self,download:QtWebEngineWidgets.QWebEngineDownloadItem):
        download_path = './results/result_pic.png'
        download.setPath(download_path)
        download.accept() 


if __name__=='__main__':
    app_web=app(sys.argv)
    Main=MainWindow()
    Main.main.show()
    app.exec()