#Find the Most Frequent Item in an Array, e.g.,  arr1 = [2, 'b', 1, 'a', 2, 6, 'a', 3, 'b', 2, 9, 3,2], output => 2
def FreqItemCheck(arr: list) -> str:
    return max(arr, key=arr.count)


#Check if a Number is a Palindrome, e.g., 212 => true, 2121 => false
def PalindromeCheck(number: int) -> bool:
    if str(number) == str(number)[::-1]:
        return True
    return False