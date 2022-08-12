from decouple import config
import requests
import json

def main():
    title_numb = input("What number SOTW is running this week? ")
    date_start = input("What day will the competition start? (YYYY-MM-DD) ")
    date_end = input("What day will the competition end? (YYYY-MM-DD) ")
    wom_code = config('WOM')
    
    usable_metrics = open("usable-metrics.txt", "r")
    metric_list = [line.strip() for line in usable_metrics]
    usable_metrics.close()
    
    valid_metric = True
    while valid_metric:
        metric = input("What is this weeks skill? (lowercase skill name) ")
        if metric not in metric_list:
            print("Please enter a usable metric. Skills need to be all lowercase.")
        else:
            valid_metric = False
    
    payload = {
                "title": "Kalico Cat SOTW " + title_numb, 
                "metric": metric, 
                "startsAt": date_start + "T12:00:00.000Z", 
                "endsAt": date_end + "T12:00:00.000Z", 
                "groupId": "909", 
                "groupVerificationCode": wom_code
            }
    
    
if __name__ == '__main__':
    main()

# Example POST Payload
# {
#   "title": "Fishing SOTW", 
#   "metric": "fishing", 
#   "startsAt": "2020-12-21T19:00:00.000Z", 
#   "endsAt": "2020-12-27T19:00:00.000Z", 
#   "groupId": "909", 
#   "groupVerificationCode": "ENV"
# }

