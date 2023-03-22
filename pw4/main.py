#import sys
#module_path = r"C:\Users\ciltr\Source\Repos\Alonelymess\pp2023\pw4\domains"
#sys.path.insert(0, module_path)
from domains import Manager
def main():
    manager = Manager.Manager()
    while True:
        print('Enter your choice: ')
        print('1. Add information ')
        print('2. Get information ')
        print('3. Change infomation')
        print('4. Remove infomation')
        print('5. Exit ')
        choice = input('Choice: ')
        if choice == '1':
            manager.add_Info()
        elif choice == '2':
            manager.get_Info()
        elif choice == '3':
            manager.change_Info()
        elif choice == '4':
            manager.remove_Info()
        elif choice == '4':
            break
        else:
            print('Please enter valid choice!')

# Call the main function
if __name__ == "__main__":
    main()
