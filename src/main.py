from parse import parse
from convert import plaintext

with open("test.yamu", "r") as f:
	file = f.read().replace("\t", "")

tokenized = parse(file)
print(tokenized)
print(plaintext(tokenized))