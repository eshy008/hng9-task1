# Hng9 Backend Stage 1 Task
# Create an (GET) api endoint that returns a json response

from flask import *
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home_page():
  data_set = {'slackUsername': '@eshi', 'backend': True, 'age' : 32, 'bio' : 'An enterpreneur, got a lot of experience with Php and taking up a new challenge using Python'}
  json_dump = json.dumps(data_set)

  return json_dump



if __name__ == '__main__':
  app.run()