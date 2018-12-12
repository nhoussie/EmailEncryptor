
def have_a_email():
    """
   This function takes an input, being the email that will be encoded later and lower cases the letters before it gets passed
   into the encoding  function.
    """
    email = ""
    while True:
        
        # All the inputs are lowered cased in order for the encoding fucntion to work
        msg = input('INPUT :\t').lower()
        # When the msg is set to "quit' the while breaks out
        if (msg == "quit"):
            break
        # msg is added to new line
        msg += "\n"
        email += msg
        
    return email  


def have_a_email_decoding():
    
    """
        This function takes an input, being the encoded emails and doesn't lower cases the letters (because it messes up with 
        the decoding function) before it gets passed into the decoding function.         
    """

    email = ""
    while True:
        # For decoding the emails, the inputs will not be lowercased because decoding function won't work due to 
        # a designed algorithm for decoding. 
        msg = input('INPUT :\t')
        #  In order to quit from inputs the word 'quit' needs to be typed to break out of loop
        if (msg == "quit"):
            break
        # msg is added to new line
        msg += "\n"
        email += msg
        
    return email  



def reverse_string(my_string):
    """
        This code takes my_string makes it into a list, reverses the list then makes it into a list again. Finally, it joins
        the list. 

    Parameters
    ----------
    my_string : string
                This message will be 

    Returns
    -------
    output : list ( joined)
             This output returns a list that is joined. 
    """

    return ''.join(list(reversed(list(my_string))))



def encode_message (my_string):
    """
    This code takes the message and encodes it. 

    Parameters
    ----------
    my_string : string
                The message to be encoded

    Returns
    -------
    output : string
             The encoded message.    
    """
    
    output = ''
    # For each character in the string it will encode those characters and return an output ( string)
    for char in my_string:    
        output += encode_chr(char)
    return output


def encode_chr(some_chr):
    """
    This encode_chr takes a letters reverses its keycode to another letter/character. 
                                   
    Parameters
    ----------
    some_chr : string
               

    Returns
    -------
    some_chr: If the email message has any of those letters in it. It will return them and not encode them.
              In addition, the other some_chr worked by taking the characters in a string, takes the ord of them,
              changes it into a string, uses the reverse_string function, changes it into an integer finally returns a 
              character. The character it returns is a reversed keycode.
    """
    # This  list of letters that won't be taken in by the function because they cause problems in the code.
    # This is further explained  in my Norah_issues_solved ( talks about the issues encoutered in project)
    problems = ['d', 'n', 'x','\n']    
    if(some_chr in problems):
    # The characters that cause the problems they will be returned 
        return some_chr
    # The final return is a character of the reversed keycode
    return chr(int(reverse_string(str(ord(some_chr)))))



def decode_message(my_string):
    """
    This code takes the message and decodes it using the reverse_string furction. First, it takes the encoded message, loops
    through each letters, finds the ord changes it into a string , takes an int

    Parameters
    ----------
    my_string : string
                The message to be decoded.

    Returns
    -------
    output : string
             The decoded message.    
   """
    
    output = ''
    # For each character in the string it will decode those characters and return an output (string)
    for char in my_string:  
        output += decode_chr(char)
    return output
    

def decode_chr(some_chr):
    """
    This function takes the encoded message and reverses it back to the originale message, however, lowercased. 

    Parameters
    ----------
    some_chr : string
               
    Returns
    -------
    some_chr: Again any of those problem letters will be still in the encoded message ( not changed because they cause issues).
              The decode function will use the same methods as the encoded function but returns the original message. 
    """
    
    problems = ['d', 'n', 'x', '\n'] 
    # The characters that cause the problems they will be returned and not decoded
    # Originally they are never encoded because their reversed key codes don't return them back
    if(some_chr in problems):
    #The characters that cause the problems they will be returned 
        return some_chr
    #The final return is a character of the original message 
    return chr(int(reverse_string(str(ord(some_chr)))))

"""" The overall picture is understanding that encoded and decoded functions use the same function because they are opposite
      of each other in a sense. But for naming purposes, they are defined separately."""
       
   
  

