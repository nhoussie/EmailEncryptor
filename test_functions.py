"""Testing encoded and decoded functions with inputs and outputs"""

from functions import *

def test_function_encode_message ():
    
    # testing that it is a function
    assert callable(encode_message)
    # Testing for encoded message as string
    assert isinstance (encode_message('test'),str)
    message = 'abcd'
    # Testing for input and output  
    assert encode_message ('abcd') == 'OYcd'
    
    
def test_function_decode_message ():
    # Testing that function is callable 
    assert callable(decode_message)
    # Testing for encoded message as string
    assert isinstance (decode_message('test'),str)
    message = 'OYcd'
    # Testing for input and output 
    assert decode_message ('OYcd') == 'abcd'  
    
    
    
    
    

