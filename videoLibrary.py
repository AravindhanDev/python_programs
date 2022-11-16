def calculateTotalCharges(newVideosValue, oldVideosValue):
    totalCharges = 0
    newVideos = int(input("Enter no of new videos: "))
    oldVideos = int(input("Enter no of new videos: "))
    totalCharges = ((newVideos * newVideosValue) + (oldVideos * oldVideosValue))
    return totalCharges


newVideosValue = 75
oldVideosValue = 50
totalCharges = calculateTotalCharges(newVideosValue, oldVideosValue)
print("Total Charges: ", totalCharges)

