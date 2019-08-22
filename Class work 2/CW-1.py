import pyowm

locate = input("Write your location: ")
owm = pyowm.OWM('ef2206ff5da67de63306d0b143e20872')  # You MUST provide a valid API key

# Have a pro subscription? Then use:
# owm = pyowm.OWM(API_key='your-API-key', subscription_type='pro')

# Search for current weather in London (Great Britain)
observation = owm.weather_at_place(str(locate))
w = observation.get_weather()
#print(w)                      # <Weather - reference time=2013-12-18 09:20,
                              # status=Clouds>

# Weather details
a= w.get_wind()                 # {'speed': 4.6, 'deg': 330}
b= w.get_humidity()              # 87
c= w.get_temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}

# Search current weather observations in the surroundings of
# lat=22.57W, lon=43.12S (Rio de Janeiro, BR)
observation_list = owm.weather_around_coords(-22.57, -43.12)

print("Current wind: {}\nThe humidity is: {}\nThe temperature is: {}".format(a['speed'], b, c['temp']))
more_info = int(input("For more details write 1 \nFor exit write 2 "))
while True:
    if more_info ==1:
        print("\n\nDetailed prognoz\n\nCurrent wind: {}\nThe deg is: {}\nThe temperature is: {}".format(a['speed'], a['deg'], c['temp']) +
              "\nThe maximum temperatura is: {}\nThe minimal temperatura is:{}".format(c['temp_max'], c['temp_min']))
    elif more_info == 2:
         print("Thanks for using our prognoz")
         break
    else:
         print("Wrong input! Try again")
         continue