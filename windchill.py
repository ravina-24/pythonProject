try:
    temperature= float(input("Enter temperature :"))
    windSpeed = float(input("Enter windspeed  :"))

    if temperature < 50 and  windSpeed >=3 and windSpeed < 120 :
         v = pow(windSpeed ,0.16)
         windChill = 35.74 + 0.6215 *temperature +( 0.4275 * temperature - 35.75 ) * v
         print( "Windchill  = {} ".format(windChill))   
     
except ValueError:
    print("sorry , you can not enter string value !")
else :
    print("Invalid input")
