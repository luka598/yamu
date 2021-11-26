def plaintext(text):
	plain_text = ""
	for i in text:
		plain_text += i.plain_text()
	return plain_text