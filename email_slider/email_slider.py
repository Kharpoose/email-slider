def main():
    print("Welcome to the e-mail slicer " )
    print("")

    email_input = input("Input your e mail address: ")
    
    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")
    print(f"User name is: {username}")
    print(f"Domaine is: {domain}")
    print(f"Extension is: {extension}")

main()    