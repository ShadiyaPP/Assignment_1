import re

#Function to display password creation rule
def rule():
    print('\n*PASSWORD MUST HAVE ONE SPECIAL CHARACTER, ONE DIGIT,ONE UPPERCASE AND ONE LOWERCASE CHARACTER AND LENGTH BETWEEN 5 TO 16*\n')


#Function to get password from file for a existing user
def fotgotPw(umail):
    file_data = open('USERDATA.txt', 'r')
    data_lines = file_data.readlines()
    pw = ''
    for line in data_lines:
        login_info = line.split()
        if umail == login_info[0]:
            pw = login_info[1]
    print('Your password:', pw)


#function to reset new password in file by deleting old one
def changePw(u_mail):
    # Rule to follow
    rule()
    new_password = input('Enter the new password: ')
    p_value = password_validation(new_password)
    if p_value == True:
        with open('USERDATA.txt', 'r') as f:
            lines = f.readlines()
        with open('USERDATA.txt', 'w') as f:
            for line in lines:
                login_info = line.split()
                if u_mail != login_info[0]:
                    f.write(line)
        with open('USERDATA.txt', 'a') as f:
            f.write(u_mail)
            f.write(' ')
            f.write(new_password)
            f.write('\n')
        print('\nPASSWORD CHANGED')

    else:
        print('INVALID PASSWORD')


#Function to validate mail id
def mail_validation(mail):
    valid_format = re.compile('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$')
    if re.fullmatch(valid_format,mail):
        return True
    else:
        return False


#Function to validate password
def password_validation(pw):
    if (len(pw) > 5 and len(pw) < 16 and re.search(r'\d+', pw) and re.search(r'[a-z]+', pw) and
            re.search(r'[A-Z]+', pw) and re.search(r'\W+', pw) and not re.search(r'\s+', pw)):
        return True
    else:
        return False


#Function register new user
def UserRegistration():
    mail = input('Enter your mail id: ')

    #Mail validation
    m_value = mail_validation(mail)
    if m_value == True:

        #Rule to follow
        rule()
        password = input('Enter the password: ')

        #password validation
        p_value = password_validation(password)
        if p_value == True:

            #Writing new user data to file
            file_data = open('USERDATA.txt', 'a')
            file_data.write(mail)
            file_data.write(' ')
            file_data.write(password)
            file_data.write('\n')
            file_data.close()

            #Success message
            print('User successfully registered!!!')


        # Invalid password
        else:
            print('INVALID PASSWORD!!!')

    # Invalid Mail
    else:
        print('INVALID MAIL ID!!!!')


#Function to check login credentials
def UserLogin():
    mail = input('Enter your mail id: ')
    password = input('Enter your password: ')
    file_data = open('USERDATA.txt','r')
    data_lines = file_data.readlines()
    flag = False
    umail = ''
    for line in data_lines:
        login_info = line.split()
        if mail==login_info[0]:
            umail = login_info[0]
        if mail==login_info[0] and password==login_info[1]:
            flag = True
            break
    if flag==True:
        print('Login Successful')
    else:
        #if user id exists
        if umail!='':
            print('\nUser "'+umail+'" exist but incorrect password!!!!\n')
            print('1.FORGOT PASSWORD\n2.RESET NEW PASSWORD')
            choice=int(input('\nEnter your choice: '))
            if choice==1:
                fotgotPw(umail)
            elif choice==2:
                changePw(umail)
            else:
                print('INVALID CHOICE')

        else:
            print('\nUSER DOES NOT EXIST')
            choice = input('\nDO YOU WANT TO REGISTER AS A NEW USER Y/N: ')
            if choice=='Y':
                UserRegistration()
            elif choice=='N':
                exit()
            else:
                print('INVALID CHOICE')


#Printing main manu
print('1.REGISTRATION \n2.LOGIN')


#Reading user choice
choice = int(input('\nEnter your choice: '))
if choice==1:
    UserRegistration()
elif choice==2:
    UserLogin()
else:
    print('INVALID CHOICE!!!')