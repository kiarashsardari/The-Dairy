import pandas as pd
from prettytable import PrettyTable as ptt
import brain as b
try:
    data = pd.read_csv('my_did.csv', encoding='utf-8-sig').to_dict('list')
    fe = True
except (FileNotFoundError, pd.errors.EmptyDataError):
    fe = False
    
def clean_input(prompt=''):
    inpt = input(prompt)
    return inpt.strip().lower()
table = ptt()
table.field_names = ['Action','Command']
table.add_row(['Saving Data','sd'])
table.add_row(['Showing Data','sh'])
table.add_row(['Feelings Plot','fp'])
table.add_row(['Exit','e'])
print(table)
command = clean_input('>> ')
print()

while True:
    if command == 'sd':
        b.main()

    elif command == 'sh':
        if fe:
            df = pd.read_csv('my_did.csv', index_col=False)
            print(df.to_string())
        else:
            print("\n File not exist or it's empty, please try ,<< sd >> first...\n")

    elif command == 'fp':
        input('\n- press enter to show plot... ')
        b.feelings_plot()
        print('')

    elif command == 'e':
        exit()

    print()
    command = clean_input('>> ')
    print()

