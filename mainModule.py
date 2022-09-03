from emailProccess import emailPrc,printmsg
emails = ['ngoknghek@gmail.com', 'hihi@loveyou.com', 'tranhang@gmail.com']
def main():
    emails = ['ngoknghek@gmail.com', 'hihi@loveyou.com', 'tranhang@gmail.com']

    for email in emails:
        user_name, domain = emailPrc(email)
        printmsg(user_name, domain)
if __name__ == '__main__':
    main()