def print_upper_words(words, must_start_with=""):
    """For a list of words print out each word on separate line in uppercase"""
    if must_start_with == "": 
        for word in words:
            print(word.upper())
    else:
        for word in words:
            for char in must_start_with:
                if word.startswith(char) or word.startswith(char.upper()):
                    print(word.upper())
                    break
            
            else: return 
            
print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], must_start_with={"h", "y"})