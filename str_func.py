def capitalize_string(input_string):
    """
    This function takes an input string and returns it in uppercase.
    """
    return input_string.upper()

def capitalize_words(input_string):
    """
    This function takes an input string and capitalizes the first letter of each word.
    """
    return ' '.join(word.capitalize() for word in input_string.split())
