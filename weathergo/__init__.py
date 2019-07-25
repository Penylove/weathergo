from flask import Flask
import pyowm

# from flask.ext.heroku import Heroku


# instance
app = Flask(__name__)
app.config['SECRET_KEY'] = "810c3833528bae093ba107025925a5d4"
pyown_api_key = "2cac2a2f1a4907ada47ba637b9c3686f"

owm = pyowm.OWM(pyown_api_key)


# from weathergo import routes

from flask import render_template,url_for,flash,redirect,request
from weathergo.forms import Location

def checkLocation(data__):
    print('checking')
    try:
       owm.weather_at_place(data__)
       return redirect(url_for('result'))
       print('checked')
    except:
        message = 'Location not found.'
        return message
         
  
@app.route('/')
@app.route('/home', methods = ['GET','POST'])
def index():
    form = Location()
    
   
    return render_template('index.html',form = form)


@app.route('/result', methods = ['GET','POST'])
def result():
    
    form = Location()
    try:
        owm.weather_at_place(form.location.data)
    except:
        flash('search not found')
        return redirect(url_for('index'))
    obs = owm.weather_at_place(form.location.data)
    w = obs.get_weather()
    location_data = form.location.data

    # get weather infos --

    wind = w.get_wind()
    ref_time = w.get_reference_time(timeformat='iso')

    clouds = w.get_clouds()

    rain = w.get_rain()

    snow = w.get_snow()

    humidity = w.get_humidity()

    pressure = w.get_pressure()

    temperature = w.get_temperature(unit = 'celsius')

    weather_stat = w.get_status()

    detailed_w_stats = w.get_detailed_status()

    weather_icon_name = w.get_weather_icon_url()


    # get forecast
    # fc3h = owm.three_hours_forecast(form.location.data)

    # fc24h = owm.daily_forecast(form.location.data)

    # forecaster
    # f3 = fc3h.get_forcast()
    # f24 = fc24h.get_forcast()


    # when_rain_3 = fc3h.when_rain()
    # when_sun_3 = fc3h.when_sun()

    # when_clouds_3 = fc3h.when_clouds()

    # when_fog_3 = fc3h.when_fog()

    # when_snow_3 = fc3h.when_snow()

    return render_template('result.html',weather_stat = weather_stat, location_data = location_data,form = form,ref_time = ref_time, rain = rain, wind = wind,humidity=humidity,clouds =clouds,snow=snow,temperature = temperature,weather_icon_name = weather_icon_name,pressure = pressure, detailed_w_stats = detailed_w_stats)

@app.route('/about')
def about():
    return render_template('about.html')

