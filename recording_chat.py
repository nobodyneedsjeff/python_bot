import os
from datetime import datetime, timedelta

#random number
b=[0,1,2,3,4,]
a=['time','\n','date','\n']
c='date'
d='text'

directory = r'C:\Users\NAkanov\PycharmProjects\tele_bot_new_att\chats'
def typing():
    while True: #ask for user input
        answer = input("print to create name for a file: ") #print request
        if answer== ('stop') : break #stop
        else:
            with open(directory+"\\"+str(answer)+".txt",'a') as f: #open file which user inputed ('answer')
                for item in a:
                    f.write(str(item))#.write('\n\n')#.write(str(c)).write(str(d)) #what to write
                f.write('\n') #type empty lines
               # f.write(str(datetime.date("%d %b %y")))
                f.close() #close file



typing()
