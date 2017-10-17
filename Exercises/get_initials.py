# Write a program that takes a full name, prints the initials of the first,
# middle, and last name. If the middle name is “NA”, then the program
# should print only the initials of the first and the last name.


def get_initials(name):
    """ Return initials of first, last and middle name.
    If the middle name is 'NA', return only the initials of the first and the last name.
    
    >>> get_initials("Alfred E. Newman")
    >>> 'A.E.N.'
    >>> get_initials("John NA Smith")
    >>> 'J.S.'
    """

    # your code here
def get_initials():
    FirstName = list(raw_input('Enter your first name:'))
    MiddleName = raw_input('Enter your middle name:')
    Surname = list(raw_input('Enter your middle name:'))

    if MiddleName == 'na':
        print FirstName[0],Surname[0]
    else:
        list(MiddleName)
        print FirstName[0],MiddleName[0],Surname[0]

get_initials()


