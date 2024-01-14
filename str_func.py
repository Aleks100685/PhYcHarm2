def capitalize_string(input_string):
    """
    This function takes an input string 
    """
    return input_string.upper()

def capitalize_words(input_string):
    """
    This function takes an input string and capitalizes the first letter of each words
    """
    return ' '.join(word.capitalize() for word in input_string.split())
