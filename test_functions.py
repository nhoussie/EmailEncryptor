from Norah_function import *

"""Testing encoded and decoded functions with inputs and outputs"""

def test_function_encode_message ():
    # testing that it is a function
    assert callable(encode_message)
    assert isinstance (encode_message('test'),str)
    message = 'abcd'
    # testing for input and output 
    assert encode_message ('abcd') == 'OYcd'
    
    
def test_function_decode_message ():
    # testing that it is a function
    assert callable(decode_message)
    assert isinstance (decode_message('test'),str)
    message = 'OYcd'
    # testing for input and output 
    assert decode_message ('OYcd') == 'abcd'  
    
    
    

