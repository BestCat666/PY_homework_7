import getting
import reading
import import_inform
import export_inform
while True:
    operation = int(input('Введите номер операции: 1 - добавление записи, 2 - вывод записи на экран, 3 - импорт, 4 - экспорт, 5 - выход из программы): '))
    if operation == 1:
        getting.get()
    if operation == 2:
        reading.read()
    if operation == 3:
        import_inform.import_()
    if operation == 4:
        export_inform.export_()
    if operation == 5:
        break
