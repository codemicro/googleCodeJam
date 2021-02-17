test_cases = int(input().strip())

for case_number in range(test_cases):

    current_parens_level = 0

    input_string = "0" + input().strip() + "0"
    output_string = ""

    for char_index in range(1, len(input_string)):
        n = int(input_string[char_index])

        diff = n - current_parens_level
        current_parens_level = n

        bracket = "("
        if diff < 0:
            bracket = ")"

        output_string += (bracket * abs(diff)) + str(n)

    output_string = output_string[:-1]  # remove final extra zero

    print("Case #{}: {}".format(case_number+1, output_string))
