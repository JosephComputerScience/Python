"""Implement a method to perform basic string compression using the counts of repeated characters. 
For example, the string aabcccccaaa would become a2b1c5a3. 
If the "compressed" string would not become smaller than the original string, 
your method should return the original string. 
You can assume the string has only uppercase and lowercase letters(a-z)."""


#This function loops through the entire string to count the letters and stores the repeating letter
#into a string and its count into two lists the second lists which holds all the counts if it is all 1's
#then it will return the original string because it cannot be compressed

def compress(string):

    if len(string) is 0:
        return "No input"
    aryS = []
    aryI = []
    index = 0
    count = 0
    for x in range(len(string)):
        if len(aryS) is 0:
            aryS.append(string[x])
        if string[x] is aryS[index]:
            count += 1
        elif string[x] is not aryS[index]:
            aryS.append(str(count))
            aryI.append(count)
            aryS.append(string[x])
            count = 1
            index += 2
    aryS.append(str(count))
    for x in aryI:
        if x >1:
            return "".join(aryS)
    return string
