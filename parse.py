import datatypes as dt

escape_codes = {"\\": dt.text,
				"b": dt.bold,
				"{": dt.text,
				"}": dt.text,
				}

def format_escaped_string(escaped_string, section_level):
	formatted = None
	if escaped_string != "":
				for escape_code in escape_codes.keys():
					if escaped_string.startswith(escape_code):
						formatted = escape_codes[escape_code](text=escaped_string[len(escape_code):], section_level=section_level)
	return formatted

def parse(plaintext):
	escaped = False
	current_string = ""
	text = []
	section_level = 0

	for letter in plaintext:
		if letter == "\\" and escaped == False:
			if len(current_string ) > 0:
				text.append(dt.text(text=current_string))
				current_string = ""
			escaped = True

		elif (letter == " " or letter == "\n") and escaped == True:
			escaped = False
			formatted = format_escaped_string(current_string, escape_codes)
			text.append(formatted)
			current_string = letter

		elif letter == "{" and escaped == False:
			section_level += 1
		elif letter == "}" and escaped == False:
			section_level -= 1
		
		else:
			current_string += letter

	return text