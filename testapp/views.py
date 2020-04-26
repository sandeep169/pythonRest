from django.shortcuts import render,redirect
#from django.http import HttpResponse
#from django.contrib.auth.models import User,auth
import requests

#---Requests--- allow you to send HTTP/1.1 requests.
# You can add headers, form data, multi-part files,
# and parameters with simple Python dictionaries,
# and access the response data in the same way --- for example below
# import requests
# req = requests.get('https://www.edureka.co/')
#https://www.edureka.co/blog/python-requests-tutorial/




#---------------API Fetch-----------

URL ="http://127.0.0.1:8000"
#we will provide username and password and in return we want to see token
# from pythonRest/myapi/api/UserAuthentication
def index(request):
    return render(request,'client.html')
def get_token():
        url ="http://127.0.0.1:8000/api/auth/"
        # an HTTP requests is send to get the token from running server of another project
        # where i have created an api and fetching data through api
        # token is need to access the data as i have set security
        response = requests.post(url, data={'username': 'sandeep', 'password': 'sandeep'})
        # i pass the credentials to fetch the token
        # all the information is stored somewhere, correct?
        # Yes, it is stored in a Response object
        return response.json()

def get_data (request):
    url=f'{URL}/api/user_list/'
    token = get_token()
    header = {'Authorization': f'Token {token}'}
    # It is fairly straightforward to send an HTTP request using Requests

    # URL and header is passed in http request to get the data using --requests--
    response = requests.get(url,headers=header)
    #the information is stored in Response object

    emp_data=response.json()
    # for e in emp_data:
    #     print(e)

    return render(request,'client.html',{'obj': emp_data})