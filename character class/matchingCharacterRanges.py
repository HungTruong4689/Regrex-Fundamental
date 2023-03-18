Regex_Pattern = r'^[a-z][1-9][^a-z][^A-Z][A-Z]'	# Do not delete 'r'.


# Regex Pattern:
# .
# ├── ^
# │   └── Denotes the start of the line
# ├── [a-z]
# │   └── Denotes a single character in the range of a and z
# ├── [1-9]
# │   └── Denotes a single character in the range of 1 and 9
# ├── [^a-z]
# │    └── Denotes any single character not included in the list 'a-z'
# ├── [^A-Z]
# │    └── Denotes any single character not included in the list 'A-Z'
# └── [A-Z]
#     └── Denotes a single character in the range of A and Z
import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())