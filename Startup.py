import sys
import os

my_package_path = r"C:\Users\s5521746\OneDrive - Bournemouth University\Masterclass Rigging\Test_Module_Scripts_2"

if my_package_path not in sys.path:
    sys.path.append(my_package_path)

print(my_package_path)

import Print_Test_1
import Print_Test_2

Print_Test_1.String_Print_1()
Print_Test_2.String_Print_2()