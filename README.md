# Norah Al.Azzam License-
I give permission to the general public to use this code in a way appropriate to the task they want to achieve. 

# Reversing Keycode for encryption and decryption 
First, you will need to set up an email system through python and be able to receive emails through your email box. The emails which you receive are encrypted and you need to use a function provided in order to decode them. In addition, the emails which you will send are encrypted as well.
The method for encryption uses reversing a Key Code. It is not like any other method where you would shift key codes and just shift them back to decode them. This method reverses the key code number of a given lowercase English letter and changes it to another character for encryption. The same method applies when you want to decode the message. This method seems simple at first, however, there was a lot of work going into how to get the method to work and also seeing what limitations it had to offer. Information will be provided on how the function works in (Norah_function.py). This project had many incorporations of Assignment 3 in it in order to create inputs and outputs. Also, Assignment 4 because functions were created for given tasks.
Each character has a key code attached to it. Of course, there are so many ways to move key codes by units to get a different key code and just move back to the original key code of that message. What I mean is that it is simple to just move key codes and it is easy to decode them that was what A2 did.
To make things advance. I thought about an idea to reverse the key code given for example lower case "a" keycode is 97 and my function will reverse the key code to 79. However, I run into many issues. One particular is that say an original key code is 100 of a letter d and if I use my function to reverse it then the key code will be 001. Now, python will then think that it is 1 and remove all the zeros. Once you try to reverse back ( decode it), you won't get the original letter. Instead, you will get an empty space or another letter.
Furthermore, there is a notebook that keeps a record of the issues I ran into and how I solved them. The notebook name is "Norah_issues_solved."Also, the notebook highlights how I thought about my project and gives a final resolution to the functions you see in (functions.py) .
## Getting Started

Make sure to have anaconda installed and python version 3 ( preferably the latest version). 

Before you start this, make sure you have your Gmail username and password ready. You might need to create a separate email for this. Or after you are finished with the task make sure to remove the password. 
Next, go to https://myaccount.google.com/lesssecureapps and login if you need to. In this page, you will want to flick the Allow less secure apps switch to on. This allows us to use less secure sign-in technology to log in to the email server; note that this will make your account more vulnerable.

### Prerequisites

* Need Python Version 3.6 or 3.7 
* Have Anaconda Jupyter
* Gmail account



## Running the tests

The test functions are further explained under test_functions.py.  The test functions test the inputs and outputs, if the functions are callable, and checks if the functions give you a string. 


## Limitations in the code
There is a Jupyter notebook that highlights the limitations in the code ( Norah_issues_solved), but here is a summary:
* All inputs will be changed to lowercase letter/characters 
* Letters like (d,n,x) will not be encoded or decoded because reversing their keycodes removes the zeros and doesn't give back the letter  




## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## License

This project is licensed under the General Pulbic License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments
* Thomas Donoghue The instructor for COGS 18 Fall 2018
* UCSD COGS 18 Instructional Assistants  and Teaching Assistant 

