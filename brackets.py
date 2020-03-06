def checkBrackets(inStr):
    brackets = [i for i in inStr if i in "([{}])"]
    if brackets:
        try:
            roundBrackets, squareBrackets, braces = 0, 0, 0
            for i in brackets:
                if roundBrackets >= 0 and squareBrackets >= 0 and braces >= 0:
                    roundBrackets += 1 if i == '(' else -1 if i == ')' else 0
                    squareBrackets += 1 if i == '[' else -1 if i == "]" else 0
                    braces += 1 if i == '{' else -1 if i == "}" else 0
                else:
                    return False
            return True if roundBrackets == 0 and squareBrackets == 0 and braces == 0 else False
        except Exception as e:
            print('\n Error: ' + str(e))
    else:
        print('\n There are no brackets in the line.')

try:
    while True:
        inputStr = input('\n Enter the string: ')
        if inputStr:
            print("\n Is valid: ", checkBrackets(inputStr))
        else:
            print('\n Entered an empty string.')
except KeyboardInterrupt:
    pass