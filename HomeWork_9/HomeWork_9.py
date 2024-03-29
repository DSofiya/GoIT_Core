contact_list = {}

def input_error(func):
    def wrapper(*args):
        try:
            return func(*args)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "ValueError. Please enter the name and phone number."
        except IndexError:
            return "IndexError. Give me name and phone please."
        except NameError:
            return "Invalid input. Name should contain only letters."
        except TypeError:
            return "Invalid input. Phone number should contain only digits."
    return wrapper


@input_error
def command_add(input_str):
    _, name, phone = input_str.split()
    name = name.title()
    if not phone.isdigit():
        raise TypeError
    if not name.isalpha():
        raise NameError 
    contact_list[name] = phone
    return f"Contact {name} with phone number {phone} has been added."

@input_error
def command_change(input_str):
    _, name, phone = input_str.split()
    name = name.title()
    if not phone.isdigit():
        raise TypeError
    if not name.isalpha():
        raise NameError 
    contact_list[name] = phone
    return f"Phone number for {name} has been updated to {phone}."

@input_error
def command_phone(input_str):
    list_comand = input_str.split()
    name = list_comand[1].title()
    if not name.isalpha():
        raise NameError
    return contact_list[name]

def command_show_all(contact_list):
    if not contact_list:
        return "Список контактів пустий."
    result = "Contacts:\n"
    for name, phone in contact_list.items():
        result += f"{name}: {phone}\n"
    return result.strip()

def main():  
    while True:
        input_str = input("Enter command: ").lower().strip()
        
        if input_str == "hello":
            print("How can I help you?")
        elif input_str.startswith("add "):
            print(command_add(input_str))      
        elif input_str.startswith("change "):
            print(command_add(input_str))
        elif input_str.startswith("phone "):
            print(command_phone(input_str))
        elif input_str == "show all":
            print(command_show_all(contact_list))
        elif input_str in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        else:
            print("Невірно введена команда. Доступні команди:'hello','add','change','phone','show all','good bye','close','exit'")

if __name__ == "__main__":
    main()
