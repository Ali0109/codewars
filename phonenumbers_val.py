import phonenumbers
import re

phone = "+998971111111"
# phone = ''.join(re.split('\D+', phone))
x = phonenumbers.parse(phone)
y = phonenumbers.is_valid_number(x)
print(y)

