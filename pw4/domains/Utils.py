class Utils:
    def __init__(self, args):
        self.set_Name(args)
        self.set_Id(args)
         
    def set_Name(self, args):
        self._name = input(f'Enter {args} name: ')
        while len(self._name) == 0 or not self._name.isalpha():
            self._name = input(f'Please enter valid {args} name: ')

    def set_Id(self, args):
        self._id = int(input(f'Enter {args} ID: '))
        while self.check_Id(self._id) == False:
            self._id = int(input(f'Please enter valid {args} ID: '))

    def get_Name(self):
        return self._name

    def get_Id(self):
        return self._id
    
    def check_Id(self, id):
        if id < 0:
            print('Invalid ID')
            return False
        return True
