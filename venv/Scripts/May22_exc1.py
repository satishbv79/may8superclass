import xlrd

path = "c:/test/Demo1.xlsx"
wb = xlrd.open_workbook(path)
ws = wb.sheet_by_name("Sheet1")
val = ws.cell_value(1, 1)
print(val)

row_count = ws.nrows
col_count = ws.ncols

# print("rows",row_count) #3
# print("cols",col_count) #2

def read_xl_data(input):
    for i in range(row_count):
        for j in range(col_count):
            if (ws.cell_value(i, j) == input):
                print(ws.cell_value(i + 1, j))
        break

read_xl_data("PWD")
