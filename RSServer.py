#!/usr/bin/env python
import web
import schedule
import time
import threading

#This is a server meant to handle http request, web-hooks, ect. as well as trigger http requests, and run local scripts on response or schedules.
#======== -- CLASSES -- ============================================================================================================================================================    
class s_schedules:
    def job_1(self):
        print threading.currentThread().getName()
        print("Scheduled job 1 executed.")
    def job_2(self):
        print threading.currentThread().getName()
        print("Scheduled job 2 executed.")
        
    def run(self):
        print threading.currentThread().getName()
        print("Setup and run scheduled jobs.")
        schedule.every(30).seconds.do(s_schedules().job_1)
        schedule.every(1).minutes.do(s_schedules().job_2)
        #schedule.every().hour.do(job)
        #schedule.every().day.at("10:30").do(job)
        #schedule.every().monday.do(job)
        #schedule.every().wednesday.at("13:15").do(job)
        
        while True:
            schedule.run_pending()
            time.sleep(1)

class httprequest:
    def GET(self, name=None):
        print threading.currentThread().getName()
        return "Hello World"


#======== -- MAIN -- ============================================================================================================================================================
#When the Python interpreter reads a source file, it executes all of the code found in it.
#Before executing the code, it will define a few special variables. For example, if the python interpreter is running that module (the source file) as the main program, it sets the special __name__ variable to have a value "__main__". If this file is being imported from another module, __name__ will be set to the module's name.
if __name__ == '__main__':
    print("----- START -----")
    #urls = capture that piece of the matched data, the second part is the name of a class to send the request to
    urls = (
        '/(.*)','httprequest',
    )
    #app will listen for requests/hooks, then interpret how/if to execute a response.
    app = web.application(urls, globals())
    web.config.debug = True
    
    #Schedules run in parrellel with WebApp
    sch = s_schedules()
    
    rt = threading.Thread(name='WebApp_Thread', target=app.run)
    st = threading.Thread(name='Schedule_Thread', target=sch.run)
    
    rt.start()
    st.start()
    
    while threading.activeCount > 1:
        time.sleep(60)
        print("There are %s active threads.\n Current thread is %s ." % (threading.activeCount(), threading.currentThread()))
    
    print("----- END -----")
