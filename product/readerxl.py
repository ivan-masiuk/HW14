import os
import openpyxl


def readxl(file_xlx):
    print("we are inside readxl. congrats")
    try:
        # xlsx_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'IPC_price_2021-01-12.xlsx')
        wb_obj = openpyxl.load_workbook(file_xlx)
        sheet = wb_obj.active
        for row in sheet.iter_rows(max_row=sheet.max_row):
            if not (row[0].value is None) and not (type(row[0].value) == str):
                article = row[0].value
                category = row[1].value
                company = row[2].value
                model = row[3].value
                start_price = row[6].value
                end_price = row[5].value
        print('Its work!')
    except:
        print('Something goes wrong!')