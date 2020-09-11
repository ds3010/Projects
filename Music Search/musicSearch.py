import albumSearch
import artistAlbSearch
import requests
import json

# TODO: Function to print all songs from a given Master'''
def printSongs(returnedDict):
    while True:
        print('\nPlease indicate which of the above albums would you like to check (Select between 1 and ' + str(len(returnedDict)) + '):')
        x = input()
        x = int(x)
        if (x < 1) or (x > len(returnedDict)):
            print('\nAlbum out of range, please select a number between 1 and ' + str(len(returnedDict)) + '): ')
        else:
            masterAPI = requests.get(returnedDict['Album ' + str(x)]['master_url'])
            masterDict = json.loads(masterAPI.text)
            print(''.center(100,'#'))
            print('Title: '+masterDict['title'])
            print('\nArtists: ')
            for j in range(len(masterDict['artists'])):
                print(masterDict['artists'][j]['name'])
            print('\nGenres:')
            for j in range(len(masterDict['genres'])):
                print(masterDict['genres'][j])
            print('\nStyles:')
            for j in range(len(masterDict['genres'])):
                print(masterDict['genres'][j])   
            print('\nYear: ' + str(masterDict['year']))    
            print('\nTracklist:')
            for j in range(len(masterDict['tracklist'])):
                print(masterDict['tracklist'][j]['position'] + '. ' + masterDict['tracklist'][j]['title'] + ' (' + masterDict['tracklist'][j]['duration'] + ')')
            print('\nThanks!, Goodbye!')
            break


# Main Code
while True:
    print('\nWhat would you like to search? (Type 1 for Artist and Type 2 for Album):')
    userSel = input()
    if userSel == '1':
        break
    elif userSel == '2':
        break
    else:
        print('Invalid input, only options 1 or 2 accepted')
if userSel == '1':
    print('\nEnter the name of the Artist:')
    printSongs(artistAlbSearch.albumSearch(input()))
if userSel == '2':
    print('\nEnter the name of the Album:')
    printSongs(albumSearch.albumSearch(input()))


# CODE BELOW ONLY FOR TESTING PURPOSES