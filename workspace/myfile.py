import requests
import pandas
import sqlalchemy as db
zip_code = input("Enter a zip code")
f = requests.get("https://api.weatherapi.com/v1/forecast.json?key=23d8c98898dc4ac8b87213201223006&q=" + zip_code)
f = f.json()
for i in range(24):
  cond = f["forecast"]["forecastday"][0]["hour"][i]["condition"]
  text = cond["text"]
  f["forecast"]["forecastday"][0]["hour"][i]["condition"] = text
data = f["forecast"]["forecastday"][0]["hour"]
df = pandas.DataFrame.from_dict(data)
engine = db.create_engine('sqlite:///data_base_name.db')
df.to_sql('Hourly', con=engine, if_exists='replace', index=False)
query_result = engine.execute("SELECT * FROM Hourly;").fetchall()
print(pandas.DataFrame(query_result))
