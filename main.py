# welcome & get inputs
print("<< welcome to the calculator >>")
print("enter your first number :", end=" ")
num_1 = input()
num_1 = int(num_1)
print("enter your operation :", end=" ")
operation = input()
print("enter your secend number :", end=" ")
num_2 = input()
num_2 = int(num_2)
# process 
if operation == "+":
    result = num_1 + num_2
elif operation == "-":
    result = num_1 - num_2
elif operation == "*":
    result = num_1 * num_2
elif operation == "/":
    result = num_1 / num_2
else:
    result = f"operation '{operation}' is not known"
# display 
print(result)

