import re

def longest(word_list):  
    longest_word = '' 
    # get word from array 
    for word in word_list: 
      # check if word have a symbols  
          word = re.sub('[!@#$%^&*()]', '', word)
          if len(word) > len(longest_word):
            longest_word = word
    print(longest_word)  

# input string and convert to array
words = "Baju ini sangat bagus sekali!" 
word_list = words.split()  
# call function
longest(word_list)  
