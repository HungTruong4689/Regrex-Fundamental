Regex_Pattern = r'^[1-3][0-2][xs0][30Aa][xsu][.,]$'	# Do not delete 'r'.


# Regex Pattern:
# .
# ├── ^
# │   └── Denotes the start of the line
# ├── [1-3]
# │   └── Denotes a single character in the range of 1 and 3
# ├── [0-2]
# │   └── Denotes a single character in the range of 0 and 2
# ├── [xs0]
# │   └── Denotes a single character from the list 'xs0'
# ├── [30Aa]
# │   └── Denotes a single character from the list '30Aa'
# ├── [xsu]
# │    └── Denotes a single character from the list 'xsu'
# ├── [.,]
# │    └── Denotes a single character from the list '.,'
# └── $
#     └── Denotes the end of the line
import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())