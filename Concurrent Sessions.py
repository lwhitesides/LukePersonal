import pandas as pd
from datetime import datetime

df = pd.read_csv('CallDetailRecords_20211220859.csv')

df['Call Start Time'] = pd.to_datetime(df['Call Start Time'])
print(type(df.iloc[0,0]))
print(type(df.iloc[0,1]))

df['Call End Time'] = df['Call Start Time'] + pd.to_timedelta(df['Duration'])
print(df['Call End Time'])

#IGNORE BELOW
#dateTest = datetime.strptime(df.iloc[0,0], "%m/%d/%Y %H:%M:%S %p %z")
#dateTest2 = dateTest.timestamp()
#print(dateTest2)

minStartTime = df['Call Start Time'].min()
print ("Min Start Time: ", minStartTime)
maxEndTime = df['Call End Time'].max()
print ("Max End Time: ", maxEndTime)

secondsRange = pd.date_range(start=minStartTime, end=maxEndTime, freq='S')
#print(secondsRange)
count=0
maxCount=0
for second in secondsRange:
    for index, row in df.iterrows():
        if row['Call Start Time'] <= second and second <= row['Call End Time']:
            count = count+1
            print("count: ", count)
    if count > maxCount:
        maxCount = count
        print("maxCount: ", maxCount)
    count = 0
print("Max Count: ", maxCount)