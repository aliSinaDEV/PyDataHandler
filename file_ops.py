def read_file(file_name):
    """ Reads in a file.

    Returns:
        string: contents of the given file.
    """
    with open(file_name, 'r') as file_data:
        read_data = file_data.read()

    return read_data
    
    raise NotImplementedError()

def read_file_into_list(file_name):
    """ Reads in a file and stores each line as an element in a list
    Args:
        file_name: the name of the file to be read

    Returns:
        list: a list where each element is a line in the file.
    """
    line_list = []
    with open(file_name, 'r') as file_data:
        read_data = file_data.readlines()
        for x in read_data:
            line_list.append(x)
    
    return line_list

    raise NotImplementedError()

def write_first_line_to_file(file_contents, output_filename):
    first_line = file_contents.split('\n')[0]
    with open(output_filename, 'w') as file_data:
        file_data.write(first_line)

    return first_line
    raise NotImplementedError()


def read_even_numbered_lines(file_name):
    """ Reads in the even-numbered lines of a file

        1. Open and read the given file into a variable
        2. Read the file line-by-line and add the even-numbered lines to a list
        3. Return the list

    Args:
        file_name: the name of the file to be read

    Returns:
        list: a list of the even-numbered lines of the file
    """
    even_lines = []
    with open(file_name, 'r') as file_data:
        read_filedata = file_data.readlines()
        for i, line in enumerate(read_filedata,1):
            if i % 2 == 0:
                even_lines.append(line)

    print(even_lines)  # Print the list of even-numbered lines

    return even_lines

    raise NotImplementedError()

def read_file_in_reverse(file_name):
    """ Reads a file and returns a list of the lines in reverse order

        1. Open and read the given file into a variable
        2. Read the file line-by-line and store the lines in a list in reverse order
        3. Print the list
        4. Return the list

    Args:
        file_name: the name of the file to be read

    Returns:
        list: list of the lines of the file in reverse order.
    """
    reversed_text = []
    with open(file_name, 'r') as file_data:
        read_file_data = file_data.readlines()
        for x in read_file_data[::-1]:
            reversed_text.append(x)

    print(reversed_text)  # Print the reversed list of lines

    return reversed_text




    raise NotImplementedError()

'''
Here are some sample commands to help test the implementations.
Feel free to uncomment/modify/add to them as you wish.
'''
def main():
    file_contents = read_file("sampletext.txt")
    print(read_file_into_list("sampletext.txt"))
    # write_first_line_to_file(file_contents, "online.txt")
    # print(read_even_numbered_lines("sampletext.txt"))
    # print(read_file_in_reverse("sampletext.txt"))

if __name__ == "__main__":
    main()
