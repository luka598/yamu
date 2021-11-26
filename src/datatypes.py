class text():
	def __init__(self, text="", tags=[], section_level=0) -> None:
		self.text = text
		self.tags = tags
		self.section_level = section_level
		return

	def plain_text(self):
		return self.text

	def __repr__(self) -> str:
		return self.plain_text()

class section():
	def __init__(self, start=True, tags=[], section_level=0) -> None:
		self.start = start
		self.tags = tags
		self.section_level = section_level
		return

	def plain_text(self):
		return ""

class bold(text):
	def plain_text(self) -> str:
		return self.text.upper()