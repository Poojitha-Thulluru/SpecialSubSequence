def special_sub_sequence_AG(string: str) -> int:
    a_count: int = 0
    ag_count: int = 0
    for char in string:
        if char == 'A':
            a_count += 1
        elif char == 'G':
            ag_count += a_count
    return ag_count


try:
    string = input("Enter a string : ")
    print(special_sub_sequence_AG(string))
except ValueError:
    print("Invalid Input. Please enter only strings")
