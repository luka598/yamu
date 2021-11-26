from parse import parse
from convert import plaintext

with open("test.yamd", "r") as f:
	file = f.read().replace("\t", "")

tokenized = parse(file)

print(plaintext(tokenized))