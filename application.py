from flask import Flask,render_template,request,redirect
#from github_analysis import createDateTimeFigure
from bokeh.embed import components
import os, sys

app = Flask(__name__)

app.vars={}

@app.route('/',methods=['GET','POST'])
def index():
    # this is a comment, just like in Python
    # note that the function name and the route argument
    # do not need to be the same.
    if request.method == 'GET':
        #create_tree()
        return render_template('inex4.html')
        #script = create_connection_dictionary("Facebook")
        #return render_template('index2.html')
    else:
        return render_template('index3.html', json_string=json_string)

if __name__ == '__main__':
    app.run()
