def triangle(angka):
  if(isinstance(angka, int) != True or angka < 0):
    return "parameter harus angka dan positif!"

  # rows
  for i in range(0, angka): 
    
      # columns 
      for j in range(0, i+1): 
        
          # print stars 
          print("# ",end="") 
      
      # new row
      print("\r") 


triangle(7)

#false
#triangle(-2)

#false
# triangle("p")
