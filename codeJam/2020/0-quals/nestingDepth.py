test_cases = int(input().strip())

for case_number in range(test_cases):

    output_string = "".join([int(i) * "(" + i + int(i) * ")" for i in input().strip()])

    while output_string.find(")(") != -1:
        output_string = output_string.replace(")(", "")

    print("Case #{}: {}".format(case_number+1, output_string))
