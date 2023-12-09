import json
import pickle
import numpy as np

locations = None
data_columns = None
model = None

def get_estimated_price(location, sqft, bhk, bath):
  try:
    loc_index = data_columns.index(location.lower())
  except:
    loc_index = -1

  xp = np.zeros(len(data_columns))
  xp[0] = sqft
  xp[1] = bath
  xp[2] = bhk
  if loc_index >= 0:
      xp[loc_index] = 1

  return round(model.predict([xp])[0], 2)

def get_location_names():
  return locations

def load_artifacts():
  print("loading artifacts STARTS...")

  global data_columns
  global locations

  with open('../model/columns.json', 'r') as f:
    data_columns = json.load(f)['data_columns']
    locations = data_columns[3:]

  global model

  if model == None:
    with open('../model/banglore_home_prices_model.pickle', 'rb') as f:
      model = pickle.load(f)

  print("loading artifacts END...")
  

if __name__ == "__main__":
  load_artifacts()
  print(get_location_names())
  print(get_estimated_price('1st Phase JP Nagar',1000, 3, 3))
  print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
  print(get_estimated_price('Kalhalli', 1000, 2, 2)) # other location
  print(get_estimated_price('Ejipura', 1000, 2, 2))  # other location