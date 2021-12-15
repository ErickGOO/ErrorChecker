from flask import Flask
application = Flask(__name__)

@application.route('/')

def index():
    return 'holis Esponjtas'

if __name__ =="__main__":
	application.run('0.0.0.0',port=80)