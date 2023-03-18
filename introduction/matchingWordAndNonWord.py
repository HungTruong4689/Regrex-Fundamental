Regex_Pattern = r"\w{3}\W\w{10}\W\w{3}"	# Do not delete 'r'.

# Regex Pattern:
# .
# ├── \w{3}
# │   ├── \w - Denotes a word character (equal to [a-zA-Z0-9_])
# │   └── {3} - Denotes the above expression for 3 times
# ├── \W
# │   └── Denotes any non-word character (equal to [^a-zA-Z0-9_])
# ├── \w{10}
# │   ├── \w - Denotes a word character (equal to [a-zA-Z0-9_])
# │   └── {10} - Denotes the above expression for 10 times
# ├── \W
# │   └── Denotes any non-word character (equal to [^a-zA-Z0-9_])
# └── \w{3}
#     ├── \w - Denotes a word character (equal to [a-zA-Z0-9_])
#     └── {3} - Denotes the above expression for 3 times


import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())