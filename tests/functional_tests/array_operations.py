import sys
import my_utils

sys.path.append("../../src")

op = sys.argv[1]
str_arr = sys.argv[2].split(",")
arr = [float(i) for i in str_arr]

if op == "mean":
    print(my_utils.array_mean(arr))
elif op == "median":
    print(my_utils.array_median(arr))
elif op == "stdev":
    print(my_utils.array_stdev(arr))
