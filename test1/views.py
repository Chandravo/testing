from django.shortcuts import render
from django.contrib.gis.geoip2 import GeoIP2
import requests

# Create your views here.
def test1(request):
    # x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')    
    # if x_forwarded_for:
    #     ip = x_forwarded_for.split(',')[0]
    # else:
    #     ip = request.META.get('REMOTE_ADDR')
    
    # device_type = ""
    # browser_type = ""
    # browser_version = ""
    # os_type = ""
    # os_version = ""    
    # if request.user_agent.is_mobile:
    #     device_type = "Mobile"
    # if request.user_agent.is_tablet:
    #     device_type = "Tablet"
    # if request.user_agent.is_pc:
    #     device_type = "PC"
    
    # browser_type = request.user_agent.browser.family
    # browser_version = request.user_agent.browser.version_string
    # os_type = request.user_agent.os.family
    # os_version = request.user_agent.os.version_string
    ip = '117.203.246.41'
    ip_response = requests.get('http://ip-api.com/json/'+ip)  
    ip_response = ip_response.json()
    location_country = ip_response['country']
    location_region = ip_response['regionName']
    location_city = ip_response['city']
    context = {
        "ip": ip,
        # "device_type": device_type,
        # "browser_type": browser_type,
        # "browser_version": browser_version,
        # "os_type":os_type,
        # "os_version":os_version,
        "location_country": location_country,
        "location_region": location_region,
        "location_city": location_city
    }    
    
    return render(request,'1.html',context)

