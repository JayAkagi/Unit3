def todo(input_string):
    if type(input_string) != str:
        raise Exception("Input is not a string type. Try again.")
    
    if "#TODO" in input_string:
        return True
    
    return False
