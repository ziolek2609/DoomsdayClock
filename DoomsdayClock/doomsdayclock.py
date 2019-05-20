# coding=utf-8
from flask import Flask, render_template, request
import datetime

app = Flask(__name__)


@app.route('/', methods=['GET'])
def send():
    return render_template('index.html')


@app.route('/timer', methods=['POST'])
def timer():
    edate = request.form['edate']  # pobieram wczytaną przez użytkownika datę
    date = edate.split("-")  # format daty zamieniam na tablicę
    etime = request.form['etime']  # pobieram wczytaną przez użytkowanika godzinę
    time = etime.split(":")  # format godziny zamieniam na tablicę
    time.append(00)  # dodaję do tablicy godziny 00, ponieważ gdy użytkownik wpisze 00sekund format to pomija
    # ustawiam datę końca świata za pomocą tablic daty i godziny
    end = datetime.datetime(int(date[0]), int(date[1]), int(date[2]), int(time[0]), int(time[1]), int(time[2]))
    now = datetime.datetime.now()
    delta = end - now  # różnica daty wpisanej i obecnej to pozostały czas do końca świata
    # obliczenia w celu uzyskania wartości poszczególnych jednostek czasowych:
    sec = round(delta.total_seconds())
    years = sec // (365 * 24 * 60 * 60)
    days = (sec % (365 * 24 * 60 * 60)) // (24 * 60 * 60)
    hours = (sec % (24 * 60 * 60)) // (60 * 60)
    mins = (sec % (60 * 60)) // 60
    secs = (sec % 60)
    # renderuje jednostki czasowe do timer.html w celu wyświetlenia odlicznika czasu
    return render_template('timer.html', years=years, days=days, hours=hours, mins=mins, secs=secs)

@app.route('/zegar', methods=['POST'])
def czas():
    edate = request.form['edate'] # pobieram wczytaną przez użytkownika datę
    etime = request.form['etime'] # pobieram wczytaną przez użytkowanika godzinę
    # renderuje do zegar.html date i godzine pobraną od użytkownika, aby wyświtlić kiedy będzie koniec świata
    return render_template('zegar.html', edate=edate, etime=etime)


if __name__ == '__main__':
    app.run(debug=True)
