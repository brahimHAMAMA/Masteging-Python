class A:
    def do_something(s):
        print('From class A')


class B(A):
    def do_something(s):
        print('From class B')

my_instance = B()

my_instance.do_something()

print(dir(str))
print(str.__len__)