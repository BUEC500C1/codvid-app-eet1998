import requests
import json
from time import sleep

def api_call(country):

    url = "https://api.covid19api.com/summary"

    payload = {}
    headers= {}

    response = requests.request("GET", url, headers=headers, data = payload)
    x = response.json()
    # Stores values of keys in data
    if x["cod"] != "404":
        
        countries = x["Countries"]
        country_dict = json.loads(countries)
        for country in country_dict:
            if country == country_dict["Country"]
                num_cases = country_dict["Country"]["TotalConfirmed"]
            return num_cases
        
        else:
            print("Error!")

# Main function to receive user input and make appropriate function calls
def main():
    print("Hello. Welcome to my Covid-19 case tracker app.") ; sleep(1.0)

    while True:
        user_choice = input("Please enter a country or type Q to quit: ")

        api_call(country)
        print()

        if user_choice == "Q":
            sleep(1.0)
            print("Goodbye.")
            break

if __name__ == '__main__':
    main()