from database import create_tables, add_entry, get_entries

menu  = """Please select one of the following options:
1) Add new entry for today.
2) View entries.
3) Exit.

Your selection: """
welcome = "Welcome to programing diary!"


def prompt_new_entry():
    entry_content = input("What have you learned?")
    entry_date = input("Enter the date:")

    add_entry(entry_content, entry_date)


def view_entries(entries):
    for entry in entries:
        print(f"{entry[1]}\n{entry[0]}\n\n")


print(welcome)
create_tables()

while (user_input := input(menu)) != "3":
    if user_input == "1":
        prompt_new_entry()
    elif user_input == "2": 
        view_entries(get_entries())   
    else:
        print("Invalid option, please try again!")


