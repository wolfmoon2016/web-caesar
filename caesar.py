

new_string="" #create a new string, this will be our output

def encrypt (text,rot):
    """3. take the inputed string, iterate though each letter, then shift each letter by the number of rotations
    """
    new_string="" #create a new string, this will be our output

    ##1. Have a loop to iterate through each letter in sentence
    for char in text:
        ##2 (in the loop)
        ##check if its a letter ( use isalpha())
        if char.isalpha()==True:
            ##call the function rotate_character
            new_letter = rotate_character(char,rot)
            new_string += new_letter
        else:
        ##if not letter, add to character without changes to new_string
            new_string += char
    return new_string

def alphabet_position(char):
    if  char == char.lower():
        return ord(char) -97 # using ascii position lowercase "a"
    else:
        return ord(char) -65 #using letter from encrypt function defaults to uppercase



def rotate_character (char, rot):
    """step 4. this function takes the letter from encrypt and actually encrupts it
    two methods for how to deal with upper case and lower case
    1. have a different condition for upper case or lower case
    2. turn everything to lower case, but use a flag that is true when its upper case. Do the match. Then if flag = true, change transformed letter to uppercase
    """
    new_string = ""

    if char ==char.lower():  #using letter from encrypt function, test for lowercase
            newpos = alphabet_position(char)
#            newpos = ord(char) -97 # using ascii position lowercase "a"
            newpos += rot  # setting the shift for encryption
            newpos = newpos % 26 #limiting the shift to 26 charatcters to wrap
            new_string += chr(newpos + 97) # putting characters into empty string in correct indexed position
    else:
            newpos = alphabet_position(char)
#            newpos = ord(char) -65 #using letter from encrypt function defaults to uppercase
            newpos += rot             #set shift from input for encryption
            newpos = newpos % 26 # setting letters to wrap around z to a
            new_string += chr(newpos + 65) ## putting characters into empty string in correct indexed position
    return new_string
