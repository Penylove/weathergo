from flask import Flask
import pyowm



# instance
app = Flask(__name__)
app.config['SECRET_KEY'] = "810c3833528bae093ba107025925a5d4"
pyown_api_key = "2cac2a2f1a4907ada47ba637b9c3686f"

owm = pyowm.OWM(pyown_api_key)


# from weathergo import routes

from flask import render_template,url_for,flash,redirect,request
from weathergo.forms import Location

@app.route('/')
@app.route('/home', methods = ['GET','POST'])
def index():
    form = Location()
    # if form.validate_on_submit():
        
    #     return render_template(url_for('result'))
    # else:
    #     return render_template('k.html')
    return render_template('index.html',form = form)


@app.route('/result', methods = ['GET','POST'])
def result():
    form = Location()
    obs = owm.weather_at_place(form.location.data)
    w = obs.get_weather()
    location_data = w.get_wind()
    return render_template('result.html',location_data = location_data,form = form)