test_cases = int(input().strip())

cases = []

for test_number in range(test_cases):
    source_string = input().strip()
    cases.append(source_string)

for case_number, data in enumerate(cases):
    case_list = list(data)
    
    sequence = []
    # loop below relies on the existence of at least one item in the list
    sequence.append([case_list[0], 1])  
    
    for index, item in enumerate(case_list[1:]):
        if sequence[-1][0] == item:
            sequence[-1][1] += 1
        else:
            sequence.append([item, 1])

    output_string = ""
    for pair in sequence:
        output_string += "(" * int(pair[0])
        output_string += pair[0] * pair[1]
        output_string += ")" * int(pair[0])

    while output_string.find(")(") != -1:
        output_string = output_string.replace(")(", "")
    
    print("Case #{}: {}".format(case_number+1, output_string))
