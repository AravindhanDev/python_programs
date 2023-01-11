from datetime import datetime, date
 
def calculateAge(birthDate):
    today = date.today()
    age = today.year - birthDate.year -((today.month, today.day) < (birthDate.month, birthDate.day))
    return age

def orderDates(friendsDict):
    newList = []
    for key in friendsDict:
        newList.append(friendsDict[key])
    newList.sort(key=lambda date: datetime.strptime(date, "%d-%m-%Y"))
    newDict = {}
    for item in newList:
        for key in friendsDict:
            if item == friendsDict[key]:
                newDict[key] = item
    print(newDict)

            
def checkOrAddFriends(friendsDict, name):
    if name in friendsDict: return
    friendsDict[name] = input("Enter dob ")

friendsDict = {
}

checkOrAddFriends(friendsDict, 'prakash')
checkOrAddFriends(friendsDict, 'ashok')
checkOrAddFriends(friendsDict, 'aravindhan')
orderDates(friendsDict)

