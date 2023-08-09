import re

name = input("What's your name? ").strip()
"""
if "," in name:
    last,first = name.split(", ")
    name = f"{first} {last}"
print(f"hello, {name}")
"""
"""
matches = re.search(r"^(.+), *(.+)$", name)
if matches:
    name = matches.group(2) + " " + matches.group(1)
"""
if matches := re.search(r"^(.+), *(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")
"""
LETS LEARN THIS STEP BY STEP AGAIN
-re.search = using the re library function to specifically search something
-(r"") regex syntax.. like the f string of (f"")
-^ $ means the everything in between of the string needs to be literal
-(.+) lets split this
    -() means its inside a group and is considered one entity
    -.+ means any 1 character except a newline and 1 or more repititions
-"," means there has to be a "," in the input
-" *" means there has to be a space or not in the input, * meaning 0 or more reps
-(.+) has already been explained
-string.group() = is a re library function that gets the groups inside the regex
    -in this case there are two groups, two () ()
"""
