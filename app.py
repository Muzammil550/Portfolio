# inside flask module there is a class #called Flask
from flask import Flask, render_template

# create an instance of Flask, __name__ is main
app = Flask(__name__)
# register/create a route and then call the function
@app.route('/')

###
def hello():
  return render_template('index.html')
if __name__ == '__main__':
    app.run( host = '0.0.0.0', debug=True)
  


 