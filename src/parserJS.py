fileName = input("Please select a JavaScript file: ")
#fileName = "test.js"
with open(fileName, "r") as file:
    HTML=file.read().split("\n")
i = 0
while(i < len(HTML)):
    if ("document.write" in HTML[i]):
        print(HTML[i][HTML[i].index("\"")+1:len(HTML[i])-3])
    i+=1