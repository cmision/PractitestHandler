import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
desired_width = 400
pd.set_option('display.width', desired_width)


#Read the files in
frameA = pd.read_excel('A.xlsx', sheet_name='Data',index_col='ID') #FrameA = Requirement Tabular Summary
frameB = pd.read_excel('B.xlsx', sheet_name='Data',index_col='ID') #FrameB = Instance Tabular Summary
frameC = pd.read_excel('C.xlsx', sheet_name='Data',index_col='ID') #FrameC = Issue Tabular Summary

#Clean up the Linked Tests Column in Frame A - Requirement Tabular Summary.
frameA['Linked Tests'] = frameA['Linked Tests'].str.replace("\[\[", "[")
frameA['Linked Tests'] = frameA['Linked Tests'].str.replace("\]\]", "]")
frameA['Linked Tests'] = frameA['Linked Tests'].apply(lambda x: x[1:-1].split('] ['))

frameA=frameA.explode('Linked Tests')
frameA[['TestIndex','TestName']] = frameA['Linked Tests'].str.split(' ',1,expand=True)
frameA['TestIndex']=pd.to_numeric(frameA['TestIndex'], errors='coerce') #convert the test indexes to number

#Clean up the Linked Issues Column in FrameB - Instance Tabular Summary.
frameB['Test: Linked Issues'] = frameB['Test: Linked Issues'].str.replace("\[\[", "[")
frameB['Test: Linked Issues'] = frameB['Test: Linked Issues'].str.replace("\]\]", "]")
frameB['Test: Linked Issues'] = frameB['Test: Linked Issues'].apply(lambda x: x[1:-1].split(']['))

frameB=frameB.explode('Test: Linked Issues')
frameB[['IssueIndex','IssueName']] = frameB['Test: Linked Issues'].str.split(' ',1,expand=True)
frameB['Test: ID']=pd.to_numeric(frameB['Test: ID'], errors='coerce') #Test:ID is used to join to frameA
frameB['IssueIndex']=pd.to_numeric(frameB['IssueIndex'], errors='coerce') #issueIndex is used to join to frameC

#frameA left join frameB on A.id=B."test:id"
masterDF=pd.merge(frameA, frameB, how='left', left_on='TestIndex', right_on='Test: ID')

#masterDF left join frameC on masterdf.IssueIndex=C.ID
masterDF=pd.merge(masterDF,frameC,how='left',left_on='IssueIndex', right_on='ID')

#create the TestCounter column
masterDF['TestCounter'] = masterDF['Test: ID']
masterDF['TestCounter'].loc[~masterDF['TestCounter'].isnull()] = 1
masterDF['TestCounter'].loc[masterDF['TestCounter'].isnull()] = 0

#create the IssueCounter column
masterDF['IssueCounter'] = masterDF['IssueIndex']
masterDF['IssueCounter'].loc[~masterDF['IssueCounter'].isnull()] = 1
masterDF['IssueCounter'].loc[masterDF['IssueCounter'].isnull()] = 0

masterDF.to_excel("output.xlsx")