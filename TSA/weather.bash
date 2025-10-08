#!/bin/bash

API_KEY="87de8f40889f46bd84c115027251205"
LAT="17.091962"
LON="82.051405"

URL="http://api.weatherapi.com/v1/current.json?key=$API_KEY&q=$LAT,$LON"

info=$(curl -s "$URL") 

name=$(echo "$info" | jq -r '.location.name')
region=$(echo "$info" | jq -r '.location.region')
temp=$(echo "$info" | jq -r '.current.temp_c')
text=$(echo "$info" | jq -r '.current.condition.text')
wind=$(echo "$info" | jq -r '.current.wind_kph')
humid=$(echo "$info" | jq -r '.current.humidity')

echo "Temperature: $temp °C | Humidity: $humid% | Wind Speed: $wind km/h | $text | $name | $region." 
