#Credit to
#HID sp18-405
#HID sp18-412

from eve import Eve
import platform
import psutil
import json
from flask import Response

my_settings = {
    'MONGO_HOST': 'localhost',
    'MONGO_PORT': 27017,
    'MONGO_DBNAME': 'the_db_name',
    'DOMAIN': {'contacts': {}}
}


app = Eve(settings=my_settings)

@app.route('/processor')
def processor():
    name = platform.processor()
    system = platform.system()
    return("Processor name: "+name+"\n"+"System description: "+system+"\n")


@app.route('/ram')
def ram():
    ramUsage = list(psutil.virtual_memory())[0]
    return("Total RAM usage: "+str(ramUsage)+"\n")


@app.route('/disk')
def disk():
    totalDiskUsage = list(psutil.disk_usage('/'))[0]
    return("Total Disk : "+str(totalDiskUsage)+"\n")



@app.route('/allinfo', methods = ['GET'])
def allinfo():
    allinfo ={"Processor name":platform.processor(), "Total Disk":list(psutil.disk_usage('/'))[0],
              "Total RAM": list(psutil.virtual_memory())[0], "Free Disk":list(psutil.disk_usage('/'))[2]}

    sdata = json.dumps(allinfo)
    response = Response()
    response.headers["status"] = 200
    response.headers["Content-Type"] = "application/json; charset=utf-8"
    response.data = sdata
    return(response)

if __name__ == '__main__':
    app.run()


#in command shell use:
#python run.py
#curl -i http://localhost:5000/processor
#curl -i http://localhost:5000/ram
#curl -i http://localhost:5000/disk
#curl -i http://localhost:5000/allinfo

