import openpyxl
import pandas
# Вариант №1
def read():
    book = openpyxl.open('my_project.xlsx', 'r')
    sheet = book.active
    for row in sheet.iter_rows():
        for cell in row:
            print(cell.value, end=" ")
        print()

# Вариант №2
# def read():
#     data = pandas.read_excel("my_project.xlsx")
#     print(data)
