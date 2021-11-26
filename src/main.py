from parse import parse
from convert import plaintext
import sys

with open(sys.argv[1], "r") as f:
	file = f.read().replace("\t", "")

tokenized = parse(file)
print(tokenized)
print(plaintext(tokenized))