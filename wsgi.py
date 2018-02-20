from flask import Flask
#from mymodule import MyModule
application = Flask(__name__)

@application.route("/")
def hello():
    '''mm = MyModule()
    c = mm.printIt()
    return c'''
    return "Hello World!"

if __name__ == "__main__":
    application.run()
