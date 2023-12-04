import re

regex = re.findall(r'(?<=[qwrtypsdfghjklzxcvbnm])[AEIOUaeiou]{2,}(?=[qwrtypsdfghjklzxcvbnm])', input())

if regex:
    for match in regex:
        print(match)
else:
    print('-1')