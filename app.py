# Hng9 Backend Stage 1 Task
# Create an (GET) api endoint that returns a json response

from crypt import methods
import enum
from flask import *
import json
from flask_cors import CORS, cross_origin


app = Flask(__name__)
# CORS(app)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/', methods=['GET'])
# @cross_origin(supports_credentials=True)
@cross_origin()

def home_page():
    data_set = {'slackUsername': '@eshi', 'backend': True, 'age' : 32, 'bio' : 'An enterpreneur, got a lot of experience with Php and taking up a new challenge using Python'}
    json_dump = json.dumps(data_set)
    return json_dump

# Task 2. Hng internshipt

@app.route('/arith', methods=['POST'])
def arithmetic():
  if request.method == 'POST':
      operation = request.json["operation_type"]
      x = request.json['x']
      y = request.json['y']
      slackUsername = '@eshi'

      if operation == 'addition':
        sum = int(x) + int(y)
        data = { "slackUsername": slackUsername, "result": sum, "operation_type" : operation }

        response = json.dumps(data)
        return Response(response, mimetype='application/json')

      elif operation == 'subtraction':
        subtract = int(x) - int(y)
        data = { "slackUsername": slackUsername, "result": subtract, "operation_type" : operation }

        response = json.dumps(data)
        return Response(response, mimetype='application/json')

      elif operation == 'multiplication':
        multiply = int(x) * int(y)
        data = { "slackUsername": slackUsername, "result": multiply, "operation_type" : operation }

        response = json.dumps(data)
        return Response(response, mimetype='application/json')

      else:
        return {"response": "Operation should be addition, subtraction or  multiplication"}
    
  return "Error processing your Operations!!!"





if __name__ == '__main__':
  app.run(debug=True)
  