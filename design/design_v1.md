## Design Junco version1

<strong>Aim: </strong>have a simple GUI tool to help me read code faster, statically. Roast me if you think this is useless. I didn't want to spend time dive deep into dynamic analysis or some fancy control flow. 

For now, I will do this for C code. Maybe later update and add C++ too. Then Python...

Obiviously, when reading a large code base, I will not have to time or energy to read all of them. However, knowing the big picture of the code base like what libraries were used in this file or is this header file included in other places etc will make my life better if I am simply reading just one particular feature, so I won't need to keep opening and finding the header files here and there and then take a bunch of notes that I wouldn't reference too much, making the process tedious. 

The name "Junco" is actually a snowbird's name. I started this project during winter and it is going to be a light weight tool, so I call it like that.

OK.

### User Interface

Show directories and the files. If user selects the file, the user will be able to see a dependency graph of the file, like #include "headerfile.h" is from this location and that location, and is also in xxx.c file. See! convinent! I didn't want to make this a code editor so the user can just open their own IDE to edit the code or view details of the code. This is merely a code statistic tool.

For C++ and Python, I might add something like class relation stuff etc, not sure now. But for dependency graph, it shouldn't be complicated. OK.

### How to do it?

Well, I feel like doing this on local web page. GUI is fine, but I don't feel like doing it because it makes me feel a little tedious...web based stuff seems really straight forward and the point of doing this little tool is to do it in a short amount of time, so there.

I will probably use flask to do it. I will use python to scan the whole code directory: scan the file names, the #includes in the files line by line, (still thinking about the function names...), then store it in a data structure, like json, and then use a library to display the graphs and statics i.e. file #include graphs, lines of code, # of functions, xxx function occured in xx,xx,xx files at line xxx, etc...using html templates to show on web.

