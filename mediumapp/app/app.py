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
#import database function from the model folder
from databaseapi import DataBase
#data for time..
from datetime import datetime
def client_test():
      app = Flask(__name__)
      app.config.from_object(__name__)
      app.config['SECRET_KEY'] = '95f5522f07d05fc9daffab6b7aecbb131f526b3fa3ff4280'
      return app

#========================app configuration=======================================
#app = Flask(__name__)
#app.config.from_object(__name__)
#app.config['SECRET_KEY'] = '95f5522f07d05fc9daffab6b7aecbb131f526b3fa3ff4280'
#==================ngrok link===================================================

ngrok_link ="https://4b96f14b.ngrok.io"

#=========================list to store rss details=============================
#store posts title of the user
rss_titles=[]
#store tags of the user
rss_tags=[]
#store link to the post
rss_links=[]
#=========================list to store publications details====================
#empty list to store name of publication
pub_name=[]
#empty list to store description of publication
desrip_pub=[]
#empty list to store image of publication
image_pub=[]
#empty list to store  publication url
url_pub=[]
#===============================================================================

#create a database....
database_name="mediumdatabase"
database=DataBase(database_name)

#set refresh button click to false
refresh_button_click=False
app=client_test()


#class for the search form
class SearchButton(Form):
       name = StringField('name:', validators=[Required()])
       #submit_value = Markup('<span class="fa fa-search" title="Submit"></span>')
       submit=SubmitField()


#route to the app page with a post method to authenticate the user if it have a valid  medium account....#redirect to medium website...
@app.route('/', methods = ['GET', 'POST'])
def home():
         name =''

         #set the refresh_button click to true
         global refresh_button_click

         refresh_button_click=True


         return render_template('home.html')
        #now how to render a post method...


def get_current_publications(user_id,acess_token):

          url="https://api.medium.com/v1/users/{}/publications".format(user_id)   #?type=json

          token=acess_token
          get_pub = Client(application_id="45ec1ddf13cb", application_secret="b42623c0f2ee207a6872a76c0bc7c2eb88411a77")

          return requests.request("GET",url,headers = { "Accept": "application/json","Accept-Charset": "utf-8", "Authorization": "Bearer %s" % token,})





# A RSS FEEDER FUNCTION
def get_medium(user_name):
    medium_feed="https://medium.com/feed/@{}".format(user_name)
    feed = feedparser.parse(medium_feed)
    first_article = feed['entries']
    return first_article



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


def get_publications_data(pub_lists):

            for dict_item in pub_lists:
                for key,value in dict_item.items():
                    if key=="id":

                      pass
                    else:
                        if key=="name":
                            pub_name.append(value)
                        if key=="description":
                            desrip_pub.append(value)
                        if key=="imageUrl":
                            image_pub.append(value)
                        if key=="url":
                            url_pub.append(value)





@app.route('/resultDisplay/callback/medium')
def call_back():
       global refresh_button_click
       global total_posts
       global count_length
       global user_profile
       global user_image
       global user_type
       global pub_name
       global desrip_pub
       global image_pub
       global url_pub
       global rss_link



       if ( refresh_button_click==True):
            #authentication process to get the acess token
            # Exchange the authorization code for an access token.
            client = Client(application_id="45ec1ddf13cb", application_secret="b42623c0f2ee207a6872a76c0bc7c2eb88411a77")
            #get_pub = Client(application_id="45ec1ddf13cb", application_secret="b42623c0f2ee207a6872a76c0bc7c2eb88411a77")
            secret = request.args.get("code")
            auth = client.exchange_authorization_code(secret,"{}/resultDisplay/callback/medium".format(ngrok_link))

            client.access_token = auth["access_token"]
            # Get profile details of the user identified by the access token.
            user = client.get_current_user()

            user_profile=user["username"]
            user_image=user["imageUrl"]
            user_id=user["id"]
            user_type=type(user)
            token=auth["access_token"]


            publications = get_current_publications(user_id,token)



            json_data_type = json.loads(publications.text) #publications.json()
            data_list=json_data_type["data"]

            #capture the data in the database....
            database.insert_data(user,data_list,datetime.now())

            # To determined the length of the publication..
            count_length = len(data_list)



            #testing
            #rss_links1=rss_feed[1].get("link")

            get_publications_data(data_list)
            '''  for dict_item in data_list:
                for key,value in dict_item.items():
                    if key=="id":

                      pass
                    else:
                        if key=="name":
                            pub_name.append(value)
                        if key=="description":
                            desrip_pub.append(value)
                        if key=="imageUrl":
                            image_pub.append(value)
                        if key=="url":
                            url_pub.append(value)

                                               '''
                       #person_data["name"]

              #get the user feeder data
            name=str(user["username"])
            rss_feed=get_medium(name)

            #store relevant data from the rss_feed to the rss_list
            get_medium_rss_data(rss_feed)



            #get the total posts of the user
            total_posts=len(rss_feed)

            #set refresh button click to false.
            refresh_button_click = False

            return render_template('callback.html',total_posts=total_posts,count_length=count_length,user_profile=user_profile,user_image=user_image,user_type=user_type,pub_name=pub_name,desrip_pub=desrip_pub,image_pub=image_pub,url_pub=url_pub,rss_links=rss_links,rss_tags=rss_tags,rss_titles=rss_titles)

       else:

            if(database.is_greater_than_cach_time(datetime.now())):
                 #get datas from the database
                 new_data=database.retrive_data()
                 #insert it back to the lists....
                 user_details=new_data[0]['userdetails']
                 pub_details=new_data[0]['publications']

                 #assigned it back to list variables  for user details and publications details
                 user_profile=user_details['username']
                 user_image=user_details['imageUrl']
                 user_id=user_details['id']
                 user_type=type(user_details)

                 get_publications_data(pub_details)



                 return render_template('callback.html',total_posts=total_posts,count_length=count_length,user_profile=user_profile,user_image=user_image,user_type=user_type,pub_name=pub_name,desrip_pub=desrip_pub,image_pub=image_pub,url_pub=url_pub,rss_links=rss_links,rss_tags=rss_tags,rss_titles=rss_titles)
            else:
                  return render_template('callback.html',total_posts=total_posts,count_length=count_length,user_profile=user_profile,user_image=user_image,user_type=user_type,pub_name=pub_name,desrip_pub=desrip_pub,image_pub=image_pub,url_pub=url_pub,rss_links=rss_links,rss_tags=rss_tags,rss_titles=rss_titles)

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
#======================================UNIT TESTING FUNCTION====================
def home_page_response():
    return 'http://127.0.0.1:5000/'

def about_page_response():
    return 'http://127.0.0.1:5000/about/'

def return_home_page_reguest():

   return requests.get('http://127.0.0.1:5000/')

def return_about_page_reguest():

   return requests.get('http://127.0.0.1:5000/about/')

def medium_test():
    medium_rss=get_medium("mmekutmfonedet")
    return type(medium_rss)
#===============================================================================

if __name__ == "__main__":
   # app.secret_key = os.urandom(12)

    app.run(debug=True)
