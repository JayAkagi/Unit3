import pytest
from lib.todo import *

# we need to find out the function todo is an instance
# of a function.

def test_todo_is_a_function():
    result = todo("")
    assert isinstance(result, bool)

# we need to find out our input of the function should be
# a string
def test_validate_input_is_string():
    input_string = "testing string"
    result = todo(input_string)
    assert isinstance(input_string, str)

# if our input is not string, an error is expected.
def test_throw_an_error_if_input_is_not_string():
    with pytest.raises(Exception) as e:
        todo(10)
    error_message = str(e.value)
    assert error_message == "Input is not a string type. Try again."

# does user_input string, contains #todo
# if it has #todo, it returns true
def test_confirm_if_input_string_contains_todo():
    input_string = "I am a random string to be checked #TODO"
    result = todo(input_string)
    assert result == True

# if it does not contain #todo, it returns false
def test_confirm_if_input_string_does_not_contains_todo():
    input_string = "I am a random string to be checked"
    result = todo(input_string)
    assert result == False



# validate if instance of the list is a list.

# confirm if we have correct amount of todo things in the
# existing list.

# Ensure #todo is capitalised.
# if #todo is not capitalised, an error is expected.