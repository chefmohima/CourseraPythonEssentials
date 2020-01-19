"""
Project for Week 4 of "Python Data Representations".
Find differences in file contents.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

IDENTICAL = -1

def singleline_diff(line1, line2):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
    Output:
      Returns the index where the first difference between
      line1 and line2 occurs.

      Returns IDENTICAL if the two lines are the same.
    """
    if len(line1) == len(line2):
        same_length = True
    else:
        same_length = False
    min_length = min(len(line1), len(line2))
    for index in range(min_length):
        if (line1[index] != line2[index]):
            return index
    # if no difference found check lengths
    if same_length:
        return IDENTICAL
    else:
        return min_length
     


def singleline_diff_format(line1, line2, idx):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
      idx   - index at which to indicate difference
    Output:
      Returns a three line formatted string showing the location
      of the first difference between line1 and line2.

      If either input line contains a newline or carriage return,
      then returns an empty string.

      If idx is not a valid index, then returns an empty string.
    """
    min_length = min(len(line1), len(line2))
    if (idx < 0) or (idx > min_length) or ("\n" in line1) or ("\n" in line2):
        return ''
    midline = "=" * idx + "^"
    result = line1 + "\n" + midline + "\n" + line2  + "\n"
    return result


def multiline_diff(lines1, lines2):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.

      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """
    if not lines1 and not lines2:
        return(-1, -1)
    if not lines1 or not lines2:
        return(0, 0)
    # check if lengths are same
    if len(lines1) == len(lines2):
        same_length = True
    else:
        same_length = False
    min_length = min(len(lines1), len(lines2))
    for idx in range(min_length):
        diff_index = singleline_diff(lines1[idx], lines2[idx])
        if diff_index != IDENTICAL:
            return(idx, diff_index)
    # no index found, now check lengths
    if same_length:
        return(IDENTICAL, IDENTICAL)
    else:
        return(idx+1, 0)
            
        
        
    
    #return (IDENTICAL, IDENTICAL)


def get_file_lines(filename):
    """
    Inputs:
      filename - name of file to read
    Output:
      Returns a list of lines from the file named filename.  Each
      line will be a single line string with no newline ('\n') or
      return ('\r') characters.

      If the file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    list_lines = []
    file_handle = open(filename, 'rt')
    for line in file_handle.readlines():
        list_lines.append(line.rstrip())
        
    return list_lines


def file_diff_format(filename1, filename2):
    """
    Inputs:
      filename1 - name of first file
      filename2 - name of second file
    Output:
      Returns a four line string showing the location of the first
      difference between the two files named by the inputs.

      If the files are identical, the function instead returns the
      string "No differences\n".

      If either file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    list_lines1 = get_file_lines(filename1)
    list_lines2 = get_file_lines(filename2)
    (line_number, index) = multiline_diff(list_lines1, list_lines2)
    if (line_number, index) == (IDENTICAL, IDENTICAL):
        return "No differences\n"
    part1 = 'Line ' + str(line_number) + ':'
    part2 = singleline_diff_format(list_lines1[line_number], list_lines2[line_number], index)
    return part1 + "\n" + part2
  
    
