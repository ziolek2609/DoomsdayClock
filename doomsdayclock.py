from flask import Flask, render_template, request
import datetime
import time
import os

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def send():
    if request.method =='POST':
        eday = request.form['eday']
        etime = request.form['etime']
        end = datetime.datetime(eday,etime)
        now = datetime.datetime.now()
        delta = end - now
        sec = round(delta.total_seconds())
        years = sec//(365*24*60*60)
        days = (sec%(365*24*60*60))//(24*60*60)
        hours = (sec%(24*60*60))//(60*60)
        mins = (sec%(60*60))//60
        secs = (sec%60)
        return render_template('zegar.html', years=years, days=days, hours=hours, mins=mins, secs=secs)

    return render_template('index.html')



if __name__=='__main__':
    app.run(debug=True)
