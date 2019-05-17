from flask import Flask, render_template, request
import datetime

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def send():
    if request.method =='POST':
        edate = request.form['edate']
        date = edate.split("-")
        etime = request.form['etime']
        time = etime.split(":")
        time.append(0)
        print(date)
        print(time)
        end = datetime.datetime(int(date[0]),int(date[1]),int(date[2]),int(time[0]),int(time[1]),int(time[2]))
        now = datetime.datetime.now()
        delta = end - now
        sec = round(delta.total_seconds())
        years = sec//(365*24*60*60)
        days = (sec%(365*24*60*60))//(24*60*60)
        hours = (sec%(24*60*60))//(60*60)
        mins = (sec%(60*60))//60
        secs = (sec%60)
        return render_template('zegar.html', edate=edate, etime=etime, years=years, days=days, hours=hours, mins=mins, secs=secs)

    return render_template('index.html')



if __name__=='__main__':
    app.run(debug=True)
