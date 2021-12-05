fileName = input("Please select a JavaScript file: ")
#fileName = "test.js"
with open(fileName, "r") as file:JS=file.read().split("\n")
i = 0
while(i < len(JS)):
    if ("document.write" in JS[i]): print(JS[i][JS[i].index("\"")+1:len(JS[i])-3])
    i+=1
