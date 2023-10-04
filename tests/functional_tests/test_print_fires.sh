test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run basic_add python calc.py add 1 1
assert_in_stdout 2
assert_exit_code 0

run basic_div python calc.py div 1 0
assert_exit_code 0