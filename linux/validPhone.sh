#this is wrong
#\{3\} means it appears three times
#\d[3] is three digits
#[] matching any one of the enclosed form
#parenthesis can be added directly
grep '([0-9]\{3\}) [0-9]\{3\}-[0-9]\{4\}\|d[3]-[0-9]\{3\}-[0-9]\{4\}' file.txt





#start with / end with/
#^$
#() will group the patterns 
#when parentheses are needed as in the pattern, will use \( \) instead
#| is or in regex
#[0-9] {3} is to multiply pattern[0-9] three times as pending
awk '/^([0-9]{3}-|\([0-9]{3}\)\ )[0-9]{3}-[0-9]{4}$/' file.txt