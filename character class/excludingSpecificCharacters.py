Regex_Pattern = r'^\D[^aeiou][^bcDF]\S[^AEIOU][^.,]$'	# Do not delete 'r'.


# Regex Pattern:
# .
# ├── ^
# │   └── Denotes the start of the line
# ├── \D
# │   └── Denotes any character that is not a digit (equal to [^0-9])
# ├── [^aeiou]
# │   └── Denotes any single character not included in the list 'aeiou'
# ├── [^bcDF]
# │   └── Denotes any single character not included in the list 'bcDF'
# ├── \S
# │   └── Denotes any non-whitespace character (equal to [^\r\n\t\f\v ])
# ├── [^AEIOU]
# │   └── Denotes any single character not included in the list 'AEIOU'
# ├── [^.,]
# │    └── Denotes any single character not included in the list '.,'
# └── $
#     └── Denotes the end of the line
import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())