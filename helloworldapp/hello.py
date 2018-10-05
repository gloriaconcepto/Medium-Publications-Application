#-------------------------------------------------------------------------------
# Name:        simple hello world app on flask
# Purpose:    educational
#
# Author:      mmk
#
# Created:     18/09/2018
# Copyright:   (c) mmk 2018
# Licence:     <gloriasoftconcepto>
#-------------------------------------------------------------------------------
from flask import Flask


app = Flask(__name__)

@app.route('/')
def hello():


    return 'Hello,World!'



if __name__ == '__main__':
    app.run()
