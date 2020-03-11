article = ['A', 'An', 'The']
adjective = ['Attractive', 'Itchy', 'Smoggy', 'Obnoxious', 'Dead']
noun = ['Cat', 'Dog', 'Person', 'Love', 'Computer']
verb = ['Adopts', 'Astonishes', 'Fries', 'Fails']

def totallyCorrectEnglishSentence():
    """This method has a great name, and creates grammatically incorrect(sometimes correct) sentences"""
    for a in article:
        for b in adjective:
            for c in noun:
                for d in verb:
                    print(a, b, c, d)


print("------------------------------------------")

        
