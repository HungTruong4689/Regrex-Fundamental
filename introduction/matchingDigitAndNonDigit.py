Regex_Pattern = r"^\d{2}.\d{2}.\d{4}"	# Do not delete 'r'.


# Regex Pattern:
# .
# ├── ^
# │   └── Denotes the start of the line
# ├── \d{2}
# │   ├── \d - Denotes a digit (equal to [0-9])
# │   └── {2} - Denotes the above expression for 2 times
# ├── .
# │   └── Denotes any characters
# ├── \d{2}
# │   ├── \d - Denotes a digit (equal to [0-9])
# │   └── {2} - Denotes the above expression for 2 times
# ├── .
# │   └── Denotes any characters
# └── \d{4}
#     ├── \d - Denotes a digit (equal to [0-9])
#     └── {4} - Denotes the above expression for 4 times
import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())