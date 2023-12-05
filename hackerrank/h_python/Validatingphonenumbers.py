import re

p = re.compile(r"^[789]\d{9}+$")
for iter_count in range(int(input())):
    phone_number = input()
    match = re.search(p, phone_number)

    if match:
        print("YES")
    else:
        print("No")
    