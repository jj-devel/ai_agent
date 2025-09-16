from functions.get_file_content import get_file_content

print("Result for current directory: \n", get_file_content("calculator", "main.py"))
print("Result for 'pkg' directory: \n", get_file_content("calculator", "pkg/calculator.py"))
print("Result for '/bin' directory: \n", get_file_content("calculator", "/bin/cat"))
print("Result for '../' directory: \n", get_file_content("calculator", "pkg/does_not_exist.py"))
