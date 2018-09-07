# If condition
# is_male = True
# is_tall = True
# if is_male and is_tall:
#     print("You are a tall male")
# elif is_male and not(is_tall):
#     print("You are a short male")
# else:
#     print("Female Candidate")

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return str(num1) + " is biggest"
    elif num2 >= num1 and num2 >= num3:
        return str(num2) + " is biggest"
    else:
        return str(num3) + " is biggest"

print(max_num(13,14,17))
# Rest is just like usual c++ operators that we use
