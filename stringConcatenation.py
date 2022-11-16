def concatenateString(str1, str2):
    print(str1 + str2)
    print("".join([str1, str2]))
    print("%s%s" % (str1, str2))
    print("{}{}".format(str1, str2))

concatenateString("Hello ", "world")
