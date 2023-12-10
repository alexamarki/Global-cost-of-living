import os
from flask import Flask, render_template, redirect, jsonify
from flask import request
from werkzeug import exceptions
from forms.form import PostForm, MapForm
import pandas as pd
import pretty_html_table
import geojson
from main import mapper

df = pd.read_csv("static/data.csv")
with open('static/countries.geojson') as f:
    gj = geojson.load(f)



app = Flask(__name__)
app.config['SECRET_KEY'] = 'KJKjxkwh7w6%575&jBHJI(987'


# @app.errorhandler(exceptions.BadRequest)
# def handle_401(_):
#     return render_template('error.html', error=401)
#
#
# @app.errorhandler(exceptions.BadRequest)
# def handle_403(_):
#     return render_template('error.html', error=403)
#
#
# @app.errorhandler(exceptions.BadRequest)
# def handle_404(_):
#     return render_template('error.html', error=404)
#
#
# @app.errorhandler(exceptions.BadRequest)
# def handle_500(_):
#     return render_template('error.html', error=500)
#
#
# app.register_error_handler(401, handle_401)
# app.register_error_handler(403, handle_403)
# app.register_error_handler(404, handle_404)
# app.register_error_handler(500, handle_500)


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
@app.route('/dash', methods=['GET', 'POST'])
def home():
    form = PostForm()
    if form.is_submitted():
        metric = form.data.data
        bottom = form.highlow.data
        amount = form.top.data
        dfc = df[[metric, 'country', 'city']]
        dfc = dfc.dropna()
        out = dfc.sort_values(by=metric, ascending=(True if bottom == 'btm' else False)).head(int(amount))
        out = pretty_html_table.build_table(out, 'orange_light', font_size='large')
        return render_template('home.html', form=form, table=out, webview_title='Cost of living - Dashboard')
    return render_template('home.html', form=form, table=None, webview_title='Cost of living - Dashboard')


@app.route('/map', methods=['GET', 'POST'])
def map():
    form = MapForm()
    if form.is_submitted():
        metric = form.data.data
        low = abs(form.low.data)
        high = abs(form.high.data)
        out = mapper(low, high, metric, df, gj)
        return render_template('map.html', form=form, map=out, webview_title='Cost of living - Map')
    return render_template('map.html', form=form, map=None, webview_title='Cost of living - Map')


@app.route('/info')
def info():
    return render_template('info.html', webview_title='Cost of living - About')


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
