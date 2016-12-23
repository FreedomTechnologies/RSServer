#!/usr/bin/env python
import web
import schedule
import time
import threading
from threading import Thread

#This is a server meant to handle http request, web-hooks, ect. as well as trigger http requests, and run local scripts on response or schedules.
#======== -- CLASSES -- ============================================================================================================================================================    

class schedules:
    def job(self):
        print("Scheduled job executed.")
        
    def run(self):
        print("Setup and run scheduled jobs.")
        job = schedules().job
        schedule.every(5).seconds.do(job)
        schedule.every(1).minutes.do(job)
        schedule.every().hour.do(job)
        schedule.every().day.at("10:30").do(job)
        schedule.every().monday.do(job)
        schedule.every().wednesday.at("13:15").do(job)
        
        while True:
            schedule.run_pending()
            time.sleep(1)

class httprequest:
    def GET(self):
        print "redirect_GET"


#======== -- MAIN -- ============================================================================================================================================================
#When the Python interpreter reads a source file, it executes all of the code found in it.
#Before executing the code, it will define a few special variables. For example, if the python interpreter is running that module (the source file) as the main program, it sets the special __name__ variable to have a value "__main__". If this file is being imported from another module, __name__ will be set to the module's name.
if __name__ == '__main__':
        #app will listen for requests/hooks, then interpret how/if to execute a response.
    print("Setup and run app request listener.")
    #urls = capture that piece of the matched data, the second part is the name of a class to send the request to
    urls = (
        '/test', 'httprequest',
    )
    app = web.application(urls, globals())
    Thread(target = app.run()).start()
    #Schedules runs in parrellel with app
    sch = schedules()
    Thread(target = sch .run()).start()
