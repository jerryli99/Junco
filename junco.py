
#pip install antlr4-python3-runtime  
#wget https://www.antlr.org/download/antlr-4.13.1-complete.jar -O antlr-4.13.1-complete.jar
#java -jar antlr-4.9.2-complete.jar -Dlanguage=Python3 [change this to something likeCalc.g4] //for generating python files like lexer,parser.py
#python junco.py or just main.py either way



#pip install libclang
# https://libclang.readthedocs.io/en/latest/_modules/clang/cindex.html#Cursor.get_included_file
import sys
import clang.cindex

def find_functions(node):
    if node.kind == clang.cindex.CursorKind.FUNCTION_DECL:
        nm = node.spelling
        print(f"Function {nm}")
    else:
        for c in node.get_children():
            find_functions(c)

index = clang.cindex.Index.create()
tu = index.parse(sys.argv[1])

for i in tu.get_includes():
    print(i.source) #the FileInclusionObject...

print('Translation unit:', tu.spelling)
find_functions(tu.cursor)

# if __name__ == '__main__':
#     main(sys.argv)










# import os 

# print(len(os.listdir()))

# import pathlib

# files = [f for f in pathlib.Path().iterdir() if f.is_file()]


# x = [print(f) for f in files]

# import os

# def get_all_files_in_directory(directory):
#     # List to store all file names
#     file_names = []

#     # Walk through all directories and subdirectories
#     for root, dirs, files in os.walk(directory):
#         # Iterate over each file in the current directory
#         for file in files:
#             # Join the current root directory with the file name to get the full path
#             file_path = os.path.join(root, file)
#             # Append the file path to the list
#             file_names.append(file_path)

#     return file_names

# # Specify the directory path
# directory_path = "C:/Users/jerry/Downloads/lua-master/lua-master"

# # Get all file names in the directory and subdirectories
# all_files = get_all_files_in_directory(directory_path)

# x = [print(f) for f in all_files]



# import os
# import re

# def get_all_files_in_directory(directory):
#     # List to store all file names
#     file_names = []

#     # Walk through all directories and subdirectories
#     for root, dirs, files in os.walk(directory):
#         # Iterate over each file in the current directory
#         for file in files:
#             # Join the current root directory with the file name to get the full path
#             file_path = os.path.join(root, file)
#             # Append the file path to the list
#             file_names.append(file_path)

#     return file_names

# def extract_information_from_c_file(file_path):
#     # List to store include statements, function names, and macro names
#     includes = []
#     functions = []
#     macros = []

#     # Regular expressions to match include statements, function declarations, and macros
#     include_pattern = r'#include\s+["<](.+?)[">]'
#     function_pattern = r'\b(?:int|void|char|float|double)\s+(\w+)\s*\([^;]*\)'
#     macro_pattern = r'#define\s+(\w+)'

#     # Read the file line by line
#     with open(file_path, 'r', encoding='utf-8') as file:
#         for line in file:
#             # Match include statements
#             include_matches = re.findall(include_pattern, line)
#             includes.extend(include_matches)

#             # Match function declarations
#             function_matches = re.findall(function_pattern, line)
#             functions.extend(function_matches)

#             # Match macros
#             macro_matches = re.findall(macro_pattern, line)
#             macros.extend(macro_matches)

#     return includes, functions, macros

# # Specify the directory path
# directory_path = ""

# # Get all file names in the directory and subdirectories
# all_files = get_all_files_in_directory(directory_path)

# # Process each file
# for file_name in all_files:
#     includes, functions, macros = extract_information_from_c_file(file_name)
    
#     # Print the extracted information for the current file
#     print("File:", file_name)
#     print("Includes:", includes)
#     print("Functions:", functions)
#     print("Macros:", macros)
#     print()

# import os
# import re

# def get_all_c_files_in_directory(directory):
#     # List to store all file names
#     c_files = []

#     # Walk through all directories and subdirectories
#     for root, dirs, files in os.walk(directory):
#         # Iterate over each file in the current directory
#         for file in files:
#             # Check if the file has a .c extension
#             if file.endswith('.h'):
#                 # Join the current root directory with the file name to get the full path
#                 file_path = os.path.join(root, file)
#                 # Append the file path to the list
#                 c_files.append(file_path)

#     return c_files

# def extract_information_from_c_file(file_path):
#     # List to store include statements, function names, and macro names
#     includes = []
#     functions = []
#     macros = []

#     # Regular expressions to match include statements, function declarations, and macros
#     include_pattern = r'#include\s+["<](.+?)[">]'
#     function_pattern = r'\b(?:int|void|char|float|double)\s+(\w+)\s*\([^;]*\)'
#     macro_pattern = r'#define\s+(\w+)'

#     # Read the file line by line with explicit encoding
#     with open(file_path, 'r', encoding='latin-1') as file:
#         for line in file:
#             # Match include statements
#             include_matches = re.findall(include_pattern, line)
#             includes.extend(include_matches)

#             # Match function declarations
#             function_matches = re.findall(function_pattern, line)
#             functions.extend(function_matches)

#             # Match macros
#             macro_matches = re.findall(macro_pattern, line)
#             macros.extend(macro_matches)

#     return includes, functions, macros

# # Specify the directory path
# directory_path = ""

# # Get all .c file names in the directory and subdirectories
# all_c_files = get_all_c_files_in_directory(directory_path)

# # Process each .c file
# for c_file in all_c_files:
#     includes, functions, macros = extract_information_from_c_file(c_file)
    
#     # Print the extracted information for the current .c file
#     print("File:", c_file)
#     print("Includes:", includes)
#     print("Functions:", functions)
#     print("Macros:", macros)
#     print()

