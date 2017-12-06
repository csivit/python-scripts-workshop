# coding: utf-8

#    .o88b.   .d8888.   d888888b 
#   d8P  Y8   88'  YP     `88'   
#   8P        `8bo.        88    
#   8b          `Y8b.      88    
#   Y8b  d8   db   8D     .88.   
#    `Y88P'   `8888Y'   Y888888P 


# Requirements: pip install requests

# above line is added as in copying and pasting text some non ASCII characters can come, to make them valid we use this

# READ ME: The script fetches the data from the google geo api and prints the formatted address. Used to learn json and requests basics
# REQUIREMENTS: requests module

import urllib.parse
import requests

main_api = 'https://maps.googleapis.com/maps/api/geocode/json?'
while True:
    try:
        print('\n============ RESTARTING ============\n')
        address = input('Address: ')

        if address == 'quit' or address == 'q' or address == 'Q':
            print('\n Thank You for using our service :)')
            break

        url = main_api + urllib.parse.urlencode({'address': address}) #useful as it converts space or two words etc and takes care of it
        print(url)
        json_data = requests.get(url).json() # requesting and getting the data and converting to json 

        json_status = json_data['status'] # json_data is  a dictionary which we can get data from
        print('API Status: ' + json_status)
        if(json_status == 'ZERO_RESULTS'):
            print("""
            ╔╦╗┬ ┬┌─┐  ┌─┐┌┬┐┌┬┐┬─┐┌─┐┌─┐┌─┐  ┬┌─┐┌┐┌┌┬┐  ┌─┐┌─┐┌┐┌┌─┐┬┌┐ ┬  ┌─┐  ┬ ┬┌─┐┬ ┬  ╔╦╗╦ ╦╔╦╗╔╗ ╔═╗  ┬
             ║ ├─┤├┤   ├─┤ ││ ││├┬┘├┤ └─┐└─┐  │└─┐│││ │   └─┐├┤ │││└─┐│├┴┐│  ├┤   └┬┘│ ││ │   ║║║ ║║║║╠╩╗║ ║  │
             ╩ ┴ ┴└─┘  ┴ ┴─┴┘─┴┘┴└─└─┘└─┘└─┘  ┴└─┘┘└┘ ┴   └─┘└─┘┘└┘└─┘┴└─┘┴─┘└─┘   ┴ └─┘└─┘  ═╩╝╚═╝╩ ╩╚═╝╚═╝  o
             """)
        else:
            formatted_address = json_data['results'][0]['formatted_address']  # list inside results and dictionary inside it
            print()
            print(formatted_address)
    
    except KeyboardInterrupt:
        print('\n Thank You for using our service :)')
        break
    except:
        raise