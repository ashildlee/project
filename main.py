import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
import pandas as pd
import matplotlib.pyplot as plt
from data_manager import DataManager
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

form_class = uic.loadUiType("stock.ui")[0]


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.data_manager = DataManager()

        self.result_arr = []

        self.fig = plt.figure(figsize=(20, 12))
        self.canvas = FigureCanvas(self.fig)
        self.verticalLayout.addWidget(self.canvas)

        # 시작/종료 날짜
        self.date_start.dateChanged.connect(self.dateStartFunction)
        self.date_end.dateChanged.connect(self.dateEndFunction)
        self.date_start.setDate(QDate(2021, 10, 20))
        self.date_end.setDate(QDate(2021, 10, 27))

        # 매수/매도 버튼
        self.radio_buy.clicked.connect(self.radioBuysellFunction)
        self.radio_sell.clicked.connect(self.radioBuysellFunction)

        # 검색 버튼
        self.btn_search.clicked.connect(self.btnsearchFunction)

        # 라디오 버튼
        self.radio_supplier_1.clicked.connect(self.radioSupplierFunction)
        self.radio_supplier_2.clicked.connect(self.radioSupplierFunction)
        self.radio_supplier_3.clicked.connect(self.radioSupplierFunction)

        # Top5 table
        self.tableWidget.clicked.connect(self.selectTableFunction)

        # 버튼1~5클릭
        self.pushButton.clicked.connect(self.btnClick1)
        self.pushButton_2.clicked.connect(self.btnClick2)
        self.pushButton_3.clicked.connect(self.btnClick3)
        self.pushButton_4.clicked.connect(self.btnClick4)
        self.pushButton_5.clicked.connect(self.btnClick5)

    def btnClick1(self):

        self.dfClose = pd.read_excel('t1701.xlsx', sheet_name='종가')
        for (columnName, columnData) in self.dfClose.iteritems():
            if columnName == '일자':
                # 숫자를 pandas 날짜포맷으로 변경 (pandas int date to string date)
                self.dfClose['일자'] = pd.to_datetime(self.dfClose['일자'].astype(str), format='%Y%m%d')
                continue

        # print(self.dfClose)

        # print(self.dfClose['일자'])

        # start_date = self.dfClose['일자'].searchsorted(self.date_start.date().toString("yyyy-MM-dd"))
        # end_date = self.dfClose['일자'].searchsorted(self.date_end.date().toString("yyyy-MM-dd"))

        # result_df = self.dfClose.iloc['20211001':'20211012']
        # result_df = self.dfClose.loc('20211001' <= self.dfClose['일자'])
        # print(result_df)

        #그래프 그리기

        plt.figure(1)
        ax = self.fig.add_subplot(2, 1, 1)  # subplot 생성
        ax.plot(self.dfClose['일자'], self.dfClose[self.result_arr[0]['code']], label=self.result_arr[0]['code'], color='g')
        # ax.plot(dfClose['일자'], dfClose[''], label='Foreign', color='b')
        ax.set_title('Stock Price & Kospi Index'+self.result_arr[0]['code'], fontsize=8)  # 타이틀 설정
        ax.set_xlabel('Date', fontsize=6)  # x축 설정
        ax.set_ylabel('Stock Price', fontsize=6)  # y축 설정
        ax.grid()
        plt.xticks(rotation=45, fontsize=6)
        self.canvas.draw()

        # clear table(pyqt QTableWidgetclear)


        # plt.legend(['Individual', 'Institutional', 'Foreign'], loc='lower right', fontsize=8)
        # btnsearchFunction

            # self.dfPerson[columnName] = (self.dfPerson[columnName] > 0).astype(int)
        # columnData
        # result_arr = self.data_manager.search(self.date_start.date().toString("yyyy-MM-dd"),
        #                                       self.date_end.date().toString("yyyy-MM-dd"),
        #                                       self.getRadioSupplier(),
        #                                       self.getRadioBuysell())

        # df['일자'] = pd.to_datetime(df['일자'], format='%Y-%m-%d')
        # df.query('일자.dt.dayofweek == 0')
        # date_limit = '"%s"<= 일자 <= "%s"' % (
        # self.initial_date_label.date().toPyDate().isoformat(), self.final_date_label.date().toPyDate().isoformat())
        # print(date_limit)
        # df_test = df.query(date_limit)
        # df1 = df_test[['일자', '095570']]
        # print(df1)

        # ax = self.fig.add_subplot(1, 1, 1)  # subplot 생성
        # ax.plot(df1['일자'], df1['외국인계'], label='Foreign', color='b')
        # ax.set_title('Foreign Stock supply and demand analysis', fontsize=10)  # 타이틀 설정
        # ax.set_xlabel('date', fontsize=8)  # x축 설정
        # ax.set_ylabel('Supply and demand status', fontsize=8)  # y축 설정
        # ax.legend(fontsize=10, loc='best')  # 범례 설정 best로 해놓으면 가장 적절한 위치에 알아서 범례가 놓이게 됩니디
        # # plt.xticks(range(0, len(df1['날짜']), 3))
        # # plt.show()
        # plt.xticks(rotation=45, fontsize=6)
        # ax.grid()
        # self.canvas.draw()

    def btnClick2(self):

        self.dfClose = pd.read_excel('t1701.xlsx', sheet_name='종가')
        # print(self.dfClose)
        for (columnName, columnData) in self.dfClose.iteritems():
            if columnName == '일자':
                # 숫자를 pandas 날짜포맷으로 변경 (pandas int date to string date)
                self.dfClose['일자'] = pd.to_datetime(self.dfClose['일자'].astype(str), format='%Y%m%d')
                continue

        plt.figure(1)
        ax = self.fig.add_subplot(2, 1, 1)  # subplot 생성
        ax.plot(self.dfClose['일자'], self.dfClose[self.result_arr[1]['code']], label=self.result_arr[1]['code'],
                color='g')
        # ax.plot(dfClose['일자'], dfClose[''], label='Foreign', color='b')
        ax.set_title('Stock Price & Kospi Index' + self.result_arr[1]['code'], fontsize=8)  # 타이틀 설정
        ax.set_xlabel('Date', fontsize=6)  # x축 설정
        ax.set_ylabel('Stock Price', fontsize=6)  # y축 설정
        ax.grid()
        plt.xticks(rotation=45, fontsize=6)
        self.canvas.draw()

    def btnClick3(self):

        self.dfClose = pd.read_excel('t1701.xlsx', sheet_name='종가')
        # print(self.dfClose)
        for (columnName, columnData) in self.dfClose.iteritems():
            if columnName == '일자':
                # 숫자를 pandas 날짜포맷으로 변경 (pandas int date to string date)
                self.dfClose['일자'] = pd.to_datetime(self.dfClose['일자'].astype(str), format='%Y%m%d')
                continue

        plt.figure(1)
        ax = self.fig.add_subplot(2, 1, 1)  # subplot 생성
        ax.plot(self.dfClose['일자'], self.dfClose[self.result_arr[2]['code']], label=self.result_arr[2]['code'],
                color='g')
        # ax.plot(dfClose['일자'], dfClose[''], label='Foreign', color='b')
        ax.set_title('Stock Price & Kospi Index' + self.result_arr[2]['code'], fontsize=8)  # 타이틀 설정
        ax.set_xlabel('Date', fontsize=6)  # x축 설정
        ax.set_ylabel('Stock Price', fontsize=6)  # y축 설정
        ax.grid()
        plt.xticks(rotation=45, fontsize=6)
        self.canvas.draw()

    def btnClick4(self):

        self.dfClose = pd.read_excel('t1701.xlsx', sheet_name='종가')
        # print(self.dfClose)
        for (columnName, columnData) in self.dfClose.iteritems():
            if columnName == '일자':
                # 숫자를 pandas 날짜포맷으로 변경 (pandas int date to string date)
                self.dfClose['일자'] = pd.to_datetime(self.dfClose['일자'].astype(str), format='%Y%m%d')
                continue

        plt.figure(1)
        ax = self.fig.add_subplot(2, 1, 1)  # subplot 생성
        ax.plot(self.dfClose['일자'], self.dfClose[self.result_arr[3]['code']], label=self.result_arr[3]['code'],
                color='g')
        # ax.plot(dfClose['일자'], dfClose[''], label='Foreign', color='b')
        ax.set_title('Stock Price & Kospi Index' + self.result_arr[3]['code'], fontsize=8)  # 타이틀 설정
        ax.set_xlabel('Date', fontsize=6)  # x축 설정
        ax.set_ylabel('Stock Price', fontsize=6)  # y축 설정
        ax.grid()
        plt.xticks(rotation=45, fontsize=6)
        self.canvas.draw()

    def btnClick5(self):

        self.dfClose = pd.read_excel('t1701.xlsx', sheet_name='종가')
        # print(self.dfClose)
        for (columnName, columnData) in self.dfClose.iteritems():
            if columnName == '일자':
                # 숫자를 pandas 날짜포맷으로 변경 (pandas int date to string date)
                self.dfClose['일자'] = pd.to_datetime(self.dfClose['일자'].astype(str), format='%Y%m%d')
                continue

        plt.figure(1)
        ax = self.fig.add_subplot(2, 1, 1)  # subplot 생성
        ax.plot(self.dfClose['일자'], self.dfClose[self.result_arr[4]['code']], label=self.result_arr[4]['code'],
                color='g')
        # ax.plot(dfClose['일자'], dfClose[''], label='Foreign', color='b')
        ax.set_title('Stock Price & Kospi Index' + self.result_arr[4]['code'], fontsize=8)  # 타이틀 설정
        ax.set_xlabel('Date', fontsize=6)  # x축 설정
        ax.set_ylabel('Stock Price', fontsize=6)  # y축 설정
        ax.grid()
        plt.xticks(rotation=45, fontsize=6)
        self.canvas.draw()

    # 매수/매도 함수
    def radioBuysellFunction(self):
        if self.radio_buy.isChecked():
            print("Radio buy Checked")
        elif self.radio_sell.isChecked():
            print("Radio sell Checked")

    # 검색 함수
    def btnsearchFunction(self):
        print("btn sell clicked")
        self.result_arr = self.data_manager.search(self.date_start.date().toString("yyyy-MM-dd"),
                                              self.date_end.date().toString("yyyy-MM-dd"),
                                              self.getRadioSupplier(),
                                              self.getRadioBuysell())

        print("result", self.result_arr)
        # clear table (pyqt QTableWidget clear)
        self.tableWidget.setRowCount(0)

        for idx, item in enumerate(self.result_arr):
            self.tableWidget.insertRow(idx)
            self.tableWidget.setItem(idx, 0, QTableWidgetItem(item["code"]))
            self.tableWidget.setItem(idx, 1, QTableWidgetItem(item["name"]))
            self.tableWidget.setItem(idx, 2, QTableWidgetItem(item["date_count"]))
            self.tableWidget.setItem(idx, 3, QTableWidgetItem(item["rate"]))

    # 라디오 함수
    def radioSupplierFunction(self):
        if self.radio_supplier_1.isChecked():
            print("Radio 1 Checked")
        elif self.radio_supplier_2.isChecked():
            print("Radio 2 Checked")
        elif self.radio_supplier_3.isChecked():
            print("Radio 3 Checked")

    # 날짜 함수 - 시작
    def dateStartFunction(self):
        print(self.date_start.date())

    # 날짜 함수 - 종료
    def dateEndFunction(self):
        print(self.date_end.date())

    def selectTableFunction(self):
        print(self.tableWidget.currentRow())
        select_row = self.tableWidget.currentRow()
        print("selected stockname : ", self.tableWidget.item(select_row, 0).text())

    # 매수/매도 값 가져오기
    def getRadioBuysell(self):
        if self.radio_buy.isChecked():
            return 1
        elif self.radio_sell.isChecked():
            return 2

    # 라디오 값 가져오기
    def getRadioSupplier(self):
        if self.radio_supplier_1.isChecked():
            return 1
        elif self.radio_supplier_2.isChecked():
            return 2
        elif self.radio_supplier_3.isChecked():
            return 3

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', '프로그램을 종료 하시겠습니까',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()