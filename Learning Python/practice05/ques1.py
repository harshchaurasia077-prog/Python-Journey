hindi_dict={"tum":"You","kaam":"work","lund":"Penis"}
key=input("Enter the name")
if hindi_dict.get(key)==None:
    print("Enter a valid word")
else:    
    print(hindi_dict.get(key))