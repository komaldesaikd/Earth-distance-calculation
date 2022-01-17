import requests
import json
from math import sin, cos, sqrt, asin, radians

def distance_cal(lat1,lat2,lon1,lon2):
    """ This Function calculates distance between 2 points based on its longitude and latitude values"""
    R = 6371.0
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)    
    dlon = lon2 - lon1
    dlat = lat2 - lat1    
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2    
    c =  2 * asin(sqrt(a))    
    distance = R * c
    return distance
  
if __name__ =="__main__" : 
    long_var1 = ''
    try:
        response = requests.get("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson").json()
        long_var1 = float(input("Enter longitude "))
        lat_var1 = float(input("Enter Latitude "))
        print()
    except Exception as e:
        print("Getting following issue!!!", e)        
    if(long_var1):
        res_dist_list = []    
        res_dict = {}
        long_lat_list = []      
        for item in response["features"]:    
            res = (item["geometry"]["coordinates"])
            title_var = (item["properties"]["title"])
            long_var2 = float(res[0])
            lat_var2 = float(res[1])
            long_lat2 = (long_var2,lat_var2)
            if (long_lat2) not in  long_lat_list:
                long_lat_list.append(long_lat2)            
                dist_var = distance_cal(lat_var1,lat_var2,long_var1,long_var2)
                res_dict[title_var] = dist_var
        sort_results = sorted(res_dict.items(), key=lambda x: x[1])
        leng = len(sort_results)    
        res_dist_list=sorted(list(set(res_dist_list)))
        ctr = 0
        for title in sort_results:
            if ctr<10:
                res_dis = round(title[1])
                print(f"{title[0]} ||  {res_dis}")
                ctr += 1
    
           

