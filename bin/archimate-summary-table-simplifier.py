#!/usr/bin/env python3
import re
import sys

s = sys.stdin.read()

# Delete tags
s = re.sub(r"</?(p|span)\b[^>]*>", r"", s)

# Chop secondary images
s = re.sub(r"(&nbsp;)+ <img [^>]*>", r"", s)

# Omit borders
s = re.sub(r"\sborder=\"\d+\"", r"", s)

# Omit tag attributes
s = re.sub(r"<(table|tr|td) [^>]*>", r"<\1>", s)

# Trim leading space
s = re.sub(r"\s*\n\s*<(/td)>", r"<\1>", s)

# Trim trailing space
s = re.sub(r"<(td)>\s*\n\s*", r"<\1>", s)

# Make src URLs absolute
s = re.sub(r" src=\"", r" src=\"https://pubs.opengroup.org/architecture/archimate31-doc/", s)

# Tweak language
s = re.sub(r"<td>Represents ", r"<td>", s)

print(s)
