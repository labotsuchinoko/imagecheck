# coding: utf-8
from flask import Flask, render_template, request, redirect, url_for, jsonify
import api
import json

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

def picked_up():
    messages = "image check"
    return messages

@app.route('/check')
def check():
    title = "check image url"
    message = picked_up()
    return render_template('index.html',
                           message=message, title=title)

@app.route('/post', methods=['GET', 'POST'])
def post():
    title = "check image url"
    #if request.method == 'POST':
    if request.form['name']:
        name = request.form['name']
        model = request.form['model']
        detectname, detail, inputurl = api.ImageCheck(name,model).goCheck()
        if detectname:
            return render_template('index.html',
                                   model=model, name=name, title=title, detectname=detectname, detail=detail, inputurl=inputurl)
        else:
            return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.route('/')
def index():
    title = "checked list"
    p = api.ccdb.PredictDb.select()
    return render_template('dblist.html', p=p)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=3001)
