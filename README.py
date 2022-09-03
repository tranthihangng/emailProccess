# emailProccess
def emailPrc(email):
    email_username = email[:email.index('@')]
    email_domain = email[email.index('@')+1:]
    return [email_username,email_domain]
def printmsg(email_username, email_domain):
    print(f'user name is {email_username}, domain is {email_domain}')
def main():
    email = input('your email: ')
    email_username, email_domain = emailPrc(email)
if __name__ == '__main__':
    main()
