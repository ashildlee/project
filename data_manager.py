import pandas as pd


class DataManager:
    def __init__(self):
        self.test = 10
        self.startDate = "2020-10-21"

        # => 엑셀 데이터 불러오기
        # 검색 키워드 : pandas excel read with sheet
        # https://ponyozzang.tistory.com/618
        self.dfClose = pd.read_excel('t1701.xlsx', sheet_name='종가')
        self.dfPerson = pd.read_excel('t1701.xlsx', sheet_name='개인')
        self.dfFirm = pd.read_excel('t1701.xlsx', sheet_name='기관')
        self.dfForeigner = pd.read_excel('t1701.xlsx', sheet_name='외국인')
        self.dfCode = pd.read_excel('종목코드2.xlsx', sheet_name='KOSPI200', header=None, dtype=str)
        # print(self.dfClose)
        # print(self.dfPerson)
        # print(self.dfFirm)
        # print(self.dfForeigner)

        self.dfCode = self.dfCode.set_index(0)
        # print(self.dfCode)


        # 컬럼 순회하기 (column iteration pandas)
        for (columnName, columnData) in self.dfPerson.iteritems():
            if columnName == '일자':
                # 숫자를 pandas 날짜포맷으로 변경 (pandas int date to string date)
                self.dfPerson['일자'] = pd.to_datetime(self.dfPerson['일자'].astype(str), format='%Y%m%d')
                continue
            # print('Colunm Name : ', columnName)
            # print('Column Contents : ', columnData.values)

            # 개인/기관/외국인 데이터 정리 (양수는 1 음수는 0으로 정리)
            # (pandas change data by condition)
            self.dfPerson[columnName] = (self.dfPerson[columnName] > 0).astype(int)

        for (columnName, columnData) in self.dfFirm.iteritems():
            if columnName == '일자':
                self.dfFirm['일자'] = pd.to_datetime(self.dfFirm['일자'].astype(str), format='%Y%m%d')
                continue
            self.dfFirm[columnName] = (self.dfFirm[columnName] > 0).astype(int)

        for (columnName, columnData) in self.dfForeigner.iteritems():
            if columnName == '일자':
                self.dfForeigner['일자'] = pd.to_datetime(self.dfForeigner['일자'].astype(str), format='%Y%m%d')
                continue
            self.dfForeigner[columnName] = (self.dfForeigner[columnName] > 0).astype(int)

        for (columnName, columnData) in self.dfClose.iteritems():
            if columnName == '일자':
                self.dfClose['일자'] = pd.to_datetime(self.dfClose['일자'].astype(str), format='%Y%m%d')
                continue
        self.dfClose = self.dfClose.set_index('일자')

    def search(self, start_date, end_date, supplier_type, buysell_type):
        # def search(self):
        # start_date = "2021-10-20"
        # end_date = "2021-10-27"
        print(start_date, end_date, supplier_type, buysell_type)

        # 검색 키워드 : pandas select row by condition for date
        if supplier_type == 1:
            mask = (self.dfForeigner['일자'] > start_date) & (self.dfForeigner['일자'] <= end_date)
            df_search = self.dfForeigner.loc[mask]
        elif supplier_type == 2:
            mask = (self.dfFirm['일자'] > start_date) & (self.dfFirm['일자'] <= end_date)
            df_search = self.dfFirm.loc[mask]
        elif supplier_type == 3:
            mask = (self.dfPerson['일자'] > start_date) & (self.dfPerson['일자'] <= end_date)
            df_search = self.dfPerson.loc[mask]
        # print(df_search)
        # print(len(df_search))

        # print(df_search.sum().sort_values(ascending=False).index)
        if buysell_type == 1:
            # print(df_search.sum().nlargest(5))
            # print(df_search.sum().nlargest(5).index)
            df_result = df_search.sum(numeric_only=True).nlargest(5)
        elif buysell_type == 2:
            # print(df_search.sum().nsmallest(5))
            # print(df_search.sum().nsmallest(5).index)2r1
            df_result = df_search.sum(numeric_only=True).nsmallest(5)

        arr_result = []

        # 20210224
        # 282330  str

        for (columnName, columnData) in df_result.iteritems():

            # print(self.dfCode.loc[columnName])
            final_value = float(self.dfClose.loc[end_date + 'T00:00:00.000000000', columnName])
            initial_value = float(self.dfClose.loc[start_date + 'T00:00:00.000000000', columnName])

            # print(self.dfClose.index.values)
            # print(self.dfClose.at[end_date+'T00:00:00.000000000', columnName])
            # print(type(self.dfClose.at[start_date+'T00:00:00.000000000', columnName]))
            # print(columnName, columnData)
            # print({
            #     "name": columnName,
            #     "date": columnData if buysell_type == 1 else len(df_search) - columnData,
            #     "rate": 0 # 이 부분은 따로 계산해야함
            # })

            # mask1 = (self.dfClose['일자'] == start_date)
            # mask2 = (self.dfClose['일자'] == end_date)

            arr_result.append({
                "code": columnName,
                "name": str(self.dfCode.loc[columnName, 1]),
                #str(dfCode.loc[columnName]),
                "date_count": str(columnData) if buysell_type == 1 else str(len(df_search) - columnData),
                "rate": str(round((final_value - initial_value) / initial_value * 100, 3)) + "%"
                # 이 부분은 따로 계산해야함
            })
        # print(arr_result)
        return arr_result

# data_manager = DataManager()
# data_manager.search("2021-10-1", "2021-10-27", 1, 1)