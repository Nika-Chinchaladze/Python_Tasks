import requests
from datetime import datetime
import os


# ================================ NUTRITIONIX PART =================================== #
my_id = os.environ.get("MY_ID")
my_key = os.environ.get("MY_KEY")

my_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
my_header = {
    "x-app-id": my_id,
    "x-app-key": my_key
}
query = input("Tell me which exercise you did? ")
exercise_info = {
    "query": query,
    "gender": "male",
    "weight_kg": 85.5,
    "height_cm": 185.64,
    "age": 25
}
response = requests.post(url=my_endpoint, json=exercise_info, headers=my_header)
print(response.status_code)
result = response.json()['exercises'][0]
user_input = result["name"].title()
duration_min = result["duration_min"]
calories = result["nf_calories"]

# ================================ CURRENT DATE PART =================================== #
today = datetime.now()
current_date = today.date()
current_time = today.time()
current_date = current_date.strftime("%d/%m/%Y")
current_time = current_time.strftime("%X")

# ================================ SPREADSHEET PART =================================== #
sheet_token = os.environ.get("SHEET_TOKEN")
sheet_id = os.environ.get("SHEET_ID")
project_name = os.environ.get("PROJECT_NAME")

sheet_header = {
    "Authorization": sheet_token
}

sheet_info = {
    "workout": {
        "date": current_date,
        "time": current_time,
        "exercise": user_input,
        "duration": duration_min,
        "calories": calories
    }
}

sheet_endpoint = f"https://api.sheety.co/{sheet_id}/{project_name}/workouts"
send_post = requests.post(url=sheet_endpoint, json=sheet_info, headers=sheet_header)
print(send_post.status_code)
print(send_post.text)
