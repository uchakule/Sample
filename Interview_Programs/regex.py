
## To find mobile number and email from raw string ##

import re

str = """hi 987654 how are you 8329749174 and
        +9123456789 uchakule@gmail.com umeshchakule@gmail.com"""

email = re.findall(r'\S+@+\S+',str)
number = re.findall(r'\d{10}',str)

print(email)
print(number)