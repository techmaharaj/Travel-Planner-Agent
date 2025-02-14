import requests
import json
import os
def get_weather(city, api_key):
    """
    Fetches weather data for a given city using the provided API key.
    
    Args:
        city (str): The name of the city.
        api_key (str): The API key for the weather API.
        
    Returns:
        str: A JSON string containing the weather information,
             or an error message if something goes wrong.
    """
    if not city:
        return "Error: City must be provided."
    if not api_key:
        return "Error: API_KEY environment variable must be set."
    api_url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        res = json.loads(response.content.decode('utf-8'))
        weather_data = {
            'temp': res['current']['temp_c'],
            'wind_speed': res['current']['condition']['text'],
            'weather_code': res['current']['cloud']
        }
        # Convert weather code to a readable condition
        weather_code = weather_data['weather_code']
        if 0 < weather_code < 10:
            weather_data['weather'] = "Mainly Clear"
        elif 40 < weather_code < 50:
            weather_data['weather'] = "Fog"
        elif 50 < weather_code < 56:
            weather_data['weather'] = "Drizzle"
        elif 60 < weather_code < 70:
            weather_data['weather'] = "Light Rain"
        else:
            weather_data['weather'] = "Rain"
        return json.dumps(weather_data)
    except requests.exceptions.RequestException as e:
        return f"Request Error: {e}"
    except json.JSONDecodeError as e:
        return f"JSON Decode Error: {e}"
    except KeyError as e:
        return f"Key Error: {e}. Check the API response."
    except Exception as e:
        return f"General Error: {e}"
if __name__ == "__main__":
    city = os.getenv("CITY")
    api_key = os.getenv("API_KEY")
    result = get_weather(city, api_key)
    print(result)  # Print the result to stdout
