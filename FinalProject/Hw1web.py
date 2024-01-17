from abc import ABC, abstractmethod


class UserInterface(ABC):
    @abstractmethod
    def show_contacts(self, contacts):
        pass

    @abstractmethod
    def show_contact_info(self, contact):
        pass

    @abstractmethod
    def show_commands(self, commands):
        pass


class ConsoleUserInterface(UserInterface):
    def show_contacts(self, contacts):
        for contact in contacts:
            print(contact)

    def show_contact_info(self, contact):
        print(contact)

    def show_commands(self, commands):
        format_str = str('{:%s%d}' % ('^', 20))
        for command in commands:
            print(format_str.format(command))


class App:
    def __init__(self, user_interface):
        self.user_interface = user_interface

    def run(self):
        # Логіка додатку
        contacts = []  # Замініть це на реальний список контактів
        commands = ['Add', 'Search', 'Edit', 'Load', 'Remove', 'Save', 'Congratulate', 'View', 'Exit']

        while True:
            action = input('Type help for list of commands or enter your command\n').strip().lower()

            if action == 'help':
                self.user_interface.show_commands(commands)
                action = input().strip().lower()

            # Логіка викликів методів для обробки команд відповідно до реалізації UserInterface
            if action == 'view':
                self.user_interface.show_contacts(contacts)
            elif action == 'exit':
                break
            else:
                print("There is no such command!")


if __name__ == "__main__":
    console_ui = ConsoleUserInterface()
    app = App(console_ui)
    app.run()