from datetime import datetime
import schedule
import time
from bot import open_class
from selenium import webdriver
import json

# def job(m,tp):
    # open_class(m,tp)
    # print("wtf is happening")
    # driver = webdriver.Chrome()
    # driver.get("https://accounts.google.com/signin/v2/identifier?service=classroom&passive=1209600&continue=https%3A%2F%2Fclassroom.google.com%2F%3Femr%3D0&followup=https%3A%2F%2Fclassroom.google.com%2F%3Femr%3D0&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
    # print(1)
    # time.sleep(m*5)
    # driver.close()

try:
    with open("Timetable.json",'r') as f:
        (tt,durationp,durationt) = json.load(f)
        f.close
except:
    tt = {}
    durationt = int(input("Duration of Theory period in minutes: "))
    durationp = int(input("Duration of practical period in minutes: "))
    for i in range(0,7):
        start = []
        nperiod = int(input("Enter number of periods for day {}: ".format(i)))
        if nperiod>0 :
            for j in range(nperiod):
                tp = str(input("Theory or practicle (t/p): "))
                fg=0
                while(fg==0):
                    if(tp=='t' or tp=='p'):
                        s = input("Start of period {} in 24hr format: ".format(j))
                        fg=1
                    else:
                        print("Wrong input enter again")
                        tp = str(input("Theory or practicle (t/p): "))
                start.append([s,tp])
            tt[str(i)] = start

    with open("Timetable.json",'w') as f:
        json.dump((tt,durationp,durationt),f)
        f.close

print("starting")
# breakpoint()

for t in tt[str(datetime.today().weekday())]:
    # for per in t:
        # breakpoint()
    if t[1]=='t':
        print(durationt,t[0],t[1])
        time_t = t[1]
        schedule.every().day.at(t[0]).do(lambda : open_class(durationt,time_t))
        print("Done1")
    else:
        time_p = t[1]
        print(durationp,t[0],t[1])
        schedule.every().day.at(t[0]).do(lambda : open_class(durationp,time_p))

while 1:
    schedule.run_pending()
    time.sleep(1)
