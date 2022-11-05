# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 10:35:40 2022

@author: aravi
"""

from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)
  
@app.route('/')
def index():
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)