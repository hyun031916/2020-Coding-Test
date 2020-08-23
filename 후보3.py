def mask_security_number(security_number):
   security_number_list = list(security_number)
   if len(security_number_list) == 14:
       security_number_list[10:15] = ["*","*","*","*"]
   else:
       security_number_list[9:14] = ["*","*","*","*"]
   return ''.join(security_number_list)

def mask_security_number_2(security_number):
   return security_number[:len(security_number) - 4] + "****"

print(mask_security_number("030319-4000000"))
print(mask_security_number_2("030319-4200000"))