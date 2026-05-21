import requests
from datetime import datetime, timedelta
import pandas as pd 

today_date = datetime.now()
print ("Today's date:", today_date)
week_ago = today_date - timedelta(days=7)

start_date = week_ago.strftime("%Y-%m-%d")
end_date = today_date.strftime("%Y-%m-%d")
print("Start date:", start_date)
print("End date:", end_date)


url = f"https://api.open-meteo.com/v1/forecast?latitude=48.85&longitude=2.35&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"
response = requests.get(url)
data = response.json()

df = pd.DataFrame({
    
     "date" : data["daily"]["time"],
     "max_temp" : data["daily"]["temperature_2m_max"],
     "min_temp" : data["daily"]["temperature_2m_min"]
})
print(df)