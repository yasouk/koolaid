print("""-------------------------------------------*---------------------
Welcome to Aunt Fannie Mae's Fruit Punch Recipe
-------------------------------------------*---------------------""")
print('\033[1m' + 'PLEASE SELECT FROM THE FOLLOWING MENU:' + '\033[0m')
print('1 = Original (Aunt Fannie’s Way)\n2 = Algorithmic (Step By Step)\n3 = Adaptation (Heather’s Way)\n')
print('\033[1m' + 'Which recipe version would you like to see?' + '\033[0m')
num = int(input())


recipe_instruction_header = """---------------------
Recipe Instructions
---------------------"""


if num == 1:
    print('\033[1m' + 'You selected option 1, Original (Aunt Fannie’s Way)'  + '\033[0m')
    print(recipe_instruction_header)
    print('')


elif num == 2:
    print('\033[1m' + 'You selected option 2, Algorithmic (Step By Step)'  + '\033[0m')
    print(recipe_instruction_header)
    print('')
   

elif num == 3:
    print('\033[1m' + 'You selected option 3, Adaptation (Heather’s Way).' + '\033[0m')
    print(recipe_instruction_header)
    print("""1. Open Kool-Aid packet.
2. Pour Kool-Aid packet contents into two liter pitcher.
3. Pour sugar into two liter pitcher.
4. Fill pitcher with water.
5. Use long handle spoon and stir mixture in pitcher for 30 seconds.
""")
else :
    print('Please enter one of the given options')


print('\033[1m' + 'Do you want to see the grocery shopping list?' + '\033[0m')
see_grocery_list = input()
print()

def g_l():  
     if see_grocery_list == 'Yes':    
         print('-------------------------------')
         print('     Grocery Shopping List     ')
         print('-------------------------------')
         print('')
         print('Kool-Aid packet')
         print('Sugar')
         print('\033[1m' + 'Enjoy your recipe!' + '\033[0m')
     elif see_grocery_list == 'No':
         print('grocery shopping list not displayed')

     else :
         print('Please enter one of the given options')
         g_l(see_grocery_list)