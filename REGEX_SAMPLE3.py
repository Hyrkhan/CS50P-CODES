import re

url = input("URL: ").strip()

#username = url.replace("https://twitter.com/", "")
"""
username = url.removeprefix("https://twitter.com/")
print(f"Username: {username}")
"""
"""
username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
print(f"Username: {username}")
"""
"""
if matches := re.search(r"^https?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
    print(f"Username: ", matches.group(2))
"""
if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)$", url, re.IGNORECASE):
    print(f"Username: ", matches.group(1))
"""
LETS LEARN THIS STEP BY STEP AGAIN
-re.search = using the re library function to specifically search something
-(r"") regex syntax.. like the f string of (f"")
-^ $ means the everything in between of the string needs to be literal
-https? means the character before "?" is not required to be present.. meaning
    that its ok for the input to be http or https
-:// means there has to be this specific characters in the input
-(?:www\.)? lets split this
    -() means its a group and is considered as one entity
    -?: means you will not catch/return this group (it will not be among the
        list of groups when you use string.group())
    -www\. means there has to be a "www" and a "." dot on the input
    -()? meaning this group is not required for the input.. meaning it is ok for
        it to not be entered by the user
-twitter\.com/ means this specific characters are needed in the input
-([a-z0-9_]+) lets split this
    -() means its a group and you can catch it later for string.group()
    -[a-z0-9_] means everything not from a to z, 0 to 9 and an underscore is not
        allowed in the input
    -[]+ means there has to be 1 or more of this in the input
"""
