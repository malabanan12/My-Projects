import os
#Main Menu
def show_main_menu():
    ''' Show main menu for Phone Book Program '''
    print("   *****************************"+
        "\n   ** C O N T A C T   B O O K **\n"+
          "   *****************************"+
          "\n------------------------------------------\n"+
          "\n"+
          "Enter 1 To Display Your Contacts Records\n" +
          "Enter 2 To Add a New Contact Record\n"+
          "Enter 3 To search your contacts\n"+
          "Enter 4 To Quit\n\n------------------------------------------")
    choice = input("Enter your choice: ")
    #Function of the program

    #Display the Contact records
    if choice == "1":
        file1 = open('file_name', "r+")
        file_contents = file1.read()
        if len(file_contents) == 0:
            print("Phone Book is empty")
            #when the phonebook is empty, the system inform the user that the phonebook is empty
        else:
            print (file_contents)
        file1.close
        ent = input("Press Enter to continue ...")
        _ = os.system('cls')
        show_main_menu()

    #Add a New Contact
    elif choice == "2":
        enter_contact_record()
        ent = input("Press Enter to continue ...")
        _ = os.system('cls')
        show_main_menu()

    #Search Contact
    elif choice == "3":
        search_contact_record()
        ent = input("Press Enter to continue ...")
        _ = os.system('cls')
        show_main_menu()
    #exit
    elif choice== "4":
        print("Thanks for using Phone Book Program presented by:"+
              "\n")
    else:
        print("Wrong choice, Please Enter [1 to 4]\n")
        ent = input("Press Enter to continue ...")
        _ = os.system('cls')
        show_main_menu()
    #if the user enter wrong choice
    #the system will return to main menu
#searching main function
def search_contact_record():
    ''' This function is used to searches a specific contact record '''
    search_name = input("Enter First name for Searching contact record: ")
    rem_name = search_name[1:]
    first_char = search_name[0]
    search_name = first_char.upper() + rem_name
    file1 = open('file_name', "r+")
    file_contents = file1.readlines()
     
    found = False   
    for line in file_contents:
        if search_name in line:
            print("Your Required Contact Record is:", end=" ")
            print (line)
            found=True
            break
    if  found == False:
        print("There's no contact Record in Phone Book with name = " + search_name )

def input_fname():
    ''' Converts first letter of your name  to Upper case '''
    fname = input("Enter First name: ")
    rem_fname = fname[1:]
    first_char = fname[0]
    return first_char.upper() + rem_fname

def input_lname():
    ''' Converts first letter of  last name  to Upper case '''
    lname = input("Enter Last name: ")
    rem_lname = lname[1:]
    first_char = lname[0]
    return first_char.upper() + rem_lname

#another add a contact functions
def enter_contact_record():
    ''' It  collects contact info firstname, last name, email and phone '''
   
    first = input_fname()
    last = input_lname()
    phone = input('Enter Phone number: ')
    contact = ("[" + first + " " + last + ", " + phone + "]\n")
    file1 = open('file_name', "a")
    file1.write(contact)
    print( "This contact\n " + contact + "has been added successfully!")

show_main_menu()

