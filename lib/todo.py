def todo(input_string):
    todo_list = ["#TODO buying grocery", "#TODO buying vegetables"]
    if type(input_string) != str:
        raise Exception("Input is not a string type. Try again.")
    if "#Todo" in input_string or "#todo" in input_string:
         raise Exception("Error : #Todo should be capitalised!")
    
    if "#TODO" in input_string:
        return True
    
    return False
