from flask import Flask
from flask import make_response
application = Flask(__name__)

@application.route("/")
def hello():
    return "<h1 style='color:blue'>Hello World!</h1>"

@application.route('/<page_name>')
def other_page(page_name):
    response = make_response('The page named %s does not exist.' \
                             % page_name, 404)
    return response

if __name__ == "__main__":
    application.run(host='0.0.0.0')
