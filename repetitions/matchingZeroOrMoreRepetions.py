Regex_Pattern = r'^\d{2,}[a-z]*[A-Z]*$'	# Do not delete 'r'.


# Regex Pattern:
# .
# ├── ^
# │   └── Denotes the start of the line
# ├── \d{2,}
# │   ├── \d - Denotes a digit (equal to [0-9])
# │   └── {2,} - Denotes the above expression for 2 or more times
# ├── [a-z]*
# │   ├── a-z - Denotes a single character in the range of a and z
# │   └── * - Denotes the above expression for 0 or unlimited times, same as {0,}
# ├── [A-Z]*
# │   ├── A-Z - Denotes a single character in the range of A and Z
# │   └── * - Denotes the above expression for 0 or unlimited times, same as {0,}
# └── $
#     └── Denotes the end of the line


import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())