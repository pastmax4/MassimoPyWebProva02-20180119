'''
Created on 18 gen 2019

@author: mpasteri

https://www.tutorialspoint.com/flask/flask_application.htm

http://127.0.0.1:5000/ 


-)Flask constructor takes the name of current module (__name__) as argument.

-)The route() function of the Flask class is a decorator, 
which tells the application which URL should call the associated function.

'''


from flask import Flask
app = Flask(__name__)

#---------------------------------------------------------------------------
# route
# Modern web frameworks use the routing technique to help a user 
# remember application URLs. It is useful to access the desired 
# page directly without having to navigate from the home page.
# The route() decorator in Flask is used to bind URL to a function. 

@app.route('/')
def hello_world():    
    return 'Hello World from Massimp.'

@app.route('/massimp')
def massimp():    
    return "It's me to code this."

@app.route('/hello/<name>')
def hello_name(name):    
    return 'Hello %s!' % name    
#----------------------------------------------------------
# The run() method of Flask class runs the application on the 
# local development server.
# app.run(host, port, debug, options)
# Defaults port is 5000
if __name__ == '__main__':    
    app.run()   
    
    
    
    
    