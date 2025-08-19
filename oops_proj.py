class chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()
    
    def menu(self):
        user_input = input("""Welcome to ChatBook !! How would you like to proceed?
                           1.Press 1 to signup
                           2.Press 2 to Signin
                           3.Press 3 to write a post
                           4.Press 4 to message a friend
                           5.Press any other key to exit
                           
                           """) 
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.my_post()
        elif user_input == "4":
            self.sendmsg()
        else:
            exit()

    def signup(self):
        email = input("Enter your email here:")
        pwd = input("Set you password here") 
        self.username=email
        self.password=pwd
        print("Yoh have Signed Up Successfully !!")
        print("\n")
        self.menu()

    def signin(self):
        if self.username == '' and self.password == '' :
            print("Please signup first by pressing 1 in main menu")
        else:
            uname = input("Enter your email/username here:->")
            pwd = input("Enter you password here:->")
            if uname == self.username and pwd == self.password:
                print("You have signed in successfully!!")
                self.loggedin = True
            else:
                print("Please enter correct credentials:") 
        print("\n")
        self.menu()  

    def my_post(self):
        if self.loggedin == True:
            txt= input("Enter your message here:")
            print(f"following message has been posted -> {txt}")
        else:
            print("Please signin first to post something...")
        print("\n")
        self.menu()   

    def sendmsg(self):
        if self.loggedin == True:
            txt= input("Enter your message here:")
            frnd = input("Enter you friend's name:")
            print(f"Message has been sent to your friend {frnd}")
        else:
            print("Please signin first to post something...")
        print("\n")
        self.menu()     

obj = chatbook()        
