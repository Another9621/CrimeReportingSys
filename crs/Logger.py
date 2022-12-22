from datetime import *
def openlog():
    Log=open('Logfile_'+str(date.today())+'.txt','a')
    print("The log file is:",Log.name)
    Log.write('\n\ntime of logging: '+str(datetime.now()))
    Log.close()
def log(*string):
    with open('Logfile_'+str(date.today())+'.txt','a') as Log   :
        for i in string:
            Log.write('\n'+str(i))
