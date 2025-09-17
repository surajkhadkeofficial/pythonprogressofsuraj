str =  'suraj'

print(len(str))  #string length 

print(str.endswith('raj'))  #check ending characters if yes then true or false

print(str.startswith('sur'))  #check starting character if yes then true or false

count=str.count('u')
print(count)             #count the given character in string

capitalized_string = str.capitalize()  #capitalize the first character of string 
print(capitalized_string)

index = str.find('r')  #find the location of string  on index
print(index)


''' This function replace the old word with
new word in the entire string.'''

replaced_string = str.replace('suraj','surya')
print(replaced_string)      



