def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")
        
print_kwargs(name="uday",power="fire")
print_kwargs(name="uday")
print_kwargs(name="uday",power="fire",enemy="dr.jackel")

