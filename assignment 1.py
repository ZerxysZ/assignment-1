translations = {
    "CU": "see you",
    ":)": "I'm happy",
    ":(": "I'm unhappy",
    ";)": "wink",
    ":-P": "stick out my tongue",
    "(`.`)": "sleepy",
    "TA": "totally awesome",
    "CCC": "Canadian Computing Competition",
    "CUZ": "because",
    "TY": "thank-you",
    "YW": "you're welcome",
    "TTYL": "talk to you later"
}

while True:
    phrase = input("Enter phrase> ")
    if phrase == "TTYL":
        print("talk to you later")
        break
    elif phrase in translations:
        print(translations[phrase])
    else:
        print(phrase)
