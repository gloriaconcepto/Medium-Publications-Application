# PROJECT TITLE:  MEDIUM PUBLICATIONS

## PROJECT DESCRIPTION:
An application that displays a user's Medium posts.On submission the app will display
the following:
1) The user's name

2) The user's avatar/image if available.

3)Number of publications subscribe by the user
 
4) Links to user's 5 recent posts.

5)The tags each post has.


Trello Project Link:https://trello.com/b/HIH0JJck/medium-publication-app

## HEROKU LINK TO THE APP:
Link: https://gloriamediumapp2.herokuapp.com/
               
## SET UP FOR INSTALLING THE APP AND RUN UNIT TEST :
                                                   
   1) Clone the repository to your local machine favourite directories:
  
   2) From your cmd (windows) cd your directory to Script directory:
     ###
        eg  yourfavouritedirectory/mediumapp/venv/Scripts/
        
   3) Activate your virtual environment by typing "activate" once inside the Script directory in your cmd..
     ###
        -activate
 
 4)Installing dependencies
    
   ###
           pip install -r requirements.txt
  
  
   5)Change your directory to the folder name "app" which is inside the "mediumapp" folder
     ###
        eg yourfavouritedirectory/mediumapp/app/
        
        
  ### HOW TO RUN THE MAIN APP :
                               Set up your mlab(https://mlab.com) or use the default setting.
                               Install ngrok if not install in your system already
                               Run ngrok 
                               In the ngrok type:  ngrok http 5000
                               create a medium account link:https://medium.com/
                               Go to setting >Developers>Manage Applications
                               Generate Client ID and ClientSecret
                               For callback url link:
                                    copy the https links from the ngrok link and insert it e.g
                                    "yournewngroklink"/resultDisplay/callback/medium
                              Click save.
                              
                              Open app.py script inside the app folder which is inside the mediumapp folder,with your favourite py ide.
                              
                              Assign the following values to the following variables:
                              
                              medium_app_id="paste your ClientID gotten from medium here"

                              medium_app_secret = "paste your ClientSecret gotten from medium here"
                              
                              
                              ngrok_link ="paste https ngrok link gotten from ngrok"
                              
                              save the script..
                              
                              On your cmd change to directory to directory which contain the app.py (which inside the app folder that is                               inside the mediumapp folder)e.gyourfavouritedirectory/mediumapp/app/app.py
                              
                              Type:app.py (this is to run the application) 
                              
                              POSSIBLE ERRORS:
                              NOT ACTIVATING THE VIRTUAL ENIVRONMENT
                              WRONG PASTING OF CLIENTID,CLIENTSECRET in the app.py script.(Be careful)
                              
                              WRONG SETTING OF YOUR CALL BACK URL:
                                 IF CONFUSE CHECK THIS EXAMPLE BELOW TO GET A GLUE..
                                 E.G https://e9954aa6.ngrok.io/resultDisplay/callback/medium 
                                 
                             NOT INSTALLING MLAB PROPERLY
                             Please check the link below:
                             link:https://docs.mlab.com/
                             
                             If really confuse just send me a message via link:https://twitter.com/gloriaconcepto
    
 ### HOW TO RUN UNIT TEST : 
                     Ensure mlab is properly setup or use the default setting
                     Ensure all dependencies are install
                     Activate your Virtual environment
                     Run the app.py 
                     Run the unitestbasecase.py(which inside the app folder that is inside the mediumapp             
                     folder)e.gyourfavouritedirectory/mediumapp/app/unitestbasecase.py
                     
                     
                     POSSIBLE ERRORS:
                       Running unitestbasecase.py before running app.py.Always run the app.py first before the  unitestbasecase.py 
                       
                       NOT ACTIVATING THE VIRTUAL ENIVRONMENT
                        
                         NOT INSTALLING MLAB PROPERLY
                             Please check the link below:
                             link:https://docs.mlab.com/
                             
                             If really confuse just send me a message via link:https://twitter.com/gloriaconcepto
                     
 
                                                     
                                               
 
### Programming Language:
               
               Python 3.7.o

### Programming Ide:

       pyscripter,Atom

### Frameworks:
          
          Flask8,monogdb,

### Python tools/Libraries: 

         python-virtual,flask-wtf,mysql.connector,requests

### Markup Languages: 
             
             JSON,HTTP,HTML5,CSS

## APPLICATION ARCHITECTURE

![alt text](MediumAppArchitecture.PNG "APPLICATION ARCHITECTURE")

## APPLICATION WORK FLOW

![alt text](MediumAppWorkFlow.PNG "ARCHITECTURE WORK FLOW")

## APPLICATION HOME PAGE

![alt text](MediumAppHomePage.PNG "ARCHITECTURE HOME PAGE")

## APPLICATION ABOUT PAGE

![alt text](MediumAppAboutPage.PNG "ARCHITECTURE ABOUT PAGE")

## APPLICATION RESULT PAGE

![alt text](MediumAppResultPage.PNG "ARCHITECTURE RESULT PAGE")


