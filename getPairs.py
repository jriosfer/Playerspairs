import requests
import json
# loadData: takes a URL and headers parameters for getting info from the URL endpoint
# parameter URL: this is the endpoint where the data is located in JSON format
# parameter headers: There is no need of headers for accessing this data, so it will be empty
def loadData(URL,header) :
        # making the info request to the endPoint
        URLrequest=requests.get(URL,headers=header)
        #storing the information to "result" variable
        result=URLrequest.json()
        return result
# takes the input from console of height
def getInput():
     while True:
        try :
           result = int(input("Introduce height in inches adds up to:"))
           break
        except ValueError:
            print("Please introduce a number")
     return result
# program starting point
totalHeight = getInput()
    
# url hardcoded
url='https://mach-eight.uc.r.appspot.com'
# load data into result (as a dcitionary) variable from url
Dataresult=loadData(url,{})
print(type(Dataresult))
for data in Dataresult['values'] :
    print(data)		