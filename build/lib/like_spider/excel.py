import time, os
from openpyxl import Workbook
from .config import *

class Excel():
    """This is a class that saves data to an excel file."""

    def saveFile(self, data, fileName):
        """save data to an excel file."""
        if fileName == "":
            print('file name error')
            return False
        fileDir = self.makeDir()
        if fileDir == '':
            print('file directory error')
            return False
        totalRow = len(data)
        if totalRow > 0:
            wb = Workbook()
            ws = wb.active
            for row in range(1, (totalRow + 1)):
                totalCol = len(data[(row - 1)])
                if totalCol > 0:
                    for col in range(1, (totalCol + 1)):
                        cell = ws.cell(row = row, column = col)
                        cell.value = data[(row - 1)][(col - 1)]
                else:
                    print('col data error')
                    break
            if totalCol > 0:
                wb.save(fileDir + "/" + fileName)
        else:
            print('row data error')

    def makeDir(self):
        """create a file directory"""
        localTime = time.localtime()
        month = time.strftime('%Y%m', localTime)
        day = time.strftime('%Y%m%d', localTime)
        if 'EXCEL_DIR' in globals() and EXCEL_DIR != "":
            if EXCEL_DIR[-1] == "/":
                path = EXCEL_DIR + month + "/" + day
            else:
                path = EXCEL_DIR + "/" + month + "/" + day
            if os.path.exists(path) == False:
                os.makedirs(path)
            return path
        else:
            return ''
