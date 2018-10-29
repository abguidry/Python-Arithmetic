### Defs file names for read and write###
fileinput = input( " Read From: " )
fileoutput = input( " Write to: " )



### Hocus Pocus Open Seasame (The files magically opened)###
f = open(fileinput , 'r');
w = open(fileoutput, 'w');



### Sets up my program to run in the fashion of a hula hoop###
for line in f:
### Much like needed groceries, slap those values on a list###
    y = line.split()

############################################################################
#EACH OF THESE WRITE THE ANSWER AND GO TO THE NEXT LINE
############################################################################



### Tells prog that + means add###
    if y[1] == "+":
        y = float(y[0]) + float(y[2])
        y = str(y)
        w.write(y + "\n")
### Tells prog / means divide###
    elif y[1] == "/":
        y = float(y[0]) / float(y[2])
        y = str(y)
        w.write(y + "\n")
### Tells prog - means subtract###
    elif y[1] == "-":
        y = float(y[0]) - float(y[2])
        y = str(y)
        w.write(y + "\n")
### Tells prog % means modulus###
    elif y[1] == "%":
        y = float(y[0]) % float(y[2])
        y = str(y)
        w.write(y + "\n")
### Defines ^ as ** and means exponentiate###
    elif y[1] == "^":
        y = float(y[0]) ** float(y[2])
        y = str(y)
        w.write(y + "\n")
### Tells prog * means multiply###
    elif y[1] == "*":
        y = float(y[0]) * float(y[2])
        y = str(y)
        w.write(y + "\n")

### When one door closes...(two files close so stuff will save.....)
f.close()
w.close()
        

print('Done. ')
input("Enter to exit...")
