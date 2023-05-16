def main():
    print(" Wlecome to the email slicer ")
    print("")


    email_input = input("Input your email adress: ")

    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")
    
    print("Username: ", username)
    print("Domain: ", domain)
    print("Extension: ", extension )

while True:
 main()






















# collect email from user
# split the email using the @ the first part as the username , the second part is gonna be saved as domain
# split domain usnig .,
#hello@codewithvika.com
