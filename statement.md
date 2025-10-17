# Problem Description

# User wants to find out if their tasks is in their list.

# User wants to find their tasks in their notes contains "#TODO".

# If the specifc task doesnt contain "#TODO" it must return False. Else, it

# it will return True.

# Must have task after or before #TODO

# =============================================================================
# ====================== FUNCTION TODO ========================================


# Allows the user to check list for exisiting, #TODO strings.
def todo(input_string):
    todo_list = ["#TODO buying grocery", "#TODO buying vegetables"]
    if type(input_string) != str:
        raise Exception("Input is not a string type. Try again.")
    if "#Todo" in input_string or "#todo" in input_string:
         raise Exception("Error : #Todo should be capitalised!")
    
    if "#TODO" in input_string:
        return True
    
    return False


# =========================================================

# ============ TESTS SCENARIOS ============================

# we need to find out the function todo is an instance
# of a function.

# TEST RESULT = function Instance exist
def test_todo_is_a_function():
    result = todo("")
    assert isinstance(result, bool)

# we need to find out our input of the function should be
# a string

# TEST RESULT = input is validated as string
def test_validate_input_is_string():
    input_string = "testing string"
    result = todo(input_string)
    assert isinstance(input_string, str)

# if our input is not string, an error is expected.
# TEST RESULT = It detects the input if its a string or not. and throw error if appropriate
def test_throw_an_error_if_input_is_not_string():
    with pytest.raises(Exception) as e:
        todo(10)
    error_message = str(e.value)
    assert error_message == "Input is not a string type. Try again."

# does user_input string, contains #todo
# if it has #todo, it returns true

# TEST RESULT = Validates if string contains #TODO, returns true if it does
def test_confirm_if_input_string_contains_todo():
    input_string = "I am a random string to be checked #TODO"
    result = todo(input_string)
    assert result == True

# if it does not contain #todo, it returns false
# TEST RESULT = Validates if string does not contain #TODO, returns false if it not
def test_confirm_if_input_string_does_not_contains_todo():
    input_string = "I am a random string to be checked"
    result = todo(input_string)
    assert result == False



# validate if instance of the list is a list.

# TEST RESULT = It looks for list then validate List exist
def test_check_if_todo_list_is_a_instance_of_a_list():
    input_str = "#TODO buying grocery"
    todo_list = ["#TODO buying grocery", "#TODO buying vegetables"]
    todo_fn = todo(input_str)
    assert isinstance(todo_list, list)
 

# confirm if we have correct amount of todo things in the
# existing list.
# TEST RESULT = Validate count of list items
def test_check_if_todo_list_has_a_right_length():
    input_str = "#TODO buying grocery"
    todo_list = ["#TODO buying grocery", "#TODO buying vegetables"]
    todo_fn = todo(input_str)
    assert len(todo_list) == 2


# Ensure #todo is capitalised.
# TEST RESULT = Validate if 'TODO' was capitalised
def  test_check_if_todo_input_str_is_capitalised():
     input_str = "#TODO buying grocery"
     todo_fn = todo(input_str)
     assert '#TODO' in input_str
     
    
# if #todo is not capitalised, an error is expected.
# TEST RESULT = Validate if 'TODO' was capitalised, Throws error message if not capitalised.
     
def test_check_if_todo_input_is_not_capitalised_gives_error():
    input_str = "#Todo buying grocery"
    with pytest.raises(Exception) as e:
        todo(input_str)
    error_message = str(e.value)
    assert error_message == "Error : #Todo should be capitalised!"
