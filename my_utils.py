def get_column(file_name, query_column, query_value, result_column=1):
    """extracts a target (result) column of data from a CSV file based on 
    a query value in a query column
     
        
    Parameters
    ----------
    file_name : the name of the file to read
    
    query_column : the index of the column to query
    
    query_value : the value to match in the query column
    
    result_column : the index of the column whose values will be extracted
    
    Returns
    -------
    result_column_accumulator 
        the column of data that matches the query value
    """
    result_column_string_accumulator = []
    try:
        with open(file_name, 'r') as f:
            lines_array = [line.split(',') for line in f]
            # Skip header column
            for line in lines_array[1:]:
                # Error handling for if result_column switches values to none
                if line[query_column] == query_value and result_column != None:
                    result_column_string_accumulator.append(line[result_column])

        result_column_int_list = [float_to_int(string_to_float(i)) for i in result_column_string_accumulator]
        return result_column_int_list
    except FileNotFoundError:
        print(f"Error: No file with the name {file_name} found")
        raise
    except PermissionError:
        print(f"Error: Permission denied for file {file_name}")
        raise
    
def string_to_float(string):
    """converts a string to a float
    
    Parameters
    ----------
    string : the string to convert
    
    Returns
    -------
    float
        the string converted to a float
    """
    try:
        return float(string)
    except ValueError:
        print(f"Error: {string} is not a number")
        raise

def float_to_int(float):
    """converts a float to an int
    
    Parameters
    ----------
    float : the float to convert
    
    Returns
    -------
    int
        the float converted to an int
    """
    try:
        return int(float)
    except ValueError:
        print(f"Error: {float} is not a number")
        raise