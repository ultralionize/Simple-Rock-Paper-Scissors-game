import random
import os

#Dictionary for storing the value of rock, paper and scissors
temp = { 1 : 'Rock', 2 : 'Paper', 3 : 'Scissors'}


#For maintaining win/lose/tie records
win = loss = tie = 0


#Rules of the game
def rules():
	print('''--------------------Rock Paper Scissors--------------------
		     
		      Rules of the game

		Rock vs paper --> paper wins
		Rock vs scissor --> Rock wins
		paper vs scissor --> scissor wins\n''')



#WinCondition for checking the winning condition
def winCondition(choice, comp):
	if choice == comp:
		return 4
	elif (choice == 1 and  comp == 2) or (choice == 2 and comp == 1):
		return 2
	elif (choice == 1 and  comp == 3) or (choice == 3 and comp == 1):
		return 1
	elif (choice == 2 and  comp == 3) or (choice == 3 and comp == 2):
		return 3


#For displaying the result
def display(result, choice, comp):
		global win, tie, loss
		if result == choice:
			win += 1
			print('''\t\t\t\tYou vs Bot
				==================================
				{} vs {}====>{} wins
				==================================
				You Win'''.format(temp[choice], temp[comp], temp[choice]))    
		elif result == comp:
			loss += 1
			print('''\t\t\t\tYou vs Bot
				==================================
				{} vs {}====>{} wins
				==================================
				You lose'''.format(temp[choice], temp[comp], temp[comp])) 
		else:
			tie += 1
			print('''\t\t\t\tYou vs Bot
				==================================
				{} vs {}====>{}
				==================================
				Its a tie'''.format(temp[choice], temp[comp], temp[choice])) 
		print('\nWins :{}  losses :  {}  tie : {}\n'.format(win, loss,tie))


#The call to various functions are given in the game function
def game(choice):
	if choice in [0, 1, 2, 3]:
		if choice == 0:
			exit()	
		comp = random.randint(1, 3)
		result = winCondition(choice, comp)
		display(result, choice, comp)
		os.system('pause')
		os.system('cls')
	else:
		os.system('cls')
		print('Enter correct choice')	


#main function which checks for correct input and calling the game
def main():
	rules()
	os.system('pause')
	os.system('cls')	
	while 1:	
		try:
			print('Enter your choice (0 to quit)')
			choice = int(input('1. Rock 2. Paper 3. Scissors : '))
		except:
			os.system('cls')
			print('Enter correct choice')
			continue
		else:
			game(choice)
			
				
if __name__=='__main__':
	main()