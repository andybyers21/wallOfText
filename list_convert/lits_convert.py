def create_list(input_txt, output_txt):
    """Takes a text list and converts it to a python list.

    Keyword arguments:
    input_txt -- a text file containing the list of words to convert.
    output_txt -- the name of your output file, which will be created during the
    process. 
    """
    file = open(input_txt, "r")

    list = []

    for line in file:
        line = line.strip()
        list.append(line)
    
    with open(output_txt, 'w') as output:
        for row in list:
            output.write("         '" + str(row) + "',\n")
