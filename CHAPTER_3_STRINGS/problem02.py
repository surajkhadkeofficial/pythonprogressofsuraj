# Write a program to fill in a letter template given below with name and date

letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''
 
print(letter.replace("<|Name|>","SURAJ").replace("<|Date|>","07/09/2025"))