class BaseClass:
    def __init__(self, value):
        self._value = value
    
    def _show_value(self):
        print(f"BaseClass Value: {self._value}")
    
    def get_value(self):
        return self._value
    
    def set_value(self, value):
        print(f"Setting value to {value}")
        self._value = value


class SubClass(BaseClass):
    def __init__(self, value, extra_value):
        super().__init__(value)
        self._extra_value = extra_value
    
    def display(self):
        self._show_value()
        print(f"SubClass Extra Value: {self._extra_value}")
    
    def _show_value(self):
        print(f"SubClass Modified Value: {self._value}")
    
    def modify_value(self, new_value):
        print(f"SubClass Modifying value...")
        self.set_value(new_value)



obj = SubClass(10, 20)
obj.display()
print(f"Initial Base Value: {obj.get_value()}")

obj.modify_value(30)
obj.display()
print(f"Updated Base Value: {obj.get_value()}")
