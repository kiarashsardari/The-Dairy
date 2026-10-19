import fa_console
from fa_console import fa_input
import pandas as pd
from prettytable import PrettyTable as ptt
import brain as b
fe = b.check_file()
    
def clean_input(prompt=''):
    inpt = input(prompt)
    return inpt.strip().lower()
table = ptt()
table.field_names = ['عمل','دستور']
table.add_row(['وارد کردن دیتای جدید','و'])
table.add_row(['نمایش دیتاهای قبلی','ن'])
table.add_row(['نمودار احساسات','ا'])
table.add_row(['خروج','خ'])
table.hrules = 1
print(table)
command = clean_input('>> ')
print()
while True:
    if command == 'sd' or command == 'و' or command == 'وارد' or command == 'جدید' or command == 'داداشم':
        b.main()

    elif command == 'sh' or command == 'ن' or command == 'نمایش':
        if fe:
            df = pd.read_csv('my_did.csv', index_col=False)
            print(df.to_string())
        else:
            print("\nهنوز وارد نشدی. اول وارد شو و فایل بساز...  \n")

    elif command == 'fp' or command == 'ا' or command == 'نمودار':
        fa_input('\n اینتر کن تا نمودار رو ببینی... ')
        b.feelings_plot()
        print('')

    elif command == 'e' or command == 'خ' or command == 'خروج' or command == 'بیرون':
        exit()

    print()
    print(table)
    print()
    command = clean_input('>> ')
    print()

