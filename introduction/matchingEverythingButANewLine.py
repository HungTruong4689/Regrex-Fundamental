regex_pattern = r"^(...\.){3}...$"	# Do not delete 'r'.


# Regex Pattern:
# .
# ├── ^
# │   └── Denotes the start of the line
# ├── (...\.){3}
# │   ├── ... - Denotes any 3 characters
# │   ├── \. - Denotes a '.' character
# │   └── {3} - Denotes the above expression for 3 times
# ├── ...
# │   └── Denotes any 3 characters
# └── $
#     └── Denotes the end of the line

import re
import sys

test_string = input()

match = re.match(regex_pattern, test_string) is not None

print(str(match).lower())