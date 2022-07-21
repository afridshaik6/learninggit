def sort_duplicates(input_str):
    elements_present = set()
    output_list = []
    for i in input_str:
        if i in elements_present:
            output_list.append(i)
        else:
            elements_present.add(i)
    return ''.join(sorted(output_list))

