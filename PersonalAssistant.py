class PersonalAssistant:
    def __init__(self, todos, birthdays, contacts):
        self.todos = todos
        self.birthdays = birthdays
        self.contacts = contacts


    def add_todo(self, new_item):
        self.todos.append(new_item)
        return f"{new_item} has been added to your todo list."
      
    def get_todos(self):
        return self.todos
      
    def remove_todo(self, new_item):
        if new_item in self.todos:
            self.todos.remove(new_item)
            return f"{new_item} removed from todo list."
        else:
            return f"To-do is not in list!"

    def get_birthdays(self):
        return self.birthdays
  
    def get_birthday(self, name):
        if name in self.birthdays:
            return f"{name}'s birthday is on {self.birthdays[name]}."
        else:
            return "Can't find birthday for this person :("

    def add_birthday (self, name, date):
        if name in self.birthdays:
            return f"You already have a birthday for {name}"
        else:
            self.birthdays[name] = date
            return f"{name}'s birthday has been added."

    def remove_birthday (self, name):
        if name in self.birthdays:
            self.birthdays.pop(name)
            return f"{name}'s birthday has been removed."
        else:
            return f"{name}'s birthday not found, so can't be removed."
  
    def get_contact (self, name):
        if name in self.contacts:
            return f"{name} is a {self.contacts[name]}"
        else:
            return "Sorry, there's no contact by that name"

    def add_contact (self, name, position):
        if name in self.contacts:
            return f"That contact is already in the list"
        else: 
            self.contacts[name] = position
            return f"{name} has been added to the contact list."
  
    def remove_contact (self, name):
        if name in self.contacts:
            self.contacts.pop(name)
            return f"{name} has been deleted from contacts."
        else:
            return f"{name} isn't in your contacts, could not remove."
   
    def get_contacts(self):
        return self.contacts

      
#    def get_birthday(self, name):
#      if name == "Maxwell":
 #       return "Birthday is 06/14/1992! "
  #    elif name == "Mom":
#        return "Birthday is 02/25/1956 "
#      elif name == "Dad":
#        return "Birthday is 02/04/1955"
#      else:
 #       return"Can't find a birthday for this person..."
  
# Code to test output of the class
#assistant = PersonalAssistant()
#assistant.add_todo("Pick up groceries")
#assistant.add_todo("Give purple some love ")
#assistant.add_todo("Call Maxwell and tell him I love him ")
#print(assistant.get_todo())
#assistant.remove_todo("Pick up groceries")
#print(assistant.get_todo())

# Change name to one from your contacts
#print(assistant.get_contact("Chelsea"))
#print(assistant.get_birthday("Maxwell"))