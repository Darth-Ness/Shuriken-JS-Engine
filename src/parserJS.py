code = ["document.write(\"Hello There\");"]
i = 0
while(i < len(code)):
    if ("document.write" in code[i]):
        print(code[i][code[i].index("\"")+1:len(code[i])-3])
    i+=1