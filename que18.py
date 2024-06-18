# 18. Write a python program that checks if two strings are anagrams of each other. 
def are_anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    return sorted(str1) == sorted(str2)

string1 = "Listen"
string2 = "Silent"
ans = are_anagrams(string1,string2)
print(ans)
