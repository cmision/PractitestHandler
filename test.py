import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
desired_width = 400
pd.set_option('display.width', desired_width)

frameA = pd.read_excel('B.xlsx', sheet_name='Data')
frameA.head()
frameA.rename(columns={'Linked Tests':'B'}, inplace = True)
frameA['B'] = frameA['B'].str.replace("\[\[", "[")
frameA['B'] = frameA['B'].str.replace("\]\]", "]")
frameA['B'] = frameA['B'].str.replace(" \"", "|")
frameA['B'] = frameA['B'].str.replace("\"\] \[", ",")
frameA['B'] = frameA.B.apply(lambda x: x[1:-1].split(','))
frameA=frameA.explode('B')
frameA[['TestIndex','TestName']] = frameA['B'].str.split('|',expand=True)
print(frameA.head(100))