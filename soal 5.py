# %pip install numpy
# %pip install math
import numpy as np
import math 

# split string to array
def split(word): 
    return [char for char in word]  

def groupNumber(string):
    result = None
    #reject symbols and space
    number = re.sub('[-!@#$%^&*()\s]', '', string)
    #math equation with logaritm
    equation = int(len(number)*math.log10(3)-1)
    #split and distribute array
    arraynumber = np.array_split(split(number), equation)

    # joining array
    a = 0
    for i in arraynumber:
      if result == None:
        results = "".join(arraynumber[a]) 
        result = results
      else:
        results = "".join(arraynumber[a]) 
        result += "-"+results
      a = a + 1
    print(result)
    

   

groupNumber("993141 -1 1323 14-232")

