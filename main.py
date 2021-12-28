#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password = []

for i in range(0,nr_letters):
  random_letter = random.randint(0,len(letters)-1)
  password.append(letters[random_letter])


for x in range(0,nr_symbols):
  #or use random_symbol = random.choice(symbols)
  #random_symbol = random.randint(0,len(symbols)-1)
  #password.append(symbols[random_symbol])

  password.append(random.choice(symbols))


for y in range(0,nr_numbers):

  random_number = random.randint(0,len(numbers)-1)
  password.append(numbers[random_number])

#randomizing the final pattern
final_password=[]
for z in range(0,len(password)):
  random_position = random.randint(0,len(password)-1)
  final_password.append(password[random_position])

#randomizing using the shuffle function
#print(f"Preshuffle {password}")

random.shuffle(password)
#print(f"Postshuffle {password}")



#print(f"Your password is {final_password}")

Finalstring = ''.join(map(str, final_password))

print(f"{Finalstring}")
