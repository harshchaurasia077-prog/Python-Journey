def filter(str1,word,):
    newstr=str1.replace(word,"")
    return newstr.strip()
message="I am learning Python. Python is a programming language. I love Python."
print(filter(message,"Python"))