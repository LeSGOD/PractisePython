def backwords():
    sentence = input("What will you type? ")
    check = sentence.split()
    backwords = []
    for i in range(1, len(check) + 1):
        backwords.append(check[len(check) - i])
    
    result = " ".join(backwords)
    print(result)

backwords()