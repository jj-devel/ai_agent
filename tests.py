from functions.get_file_content import get_file_content
from functions.write_file import write_file

print("Result for current directory: \n", write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
print("Result for 'pkg' directory: \n", write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
print("Result for '/bin' directory: \n", write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))
