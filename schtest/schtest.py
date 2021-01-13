import schedule
import time
import datetime
import datetime



def writeout():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    with open('output.txt','a') as f:
        f.write("\n\n\nACTUALLY RAN AT {}\n\n\n".format(current_time))
        f.write("\n")
    return()



schedule.every().day.at("16:05").do(writeout)
while True:
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    with open('output.txt','a') as f:
        f.write("- did not run {}".format(current_time))
        f.write("\n")
    schedule.run_pending()
    time.sleep(360)
