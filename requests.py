import httplib2
import datetime
import time
import os
http = httplib2.Http()
content = http.request('http://127.0.0.1:5000/')[1]
decoded_c = content.decode()
begin_s=decoded_c.find("<p>")
end_s=decoded_c.find("</p>")
scope = decoded_c[begin_s+3:end_s]
list = scope.split(" ")
date = list[4]
hour = list[8]
date_parts=date.split(".")
hour_parts=hour.split(":")
end = datetime.datetime(int(date_parts[2]),int(date_parts[1]),int(date_parts[0]),int(hour_parts[0]),int(hour_parts[1]),int(hour_parts[2]))
print(end)
while True:
    now = datetime.datetime.now()
    delta = end - now
    sec = round(delta.total_seconds())
    years = sec//(365*24*60*60)
    days = (sec%(365*24*60*60))//(24*60*60)
    hours = (sec%(24*60*60))//(60*60)
    mins = (sec%(60*60))//60
    secs = (sec%60)
    print("to the end of the world left:")
    print(years,"years",days,"days",hours,"hours",mins,"minutes",secs,"seconds")
    time.sleep(1)
    os.system("cls")
