import re

def usernameCheck(username):
  x = re.findall("^(?=.*[a-z])(?!.*[A-Z]).{5,7}$", username)
  if(x):
    return True
  return False
  
def passwordCheck(pasword):
  x = re.findall("^([a-zA-Z0-9@]{9})$", pasword)
  if(x):
    return True
  return False
  

#call funtion usernameCheck true
print(usernameCheck("diandra"))

#call funtion usernameCheck false
#print(usernameCheck("Ebi"))

#call funtion passwordCheck true
print(passwordCheck("Kint4m@ni"))

#call funtion passwordCheck false
#print(passwordCheck("p@ssW0rd!"))
