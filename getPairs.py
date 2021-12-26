import requests
from collections import defaultdict

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

# parameters:
#  data: Dictionary with players Info
#  totalHeight: the total height of the players' pair
def createHeightDictionary(data, totalHeight):
    # create an empty dictionary with heights
    dictPairs = defaultdict(list)
    # check if
    print(type(dictPairs))
    for player in data:
        try:
            # takes playerHeight of each player record and validates data quality
            playerHeight = int(player['h_in'])
        except ValueError:
            print("Height is not an integer value on player:" + player['first_name'] + " " + player['last_name'])

        # add player to the dictionary
        dictPairs[playerHeight].append(player['first_name'] + " " + player['last_name'])
        # print(dictPairs)

    return dictPairs
# program starting point
totalHeight = getInput()
    
# url hardcoded
url='https://mach-eight.uc.r.appspot.com'
# load data into result (as a dcitionary) variable from url
Dataresult=loadData(url,{})
print(type(Dataresult))
for data in Dataresult['values'] :
    print(data)		

playersHeight = createHeightDictionary(Dataresult['values'],totalHeight)
print(playersHeight)
# search pairs depends on each heigh against another player
print("The pairs of basketball players that added up:["+ str(totalHeight)+"] inches are:")
for height in playersHeight:
    # print(height)
    if totalHeight - height in playersHeight:
      for otherPlayer in playersHeight[totalHeight - height] :
          for player in playersHeight[height]:
                 #print("player:"+player)
                 if player < otherPlayer:
                       print("["+player + " - " + otherPlayer+"]")
                       