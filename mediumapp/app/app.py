from flask import Flask

from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask import Flask, render_template, flash, request,url_for,redirect
#from flask import Flask, flash, redirect, render_template, request, session, abort
#from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import requests
import json
from medium import Client
import feedparser
import os
from markupsafe import Markup
#app configuration
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '95f5522f07d05fc9daffab6b7aecbb131f526b3fa3ff4280'
#ngrok link
ngrok_link ="https://c0dcc7f0.ngrok.io"






# (Send the user to the authorization URL to obtain an authorization code.)

# Exchange the authorization code for an access token.

#auth = client.exchange_authorization_code("YOUR_AUTHORIZATION_CODE", "http://127.0.0.1:5000/resultDisplay/callback/medium")

#class for the search form
class SearchButton(Form):
       name = StringField('name:', validators=[Required()])
       #submit_value = Markup('<span class="fa fa-search" title="Submit"></span>')
       submit=SubmitField()


#route to the app page with a post method to authenticate the user if it have a valid  medium account....#redirect to medium website...
@app.route('/', methods = ['GET', 'POST'])
def home():
        name =''

        #home page rendering...
        #set the default page to render a default medium user account
        #if the page is search redirect to another page with the same layout
        #save the data tenporary for 5 min in the database then ..more ideas to come....
        form = SearchButton()

         #if the submit button is click get the user name:
        if request.method=="POST":
            #flash(f'name is {{form.name}}','sucess')
            name=request.form['name']

            #return redirect(url_for('about'),name=name)
            return render_template('resultDisplay.html',name=name)



         #if request.method == 'POST' :
            # name=request.form['name']
        # if form.validate_on_submit():
         #          name = form.name.data
          #         form.name.data=''

           #        return  render_template('about.html')



         #elif request.method == 'GET':
         #else:
         #  flash("hey")  #flash work when a variable is created and the variable is capture at the html form.
        return render_template('home.html',form=form)
        #now how to render a post method...

def get_current_publications(user_id,acess_token):

          url="https://api.medium.com/v1/users/{}/publications".format(user_id)   #?type=json

          token=acess_token
          get_pub = Client(application_id="45ec1ddf13cb", application_secret="b42623c0f2ee207a6872a76c0bc7c2eb88411a77")

          return requests.request("GET",url,headers = { "Accept": "application/json","Accept-Charset": "utf-8", "Authorization": "Bearer %s" % token,})
          #return get_pub._request("GET",url2)


#empty list to store name of publication
pub_name=[]
#empty list to store description of publication
desrip_pub=[]
#empty list to store image of publication
image_pub=[]
#empty list to store  publication url
url_pub=[]

# A RSS FEEDER FUNCTION
def get_medium(user_name):
    medium_feed="https://medium.com/feed/@{}".format(user_name)
    feed = feedparser.parse(medium_feed)
    first_article = feed['entries']
    return first_article
    ''' return """<html>
    <body>
    <h1>Headlines </h1>
    <b>{0}</b> </ br>
    <i>{1}</i> </ br>
    <p>{2}</p> </ br>
    </body>
    </html>""".format(first_article.get("title"), first_article.
    get("link"), first_article.get("post")) '''

#store posts title of the user
rss_titles=[]
#store tags of the user
rss_tags=[]
#store link to the post
rss_links=[]

#A FUCNTION TO STORE DATA GOTTEN FROM MEDIUM RSS FEEDER.
def get_medium_rss_data(feed_data):
    ''' This Function only store the following datas: posts Title,post tags,post link '''
    #loop through the feed_data  a list in a
    for dict_item in feed_data:
        for key,value in dict_item.items():
            if key=="tags":
                    rss_tags.append(value)
            if key=="title":
                    rss_titles.append(value)
            if key=="link":
                    rss_links.append(value)
            else:
                pass







@app.route('/resultDisplay/callback/medium')
def callback():
    #authentication process to get the acess token
    # Exchange the authorization code for an access token.
    pass

@app.route('/about/')
def about():

    return render_template('about.html')


# A Result landing page that displays the medium account details:
@app.route('/resultDisplay/')
def resultDisplay():
      #intialisation
    client = Client(application_id="45ec1ddf13cb", application_secret="b42623c0f2ee207a6872a76c0bc7c2eb88411a77")
    #post="Post"
    #client._request(post,"https://86acd90c.ngrok.io/resultDisplay/")

     # Build the URL where you can send the user to obtain an authorization code.
    auth_url = client.get_authorization_url("secretstate","{}/resultDisplay/callback/medium".format(ngrok_link),["basicProfile", "publishPost","listPublications"])

   # auth = client.exchange_authorization_code(print(auth_url),"https://b351e15d.ngrok.io/resultDisplay/callback/medium")
    return  redirect(auth_url,code=302)

    #how to get authorization code and send a request on medium.
    #auth = client.exchange_authorization_code("YOUR_AUTHORIZATION_CODE", "https://b351e15d.ngrok.io/resultDisplay/")

    #return render_template('resultDisplay.html')


if __name__ == "__main__":
   # app.secret_key = os.urandom(12)

    app.run(debug=True)
