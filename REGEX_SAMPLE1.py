import re

email = input("What's your email? ").strip()
"""
if "@" in email and "." in email:
    print("Valid")
else:
    print("Invalid")
"""
"""
username, domain = email.split("@")

if (username) and domain.endswith(".edu"):
    print("Valid")
else:
    print("Invalid")
"""
"""
 . = any 1 character except a newline
 * = 0 or more repititions
 + = 1 or more repititions
 ? = 0 or 1 repititions
 {n} = number of repititions
 {n1, n2} = n1 - n2 number of repititions
 ^ = matches the start of the string
 $ = matches the end of the string or just before the newline
     at the end of the string
[] = set of characters
[^] = complementing the set
A|B = either A or B using |
(...) = a group
(?:...) = non-capturing version
\d = decimal digit
\D = not a decimal digit
\s = whitespace characters
\S = not a whitespace character
\w = word characters as well as numbers and underscore
\W = not a word character
"""
"""
 use \ to indicated that you want that character literally in there
 want to have a literal . so used \.
 if re.search(r"^.+@.+\.edu$", email):
 [^@] means any character except the "@" sign
 if re.search(r"^[^@]+@[^@]+\.edu$", email):
 [a-zA-Z0-9_] means only accepting from a to z, captial a to z, numbers, and _
 if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):
 \w means any word character (same as [a-zA-Z0-9_])
 re.IGNORECASE means ignoring case when validating regex(.com or .edu)
"""

if re.search(r"^\w+@(\w+\.)?\w+\.(com|edu)$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")
"""
LETS LEARN THIS STEP BY STEP AGAIN
-re.search = using the re library function to specifically search something
-(r"") regex syntax.. like the f string of (f"")
-^ $ means the everything in between of the string needs to be literal
-\w means we are allowing all word characters(letters and numbers) and an underscore
-\w+ the + means there has to be atleast 1 \w characters or more
-@ means there has to be only one of such character
-(\w+\.)? lets split this
    -the () means it is inside a group (meaning it is one entity)
    -\w+ there has to be 1 or more word characters
    -\. there has to be one "."
    -()? means this group can be present or not in the input
-\w+\. means there has to be 1 or more wordcharacters and a "." dot
-(com|edu) lets split this
    -() means it is a group
    -com|edu means either "com" OR "edu" has to be present on the input
-re.IGNORECASE = a re library function that ignores case in the input
"""
