# A program for implementing a simple contact manager to store, process and retrieve a person’s names, contact number, and email address.
# Vincent T Mukwevo MKWVIN004
# 05 May 2024

def path_exists(file_path):
    # Checks if the path to the contacts file exists.
    try:
        with open(file_path, 'r'):
            return True
    except FileNotFoundError:
        return False

def add_contact(file_path, name, phone, email):
    # Reads the existing contacts to check if the new contact already exists.
    existing_contacts = read_contact(file_path)
    new_contact = f'{name},{phone},{email}'
    
    # Check if the new contact details are already in the existing contacts.
    if new_contact not in existing_contacts:
        with open(file_path, 'a') as path:
            print(new_contact, file=path)
            path.close()
        print('Contact added successfully.')
    else: print('Contact already exists.')
    return ''

def custom_sort(contacts):
    # Sorts the contacts list alphabetically by name.
    return sorted(contacts)

def search_contact(file_path, query):
    # Searches for contacts in the contacts file based on the query supplied by the user.
    with open(file_path, 'r') as path:
        lines = [line.strip('\n') for line in path]
        path.close
    cont = [line for line in lines if query in line]

    if len(cont) > 0:
       print('Found contact(s):')  
       print('============================================================')
       print('| Name                 | Phone           | Email                     |')
       print('============================================================')
       for item in cont: 
            result = item.split(',')
            print(f'| {result[0]: <20.20s} |',end='')
            print(f' {result[1]: <15.15s} |',end='')
            print(f' {result[2]: <25.25s} |')
            print('------------------------------------------------------------')
    else:print('No contact found.')
    return ''

def read_contacts(file_path):
    # Reads contacts from the contacts file and returns a lists within a list of contacts.
    with open(file_path, 'r') as path:
        lines = [line.strip('\n') for line in path]
        path.close()
    cont = []
    inner = []
    for line in lines:
       cont.append(line.split(',')) 
    return cont

def read_contact(file_path):
    # Reads contacts from the contacts file and returns a list of contacts.
    with open(file_path, 'r') as path:
        lines = [line.strip('\n') for line in path]
        path.close()
    cont = [line for line in lines]
    return cont

def prinzer(contacts):
    # Prints the contacts in a formatted output.
    print('============================================================')
    print('| Name                 | Phone           | Email                     |')
    print('============================================================')
    for lines in contacts:
        result = lines.split(',')
        print(f'| {result[0]: <20.20s} |',end='')
        print(f' {result[1]: <15.15s} |',end='')
        print(f' {result[2]: <25.25s} |')
        print('------------------------------------------------------------' )
    return ''

def list_contacts(file_path):
    # Lists all contacts sorted alphabetically by name.
    contacts = read_contact(file_path)
    contacts = custom_sort(contacts)
    prinzer(contacts)
    return ''

def main():
    # Main function to provide menu and interface with the user.
    file_path = input('Enter the name for the contacts file: \n')
    file_path = f'{file_path}.txt'
    if not path_exists(file_path):
        with open(f'{file_path}', 'w'):
            print(f'Contacts file \'{file_path}\' created.')
    while True:
        print('\n1. Add Contact \n2. Search Contact \n3. List Contacts \n4. Exit')
        choice = input('Enter your choice: ')
        if choice.isdigit():
            choice = int(choice)
       
        if choice == 1:
            name = input('Enter name: ')
            phone = input('Enter phone number: ')
            email = input('Enter email: ')
            add_contact(file_path, name, phone, email)

        elif choice == 2:
            query = str(input('Enter first name, last name, phone number, or email to search:\n'))
            if query == '*':
                print('Found contact(s):')
                list_contacts(file_path)
            else: search_contact(file_path,query)

        elif choice == 3:
            print('\nList of contacts:')
            list_contacts(file_path)

        elif choice == 4:
            print('Exiting program.')
            break

if __name__=='__main__': 
    main()