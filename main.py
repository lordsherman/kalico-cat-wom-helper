import requests
import json

def gather_details():
    title_numb = input("What number SOTW is running this week? ")
    date = input("What day will the competition start? (MM-DD-YYYY) ")
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
    
    return title_numb, metric, date

def main():
    gather_details()
    
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

