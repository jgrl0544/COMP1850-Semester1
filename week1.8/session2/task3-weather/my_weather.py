
import httpx
import pandas as pd
import matplotlib.pyplot as plt
import sys
import sys

def fahrenheit_to_celsius(f):
    return (f - 32) * (5/9)

api_key="U6KXJTZC2E8VGH39PD7UMG4BZ"   # your API key

city="Leeds"     # city location
country="UK"     # country location

elements = "include=days&elements=tempmax,tempmin,temp"   # request history of temperature data for Leeds

# URL location of the API for time history forecasts
base = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"

# construct the URL string for the API call
url = base + city + "," + country + "?key=" + api_key + "&" + elements

# http request
response = httpx.get(url)

# status code (should be checked)
print(response.status_code)

# get sucessful code is 200.
if (response.status_code != 200):
    sys.exit(f"Error: Status code is {response.status_code}. Please check your request or try again later!")

# json data
data = response.json()

# raw data output
print(data)

# extract the temperature data as lists from the JSON dictionary
temp_data = data['days']

print(temp_data)

# use pandas to convert data to dataframe

df = pd.DataFrame(temp_data)

df = df.map(lambda x : fahrenheit_to_celsius(x)) # maps all elements in the dataframe to their celsius counterparts.

# using matplotlib plot the 3 data sets: (tempmin,temp,tempmax) as line graphs

plot = df.plot()

# you need to change the actual dataframe's return value, not plt.  
plot.set_xlabel("Day")
plot.set_ylabel("Temperature (C)")
plot.set_title("Temperature in Leeds over the last 14 days")

plt.show()

# annotate the graph with axis labels DONE

# note that temperature is in Farenheit (F)
# convert to Celcius before plotting DONE

def celsius_to_fahrenheit(celsius):
    return (celsius * 1.8) + 32

# using the documentation explore other data, eg. rainfall  
