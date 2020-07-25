import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
desired_width = 400
pd.set_option('display.width', desired_width)

#FrameA = Requirement Tabular Summary
frameA = pd.read_excel('A.xlsx', sheet_name='Data')
frameA.head()

#Clean up the Linke Tests Column.
# todo:  try lambda functions
frameA['Linked Tests'] = frameA['Linked Tests'].str.replace("\[\[", "[")
frameA['Linked Tests'] = frameA['Linked Tests'].apply(lambda x: x[1:-1].split('] ['))

frameA=frameA.explode('Linked Tests')
frameA[['TestIndex','TestName']] = frameA['Linked Tests'].str.split(' ',1,expand=True)

#FrameB = Instance Tabular Summary


#FrameC = Issue Tabular Summary


print(frameA.head(100))