import pandas
import openpyxl
def import_():
    input_file = input('Введите название файла с расширением: ')
    d1 = pandas.read_excel(f'{input_file}')
    d2 = pandas.read_excel('my_project.xlsx')
    d3 = pandas.concat([d2, d1], axis = 0, ignore_index = False)
    d3 = d3.set_index('ID')
    # d3 =  pandas.concat([d2, d1], keys=['t1', 't2']).reset_index()
    d3.to_excel('my_project.xlsx')
    # merge =  pandas.DataFrame()
    # for file in files:
    #     df = pandas.read_excel(file)
    #     merge = pandas.concat(df)
    #     merge.to_excel('my_project.xlsx')
    # # data.to_excel('my_project.xlsx')
