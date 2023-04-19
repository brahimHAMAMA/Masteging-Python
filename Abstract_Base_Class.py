from abc import ABCMeta, abstractmethod
class Programming(metaclass = ABCMeta):
    @abstractmethod
    def has_oop(s):
        pass
    @abstractmethod
    def has_name(s):
        pass

class Python(Programming):
    def has_oop(s):
        return "Yes"

class Pascal(Programming):
    def has_oop(s):
        return "No"
    def has_name(s):
        return "Pascal"



one = Pascal()

print(one.has_oop())
print(one.has_name())

