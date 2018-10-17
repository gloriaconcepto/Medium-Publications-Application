#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      mmk
#
# Created:     18/09/2018
# Copyright:   (c) mmk 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Fucker!"




if __name__ == '__main__':
    app.run()
