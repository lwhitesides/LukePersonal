import pandas as pd
from datetime import datetime

#READ CSV
df = pd.read_csv('CallDetailRecords_20211220859.csv')

#CONVERT STRING TO DATETIME
df['Call Start Time'] = pd.to_datetime(df['Call Start Time'])
print(type(df.iloc[0,0]))
print(type(df.iloc[0,1]))

#CREATE NEW COLUMN FOR CALL END TIME AND SORT DATA
df['Call End Time'] = df['Call Start Time'] + pd.to_timedelta(df['Duration'])
df = df.sort_values(by='Call Start Time')
print(df['Call End Time'])


#CHECK THAT CALL START TIME AND END TIME ARE CREATED CORRECTLY
minStartTime = df['Call Start Time'].min()
print ("Min Start Time: ", minStartTime)
maxEndTime = df['Call End Time'].max()
print ("Max End Time: ", maxEndTime)

#LOOP THROUGH ALL THE DATA. FOR EACH ROW CHECK IF THE CALL END TIME IS AFTER THE CALL START TIME OF OTHER ROWS
count = 0
maxCount = 0
for i in range(0, len(df)):
    for j in range(i+1, len(df)):
        if df.iloc[i]['Call End Time'] > df.iloc[j]['Call Start Time']:
            count = count+1
        if count > maxCount:
            maxCount = count
            print("maxCount: ", maxCount)
            print(df.iloc[i]['Call Start Time'])
    count = 0        
print("Done!")
