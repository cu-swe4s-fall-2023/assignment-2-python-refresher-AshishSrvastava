def array_mean(array):
    """Calculates the mean of an array of numbers

    Parameters
    ----------
    array: an array of numbers

    Returns
    -------
    float
        the mean of the array
    """
    try:
        if not isinstance(array, list):
            raise TypeError("Error: array_mean() expects a list")
        return sum(array) / len(array)
    except ZeroDivisionError:
        raise ValueError("Error: array_mean() expects a non-empty list")


def array_median(array):
    """Calculates the median of an array of numbers

    Parameters
    ----------
    array: an array of numbers

    Returns
    -------
    float
        the median of the array
    """
    try:
        sorted_array = sorted(array)
        if len(sorted_array) % 2 == 1:
            return sorted_array[len(sorted_array) // 2]
        else:
            m1 = sorted_array[len(sorted_array) // 2 - 1]
            m2 = sorted_array[len(sorted_array) // 2]
            return (m1 + m2) / 2
    except TypeError:
        raise TypeError("Error: array_median() expects a list of numbers")


def array_variance(array):
    """Calculates the variance of an array of numbers

    Parameters
    ----------
    array: an array of numbers

    Returns
    -------
    float
        the variance of the array
    """
    try:
        mean = array_mean(array)
        return sum([(i - mean) ** 2 for i in array]) / len(array)
    except TypeError:
        raise TypeError("Error: array_variance() expects a list of numbers")


def array_stdev(array):
    """Calculates the standard deviation of an array of numbers

    Parameters
    ----------
    array: an array of numbers

    Returns
    -------
    float
        the standard deviation of the array
    """
    try:
        return array_variance(array) ** 0.5
    except TypeError:
        raise TypeError("Error: array_stdev() expects a list of numbers")


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
    except TypeError:
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
        with open(file_name, "r") as f:
            lines_array = [line.split(",") for line in f]
            # Skip header column
            for line in lines_array[1:]:
                # Error handling for if result_column switches values to none
                if (
                    line[query_column] == query_value
                    and result_column is not None
                ):
                    result_column_string_accumulator.append(
                        line[result_column]
                    )

        result_column_int_list = [
            float_to_int(string_to_float(i))
            for i in result_column_string_accumulator
        ]
        return result_column_int_list
    except FileNotFoundError:
        print(f"Error: No file with the name {file_name} found")
        raise
    except PermissionError:
        print(f"Error: Permission denied for file {file_name}")
        raise
