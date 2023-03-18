Regex_Pattern = r"^\d\w{4}\.$"	# Do not delete 'r'.


# Regex Pattern:
# .
# ├── ^
# │   └── Denotes the start of the line
# ├── \d
# │   └── Denotes a digit (equal to [0-9])
# ├── \w{4}
# │   ├── \w - Denotes a word character (equal to [a-zA-Z0-9_])
# │   └── {4} - Denotes the above expression for 4 times
# ├── \.
# │   └── Denotes a '.' character
# └── $
#     └── Denotes the end of the line

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())