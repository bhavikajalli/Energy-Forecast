#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Created on Sun Jun 10 19:10:18 2018
    
    @author: BhavikaJalli
    """

from flask import Flask, render_template, request, redirect
import requests
from requests.auth import HTTPBasicAuth
#import simplejson as json
import json
import pandas as pd
from bokeh.io import output_notebook
import numpy as np
from bokeh.layouts import gridplot
from bokeh.plotting import figure, show, output_file
from bokeh.models import ColumnDataSource
import bokeh
from bokeh.embed import components
import folium
import branca.colormap as cm
import time
from selenium import webdriver
from folium.plugins import HeatMap
import branca.colormap as cm


app = Flask(__name__)

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

@app.route('/DataExploration',methods=['GET','POST'])
def DataExploration():
    if request.method == 'GET':
        return render_template('DataExploration.html')
    else:
        year = request.form['year']
        graph = request.form['graph']
        return render_template('DataExploration.html',year = year,graph = graph) 

@app.route('/show_map/<year>/<graph>',methods=['GET'])
def show_map(year,graph):
    #request.args
    #year = request.form['year']
    #graph = request.form['graph']
    return render_template('maps/map_'+year+'_'+str(graph)+'.html')



if __name__ == '__main__':
    app.run(port=33507, debug=True)
