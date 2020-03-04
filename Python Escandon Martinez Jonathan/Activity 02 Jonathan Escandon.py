username = input('Please enter your name: ')
print( f'Hello, {username}')
s_age = input('Age:')
age = int(s_age)
s_height  = input('Height:')
height = float(s_height)
print(f'You said you are {age} years old and {height}m tall.')
Number=0
gender=None
email=None
bank_account=None
Show=None
anime=None
videogame=None

print("I will ask for some data, leave it blank if you don't want to tell me.")
You_gender=input('¿What is your Gender (m or f)?')
if(You_gender!= ''):
	if You_gender== 'm':
		gender='Male'
		Number=Number+1
	elif You_gender=='f':
		gender='Female'
		Number=Number+1
	else:
		print(f'({You_gender}) does not exist in my database ')

You_email=input('¿What is your E-mail?')
if You_email != '':
	Number=Number+1
	email=You_email

if Number>=2:
	answer=input('Can I have your phone number? (yes/no)')
	if answer=='yes':
		Number=Number+1
		phone_number = input('Phone number:' )

if Number>=3:
	answer = input('Can I have your bank account? (yes/no)')
	if answer== 'yes':
		Number=Number+1
		bank_account=input('Account number:')

if Show=input('¿What is you favourity tv show?'):
    answer=input('Ohh, This is a great show')
	


