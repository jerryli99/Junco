#===- cindex-dump.py - cindex/Python Source Dump -------------*- python -*--===#
#
# Part of the LLVM Project, under the Apache License v2.0 with LLVM Exceptions.
# See https://llvm.org/LICENSE.txt for license information.
# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
#
#===------------------------------------------------------------------------===#

# import time


# """
# A simple command line tool for dumping a source file using the Clang Index
# Library.
# """

# def get_diag_info(diag):
#     return { 'severity' : diag.severity,
#              'location' : diag.location,
#              'spelling' : diag.spelling,
#              'ranges' : diag.ranges,
#              'fixits' : diag.fixits }

# def get_cursor_id(cursor, cursor_list = []):
#     if not opts.showIDs:
#         return None

#     if cursor is None:
#         return None

#     # FIXME: This is really slow. It would be nice if the index API exposed
#     # something that let us hash cursors.
#     for i,c in enumerate(cursor_list):
#         if hash(cursor) == hash(c): #indeed, with the hash, the speed is faster.
#             return i
#     cursor_list.append(cursor)
#     return len(cursor_list) - 1

# def get_info(node, depth=0):
#     if opts.maxDepth is not None and depth >= opts.maxDepth:
#         children = None
#     else:
#         children = [get_info(c, depth+1)
#                     for c in node.get_children()]
#     return { 'id' : get_cursor_id(node),
#              'kind' : node.kind,
#              'usr' : node.get_usr(),
#              'spelling' : node.spelling,
#              'location' : node.location,
#              'extent.start' : node.extent.start,
#              'extent.end' : node.extent.end,
#              'is_definition' : node.is_definition(),
#              'definition id' : get_cursor_id(node.get_definition()),
#              'children' : children }

# def main():
#     from clang.cindex import Index
#     from pprint import pprint

#     from optparse import OptionParser, OptionGroup

#     global opts

#     parser = OptionParser("usage: %prog [options] {filename} [clang-args*]")
#     parser.add_option("", "--show-ids", dest="showIDs",
#                       help="Compute cursor IDs (very slow)",
#                       action="store_true", default=False)
#     parser.add_option("", "--max-depth", dest="maxDepth",
#                       help="Limit cursor expansion to depth N",
#                       metavar="N", type=int, default=None)
#     parser.disable_interspersed_args()
#     (opts, args) = parser.parse_args()

#     if len(args) == 0:
#         parser.error('invalid number arguments')

#     index = Index.create()
#     tu = index.parse(None, args)
#     if not tu:
#         parser.error("unable to load input")

#     pprint(('diags', [get_diag_info(d) for d in  tu.diagnostics]))
#     pprint(('nodes', get_info(tu.cursor)))

# if __name__ == '__main__':
#     start_time = time.time()
#     main()
#     print("--- %s seconds ---" % (time.time() - start_time))


# def main():
#     import sys
#     from clang.cindex import Index

#     from optparse import OptionParser, OptionGroup

#     parser = OptionParser("usage: %prog [options] {filename} [clang-args*]")
#     parser.disable_interspersed_args()
#     (opts, args) = parser.parse_args()
#     if len(args) == 0:
#         parser.error('invalid number arguments')

#     # FIXME: Add an output file option
#     out = sys.stdout

#     index = Index.create()
#     tu = index.parse(None, args)
#     if not tu:
#         parser.error("unable to load input")

#     # A helper function for generating the node name.
#     def name(f):
#         if f:
#             return "\"" + f.name + "\""

#     # Generate the include graph
#     out.write("digraph G {\n")
#     for i in tu.get_includes():
#         line = "  ";
#         if i.is_input_file:
#             # Always write the input file as a node just in case it doesn't
#             # actually include anything. This would generate a 1 node graph.
#             line += name(i.include)
#         else:
#             line += '%s->%s' % (name(i.source), name(i.include))
#         line += "\n";
#         out.write(line)
#     out.write("}\n")

# if __name__ == '__main__':
#     main()



import os
import clang.cindex

# Set the directory containing your source/header files
directory = ""

# Function name to search for
function_name = 'lua_setfield'

# Dictionary to store function declarations
function_declarations = {}

def find_function_declarations(node):
    if node.kind == clang.cindex.CursorKind.FUNCTION_DECL and node.spelling == function_name:
        location = (node.location.file.name, node.location.line)
        function_declarations[function_name] = location

    # Recursively traverse children nodes
    for child in node.get_children():
        find_function_declarations(child)

def normalize_location(location):
    # Normalize the file name (e.g., convert to absolute path)
    normalized_filename = os.path.abspath(location[0])
    # Return a tuple containing the normalized location
    return (normalized_filename, location[1], location[2])

# Dictionary to store unique function call locations
function_calls = set()

def find_function_occurrences(root):
    stack = [root]

    while stack:
        node = stack.pop()

        if node.kind == clang.cindex.CursorKind.CALL_EXPR and node.spelling == function_name:
            location = (node.location.file.name, node.location.line, node.location.column)
            # Normalize the location before adding it to the set
            normalized_location = normalize_location(location)
            function_calls.add(normalized_location)

        # Add children to the stack
        for child in node.get_children():
            stack.append(child)



# Initialize libclang index
index = clang.cindex.Index.create()

# Traverse all files in the directory
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith((".c", ".cpp", ".h")):
            filename = os.path.join(root, file)

            # Parse the translation unit
            try:
                tu = index.parse(filename)
            except clang.cindex.TranslationUnitLoadError:
                print(f"Error parsing {filename}. Skipping...")
                continue

            # Traverse the AST to find function declarations
            find_function_declarations(tu.cursor)

            # Traverse the AST to find function calls
            find_function_occurrences(tu.cursor)

# Convert set to list and sort by file name
sorted_calls = sorted(list(function_calls), key=lambda x: (x[0], x[1]))


# Print function call locations
for location in sorted_calls:
    filename, line, column = location
    print(f"Function call to '{function_name}' at line {line}, column {column} in file {filename}")

# Print function declarations
if function_name in function_declarations:
    declaration_file = function_declarations[function_name]
    print(f"Function '{function_name}' is declared in file {declaration_file}")
else:
    print(f"Function '{function_name}' is not declared in any of the parsed files")
