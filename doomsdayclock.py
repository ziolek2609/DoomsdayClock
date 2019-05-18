from flask import Flask, render_template, request
import datetime

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def send():
    if request.method =='POST':
        edate = request.form['edate'] #pobieram wczytaną przez użytkownika datę
        date = edate.split("-") #format daty zamieniam na tablicę
        etime = request.form['etime'] #pobieram wczytany przez użytkowanika czas
        time = etime.split(":") #format czasu zamieniam na tablicę
        time.append(00) #dodaję do tablicy czasu 00, ponieważ gdy użytkownik wpisze 00sekund format to pomija
        #ustawiam datę końca świata za pomocą tablic daty i czasu
        end = datetime.datetime(int(date[0]),int(date[1]),int(date[2]),int(time[0]),int(time[1]),int(time[2]))
        now = datetime.datetime.now()
        delta = end - now
        #obliczenia w celu uzyskania wartości poszczególnych jednostek czasowych:
        sec = round(delta.total_seconds())
        years = sec//(365*24*60*60)
        days = (sec%(365*24*60*60))//(24*60*60)
        hours = (sec%(24*60*60))//(60*60)
        mins = (sec%(60*60))//60
        secs = (sec%60)
        #określenie co ma zostać zwrócone do zegar.html:
        return render_template('zegar.html', edate=edate, etime=etime, years=years, days=days, hours=hours, mins=mins, secs=secs)

    return render_template('index.html')



if __name__=='__main__':
    app.run(debug=True)
