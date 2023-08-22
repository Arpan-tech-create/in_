def find_element(arr,target):

    try:
        index=arr.index(target)
        return index
    except ValueError:
        return -1



input_array=input("Enter array element").split()

input_array=[int(x) for x in input_array]

target_ele=int(input("enter element"))

res=find_element(input_array,target_ele)

if res != -1:
    print(f"The index of {target_ele} is {res}")
else :
    print("no element found")