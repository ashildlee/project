import pandas as pd

class DataManager:
    def __init__(self, dfclose):

        self.startDate = "2021-1-1"
        self.dfClose = dfclose
        self.dfPerson = pd.read_excel('data_202111.xlsx', sheet_name='개인')
        self.dfFirm = pd.read_excel('data_202111.xlsx', sheet_name='기관')
        self.dfForeigner = pd.read_excel('data_202111.xlsx', sheet_name='외국인')
        self.dfCode = pd.read_excel('종목코드.xlsx', sheet_name='KOSPI200', header=None, dtype=str)
        self.dfCode = self.dfCode.set_index(0)

        # 컬럼 순회하기 (column iteration pandas)
        for (columnName, columnData) in self.dfPerson.iteritems():
            if columnName == '일자':
                self.dfPerson['일자'] = pd.to_datetime(self.dfPerson['일자'].astype(str), format='%Y%m%d')
                continue

            # 개인/기관/외국인 데이터 정리 (양수는 1 음수는 0으로 정리)
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

        self.dfClose = self.dfClose.set_index('일자')

    def search(self, start_date, end_date, supplier_type, buysell_type):

        print(start_date, end_date, supplier_type, buysell_type)

        if supplier_type == 1:
            mask = (self.dfForeigner['일자'] >= start_date) & (self.dfForeigner['일자'] <= end_date)
            df_search = self.dfForeigner.loc[mask]
        elif supplier_type == 2:
            mask = (self.dfFirm['일자'] >= start_date) & (self.dfFirm['일자'] <= end_date)
            df_search = self.dfFirm.loc[mask]
        elif supplier_type == 3:
            mask = (self.dfPerson['일자'] >= start_date) & (self.dfPerson['일자'] <= end_date)
            df_search = self.dfPerson.loc[mask]

        if buysell_type == 1:
            df_result = df_search.sum(numeric_only=True).nlargest(10)
        elif buysell_type == 2:
            df_result = df_search.sum(numeric_only=True).nsmallest(10)
        arr_result = []

        for (columnName, columnData) in df_result.iteritems():

            final_value = float(self.dfClose.loc[df_search.loc[df_search.index[0], '일자'], columnName])
            initial_value = float(self.dfClose.loc[df_search.loc[df_search.index[-1], '일자'], columnName])

            arr_result.append({
                "code": columnName,
                "name": str(self.dfCode.loc[columnName, 1]),
                "date_count": str(columnData).center(16) if buysell_type == 1 else str(len(df_search) - columnData).center(16),
                "rate": (str(round((final_value - initial_value) / initial_value * 100, 2)) + "%").center(15)
            })
        return arr_result
