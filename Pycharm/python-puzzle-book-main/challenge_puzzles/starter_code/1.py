def filter_strings_containing_a(input_strs: list[str]) -> list[str]:
    oplist = []
    for item in input_strs:
        if "a" in item:
            oplist.append(item)
    return oplist
#Test Cases
#print(filter_strings_containing_a(["apple", "banana", "cherry", "date"]))
#print(filter_strings_containing_a([]))
print (filter_strings_containing_a(["bbb", "ccc"]))