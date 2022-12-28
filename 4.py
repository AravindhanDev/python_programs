def seriesGenerator(str1, str2):
    seriesList = []
    for i in str1:
        seriesList.append(i + str2)
    return seriesList

str1 = input("Enter string1: ")
str2 = input("Enter string2: ")
res = seriesGenerator(str1, str2)
print(res)
