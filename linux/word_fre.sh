grep -oE '[a-z]+' file.txt| sort | uniq -c | sort -r | awk '{print $2, $1}'
## the first will split all the words in the txt 
## the second will order them in alphabeta order
## the third gives unique number on each cluster 
## the fourth sort in reverse order
## the fifth prints the second part first, then the first part