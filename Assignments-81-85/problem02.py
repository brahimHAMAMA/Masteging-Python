# Create Your Decorator Here
def myDecorator(fun):
    def nested():
        print("Sugar Added From Decorators")
        fun()
        print("####################")
    return nested()

@myDecorator
def make_tea():
  print("Tea Created")
@myDecorator
def make_coffe():
  print("Coffe Created")

make_tea()
make_coffe()

# Needed Output

"Sugar Added From Decorators"
"Tea Created"
"####################"
"Sugar Added From Decorators"
"Coffe Created"
"####################"