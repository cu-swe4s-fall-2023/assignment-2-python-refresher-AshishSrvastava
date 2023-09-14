def get_column(file_name, query_column, query_value, result_column):
    """extracts a target (result) column of data from a CSV file based on 
    a query value in a query column
     
        
    Parameters
    ----------
    file_name : the name of the file to read
    
    query_column : the index of the column to query
    
    query_value : the value to match in the query column
    
    result_column : the index of the column whose values will be returned
    
    Returns
    -------
    result_column_accumulator 
        the column of data that matches the query value
    """
    result_column_accumulator = []
    with open(file_name) as f:
        lines_array = [line.split(',') for line in f]
        # Skip header column
        for line in lines_array[1:]:
            if line[query_column] == query_value:
                result_column_accumulator.append(line[result_column])
    return result_column_accumulator