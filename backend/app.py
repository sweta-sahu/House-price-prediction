from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/location_names', methods = ['GET'])
def get_location_names():
  response = jsonify({
    'locations': util.get_location_names()
  })
  response.headers.add('Access-Control-Allow-Origin', '*')

  return response

@app.route('/predict_prices', methods = ['POST'])
def get_predicted_prices():
  total_sqft = float(request.form['total_sqft'])
  location = request.form['location']
  bhk = int(request.form['bhk'])
  bath = int(request.form['bath'])

  response = jsonify({
    'estimated_house_price': util.get_estimated_price(location, total_sqft, bhk, bath)
  })
  response.headers.add('Access-Control-Allow-Origin', '*')
  return response

if __name__ == "__main__":
  util.load_artifacts()
  app.run()