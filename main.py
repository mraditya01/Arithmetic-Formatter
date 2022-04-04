# This entrypoint file to be used in development. Start by reading README.md
from pytest import main

from arithmetic_arranger import arithmetic_arranger
d=False

print(arithmetic_arranger(["1 + 99", "2 + 32"],True))
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"],True))
