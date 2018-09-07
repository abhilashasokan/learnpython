# Python Functions
# ****************
# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.

def greetings(customer_name = "Customer"):
    print("Hai " +customer_name)
    return 10
greetings("Abhilash")
greetings("Aparna")
abc = greetings()
print(abc)
