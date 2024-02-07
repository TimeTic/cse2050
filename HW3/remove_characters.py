
def remove_characters(input_string, to_remove):
    """this functions takes two parameters, and remove characters from input string.
    
    this is O(n) linear algorithim
    """
    remove_char = set(to_remove)
    result = []

    for char in input_string:
        if  char not in remove_char:
            result.append(char)
    new_string = ''.join(result)
    return  new_string
    
#exampesl
new_string = remove_characters('abcd', 'c')
print(new_string)