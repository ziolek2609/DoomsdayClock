from flask import Flask, render_template, request, jsonify
import datetime

app = Flask(__name__)


@app.route('/', methods=['GET'])
def send():
    return render_template('index.html')


@app.route('/timer', methods=['POST'])
def timer():
    edate = request.form['edate']  # pobieram wczytaną przez użytkownika datę
    date = edate.split("-")  # format daty zamieniam na tablicę
    etime = request.form['etime']  # pobieram wczytany przez użytkowanika czas
    time = etime.split(":")  # format czasu zamieniam na tablicę
    time.append(00)  # dodaję do tablicy czasu 00, ponieważ gdy użytkownik wpisze 00sekund format to pomija
    # ustawiam datę końca świata za pomocą tablic daty i czasu
    end = datetime.datetime(int(date[0]), int(date[1]), int(date[2]), int(time[0]), int(time[1]), int(time[2]))
    now = datetime.datetime.now()
    delta = end - now
    sec = round(delta.total_seconds())
    years = sec // (365 * 24 * 60 * 60)
    days = (sec % (365 * 24 * 60 * 60)) // (24 * 60 * 60)
    hours = (sec % (24 * 60 * 60)) // (60 * 60)
    mins = (sec % (60 * 60)) // 60
    secs = (sec % 60)
    # różnica daty wpisanej i obecnej to pozostały czas do końca świata
    # obliczenia w celu uzyskania wartości poszczególnych jednostek czasowych:
    if delta.total_seconds()<0: #jeżeli minie wyznaczony czas, to spełnia się określone warunki i zegar oraz data znikają
        return jsonify(
        timer=render_template('timer.html', years=years, days=days, hours=hours, mins=mins, secs=secs), #renderuje plik z zegarem
        zegar = True,
        the_end = True,
        doomsday = True
        )
    elif (3600-20)<delta.total_seconds() <= 3600: # jeżeli zostanie poniżej godziny to na 20 sekund wyświetli się gif
        return jsonify(
            timer=render_template('timer.html', years=years, days=days, hours=hours, mins=mins, secs=secs),
            less_than_hour=True
            )

    elif (60*60*24-20)<delta.total_seconds() <= (60*60*24): # jeżeli zostanie poniżej dnia to na 20 sekund pojawi się gif
        return jsonify(
            timer=render_template('timer.html', years=years, days=days, hours=hours, mins=mins, secs=secs),
            less_than_day=True
        )
    elif (60*60*24*365-20)<delta.total_seconds()<=(60*60*365*24): # jeżeli zostało poniżej roku to na 20 sekund pojawi sie gif
        return jsonify(
            timer=render_template('timer.html', years=years, days=days, hours=hours, mins=mins, secs=secs),
            less_than_year=True
            )
    else: # jeżeli nie zostanie spełniony żaden z powyższych warunków, to renderuje się zwykły zegar odliczający czcas do końca
        return jsonify(
        timer=render_template('timer.html', years=years, days=days, hours=hours, mins=mins, secs=secs)
    )


@app.route('/zegar', methods=['POST'])
def czas():
    edate = request.form['edate']
    etime = request.form['etime']
    return render_template('zegar.html', edate=edate, etime=etime) # renderuje zegar z wykorzystaniem czasu i daty podanej w index.html


if __name__ == '__main__': #uruchamia serwer
    app.run(debug=True)
