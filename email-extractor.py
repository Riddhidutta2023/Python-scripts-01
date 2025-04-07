# This program extracts the name from a supplied email


email_supplied=input('Write down the email address:  \n')
print(f"You wrote {email_supplied}\n")

if '@'in email_supplied:
    index_of_delimiter = email_supplied.index('@')
    name=email_supplied[0:index_of_delimiter]
    email=email_supplied[index_of_delimiter+1:]
else:
    print('The email supplied is invalid')

print(f"username:{name},\ndomain:{email}")



