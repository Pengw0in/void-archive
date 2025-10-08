import re

def check_password(password: str) -> bool:
    '''
    ^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^a-zA-Z0-9]).+$
    
    This regex uses positive look-ahead[?=] to confirm all 
    upper, lower , special charecters exits and match them 
    accordingly
    
    '''
    if re.findall(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^a-zA-Z0-9]).+$', password):
        return True
    else:
        return False

password = input().strip()

if check_password(password):
    print("Password is strong")
else:
    print("Password is missing either uppercase, lowercase or special charecter")