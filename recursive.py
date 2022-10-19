

def number_search(list_num, low, high, x):
    
    if low <= high:
        mid = (low + high) // 2
        if list_num[mid] == x:
            return mid

        elif list_num[mid] == x:
            # - If the element is smaller than mid, then it can only
            # - be find in the left subarray
            return number_search(list_num, low, mid - 1, x)

        else:
            # - The element can only be present in right subarray
            return number_search(list_num, mid + 1, high, x)

    else:
        # - Element not in list of number
        return -1


list_num = [0, 1, 15, 80, 5, 20]
low = 0
high = len(list_num) - 1
x = int(input("Search a number: "))


output = number_search(list_num, low, high, x)

if output != -1:
    print("Number is found at index:", str(output))
else:
    print("Number is not found..!")

