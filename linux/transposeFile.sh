rm -rf file1.txt
echo "name age location" >> file1.txt
echo "alice 21 USA" >> file1.txt
echo "ryan 30 CH"  >> file1.txt

# Read from the file file.txt and print its transposed content to stdout.

# NF: Columns for the file 
# NR: rows for the file
# Line is a new variable that will absorb the required inputs

awk '
    {
        for (i=1; i<=NF; i++) {
            if (line[i] == "") { line[i] = $i } 
            else { line[i] = line[i]" "$i }
        }
    } END {
        for (i=1; line[i]!= ""; i++) { print line[i] }
    }
' file1.txt

#the first line iterate over the column
#the second line determine if the new variable line at ith row is empty
#    if it is then
#                 add the the element on the ith column in file to the ith row of line
#    otherwise
#                change the element on ith row of line to the original one appended by ith column in file
#return the result line
#for every element in line
#             print line

