a = [1,2,3,4,5,6,7,8]
even = list(filter(lambda a:a%2==0,a))
for i in even:
    print("even no =",i)

print("__________________________")


new_value = [67,34,89,45,12,21,16,90]
# Creating a function

def filtered_val(val):
    if val >= 29:
        return True

new_result = filter(filtered_val,new_value)
print(list(new_result))
        