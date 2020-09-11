import requests
import json
import time
import sys

def albumSearch(userInput):
    #THE FIRST TASK IS TO KNOW THE TOTAL NUMBER OF PAGES AND ITEMS FOUND
    initAns = requests.get('https://api.discogs.com/database/search?artist=' + userInput + '&token=KtehgpFdeuBMDRZZvmFDSZWtJCMpAthaUdUKmLmV')
    initDict = json.loads(initAns.text)
    numPages = initDict['pagination']['pages']
    if numPages >= 100:
        print('\nTHE NUMBER OF POSSIBILITIES IS HIGHER THAN 5,000 AND THE CODE IS UNABLE TO CONTINUE, PLEASE TRY AGAIN WITH A MORE DESCRIPTIVE SEARCH')
        sys.exit()
    numItems = initDict['pagination']['items']
    '''
    >newDict is a Dictionary that saves every album with a unique master ID, along with its title, master URL and year
    if existing.
    >albCount is an integet that will be incremented by one everytime a new album is found.
    >masterList will keep a list of unique master IDs.
    >itemsToGo will be used to know when to stop searching
    '''
    newDict = {}
    albCount = 0
    masterList = []
    itemsToGo = numItems
    # We need to search each page individually, each one will give us a new list of 50 albums to play with
    for x in range(numPages):
        # THE API HAS A LIMITATION WITH THE NUMBER OF REQUESTS YOU CAN MAKE
        # THIS FORCES ME TO PUT A DELAY BEFORE EACH GET REQUEST
        time.sleep(0.5)
        initAns = requests.get('https://api.discogs.com/database/search?artist=' + userInput + '&token=KtehgpFdeuBMDRZZvmFDSZWtJCMpAthaUdUKmLmV&page=' + str(x+1))
        initDict = json.loads(initAns.text)
        #If there is only one page, then there are only 50 albums or less, so the for loop has to stop at "itemsToGo"
        if itemsToGo <= 50:
            #JUST TO SEARCH FOR BUGS, PRINT THE PAGE NUMBER RIGHT BEFORE THE ERROR:
            #print('Page ' + str(x+1))
            for y in range(itemsToGo):
                #Here we only add an album, title, master_id and year if the master_id exists, if it is higher than ZERO,
                #different than "NONE" and it has not been added yet to the masterList
                
                #JUST TO SEARCH FOR BUGS, PRINT THE ITEM NUMBER RIGHT BEFORE THE ERROR:
                #print('item ' + str(y+1))
                if (('master_id' in initDict['results'][y].keys()) and (initDict['results'][y]['master_id'] != None) 
                and (initDict['results'][y]['master_id'] not in masterList) and (initDict['results'][y]['master_id'] > 0)):
                    #Let's add the master ID number to the master list and increament albCount by one
                    masterList.append(initDict['results'][y]['master_id'])
                    albCount = albCount + 1
                    #Finally we create the Album object, and its value is a nested Dictionary with a title, year and masterID
                    #Sometimes the year is not included as a key:value pair, in that case, save it as "Unknown Year"
                    newDict.setdefault('Album ' + str(albCount), {})
                    newDict['Album ' + str(albCount)].setdefault('title',initDict['results'][y]['title'])
                    if 'year' not in initDict['results'][y].keys(): 
                        newDict['Album ' + str(albCount)].setdefault('year','Unknown Year')
                    if 'year' in initDict['results'][y].keys():
                        newDict['Album ' + str(albCount)].setdefault('year',initDict['results'][y]['year'])
                    newDict['Album ' + str(albCount)].setdefault('master_id',initDict['results'][y]['master_id'])
                    #Let's also save the master_URL so it can be used later to get the tracklist
                    newDict['Album ' + str(albCount)].setdefault('master_url',initDict['results'][y]['master_url'])
        #Now let's do the same but when the number of items are higher than 50. In that case, we know there is a new page coming next
        #So the only difference is that the loop goes up to range(50) and then itemsToGo is decreased by 50 for the next iteration
        if itemsToGo > 50:
            #JUST TO SEARCH FOR BUGS, PRINT THE PAGE NUMBER RIGHT BEFORE THE ERROR:
            #print('Page ' + str(x+1))
            for y in range(50):
                #JUST TO SEARCH FOR BUGS, PRINT THE ITEM NUMBER RIGHT BEFORE THE ERROR:
                #print('item ' + str(y+1))

                # A BUG WAS FOUND IN THE API: ONE OR MORE NON-LAST PAGES DO NOT HAVE 50 ITEMS BUT LESS, SO WHEN GETTING INTO THE 50th 
                # ITERATION THE LIST-INDEX RETURNS AN ERROR, THE TRY AND EXCEPT HERE BELOW ARE USED TO FIX THAT. 
                # THIS WAS FOUND ON THE SEARCH FOR STRING "STARS" ON PAGE 23 (ONLY 49 ALBUMS LISTED)
                try:
                    if (('master_id' in initDict['results'][y].keys()) and (initDict['results'][y]['master_id'] != None) and 
                    (initDict['results'][y]['master_id'] not in masterList) and (initDict['results'][y]['master_id'] > 0)):
                        masterList.append(initDict['results'][y]['master_id'])
                        albCount = albCount + 1
                        newDict.setdefault('Album ' + str(albCount), {})
                        newDict['Album ' + str(albCount)].setdefault('title',initDict['results'][y]['title'])
                        if 'year' not in initDict['results'][y].keys(): 
                            newDict['Album ' + str(albCount)].setdefault('year','Unknown Year')
                        if 'year' in initDict['results'][y].keys():
                            newDict['Album ' + str(albCount)].setdefault('year',initDict['results'][y]['year'])
                        newDict['Album ' + str(albCount)].setdefault('master_id',initDict['results'][y]['master_id'])
                        newDict['Album ' + str(albCount)].setdefault('master_url',initDict['results'][y]['master_url'])
                except IndexError:
                    continue
            itemsToGo = itemsToGo - 50            
    
    #Now let's print the results and return the newDict Dictionary
    print(str(albCount) + ' Albums Found')

    for k, v in newDict.items():
        print('\n' + k + ': ')
        print(v.get('title', 'error'))
        print('(' + v.get('year', 'error') + ')')
        print(v.get('master_id', 'error'))

    return newDict

#albumSearch('')