# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 22:08:07 2022

@author: yehuh
"""
import GetWorkedDay

def hello_world(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    real_work_day = GetWorkedDay.GetWorkedDay(5)

    request_json = request.get_json()
    if request.args and 'message' in request.args:
        return request.args.get('message')
    elif request_json and 'message' in request_json:
        return request_json['message']
    else:
        return str(real_work_day[0])

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/data/appInfo/<name>', methods=['GET'])
def queryDataMessageByName(name):
    print("type(name) : ", type(name))
    return 'String => {}'.format(name)

@app.route('/data/appInfo/id/<int:id>', methods=['GET'])
def queryDataMessageById(id):
    print("type(id) : ", type(id))
    return 'int => {}'.format(id)

@app.route('/data/appInfo/version/<float:version>', methods=['GET'])
def queryDataMessageByVersion(version):
    print("type(version) : ", type(version))
    return 'float => {}'.format(version)

import ToGoogleCloud
from datetime import date
@app.route("/home")
def home():
    df = ToGoogleCloud.GetDF_FromGCP()
    work_days = GetWorkedDay.GetWorkedDay(10)
    work_day = work_days[0].date()
    df_today = df[df.DATE == work_day]
    df_over = df_today[df_today.DEAL_AMOUNT > 1000000000]
    html = df_over.to_html()
    #text_file = open("C:/Users/yehuh/FlaskOnGCP/templates/index.html", "w")
    #text_file.write(html)
    #text_file.close()
    
    return html
    #return render_template("index.html")
    #return render_template("home.html")

@app.route("/page/text")
def pageText():
    return render_template("page.html", text="Python Flask !")

@app.route('/page/app')
def pageAppInfo():
    appInfo = {  # dict
        'id': 5,
        'name': 'Python - Flask',
        'version': '1.0.1',
        'author': 'yehuh',
        'remark': 'Python - Web Framework'
    }
    return render_template('page.html', appInfo=appInfo)

@app.route('/page/data')
def pageData():
    data = {  # dict
        '01': 'Text Text Text',
        '02': 'Text Text Text',
        '03': 'Text Text Text',
        '04': 'Text Text Text',
        '05': 'Text Text Text'
    }
    return render_template('page.html', data=data)

@app.route('/static')
def staticPage():
    return render_template('static.html')

app.run()


