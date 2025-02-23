
#importing phonenumbers
import phonenumbers
#importing geocoder
from phonenumbers import geocoder
import folium
#importing key from opencage
Key="6d6f969fd9024ac8afde957f0c86a5ba"
print("Do you want to know which country the respective number belongs to..?")
n=input("Enter YES or NO: ")
if n=="YES":
    #asking the user to enter the phone number for details
    number=input("Enter phone number with Country Code:")
    check_number=phonenumbers.parse(number) 
    number_location=geocoder.description_for_number(check_number,"en")
    #printing the country to which it belonged to
    print("Country of phone number:",number_location)
print("Do you want to know service provider of respective mobile number..?")
n=input("Enter YES or NO: ")
if n=="YES":
    from phonenumbers import carrier
    service_provider=phonenumbers.parse(number)
    #printing the  service provdier name such as airtel,tata etc
    service=carrier.name_for_number(service_provider,"en")
    print("Service provider:",service)
print("Do you want to know latitude and longtitude ranges of respective mobile numbers country..?")
n1=input("Enter YES or NO: ")   
if n1=="YES":
    from opencage.geocoder import OpenCageGeocode
    geocoder=OpenCageGeocode(Key)
    query=str(number_location)
    results=geocoder.geocode(query)
    lat=results[0]['geometry']['lat']
    lng=results[0]['geometry']['lng']
#printing the latitude and longtitude ranges 
print("Latitude=",lat)
print("Longitude=",lng)
print("Do you want to know location of that mobile number..?")
n2=input("Enter YES or NO: ")   
if n2=="YES":
    #mapping the mobile number in maps using html
    map_location=folium.Map(location=[lat,lng],zoom_start=9)
    folium.Marker([lat,lng],popup=number_location).add_to(map_location)
    map_location.save("mylocation.html")
    print("open mylocation in files to see the location")
print("THANK YOU")