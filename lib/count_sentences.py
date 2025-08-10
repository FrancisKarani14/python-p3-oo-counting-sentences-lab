class MyString:
    def __init__(self, value=""):
        self._value = ""  # Use a private variable
        self.value = value  # Will go through setter validation

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            print("The value must be a string.")
            self._value = ""
        else:
            self._value = new_value

    def is_sentence(self):
        """Return True if value ends with a period."""
        return self._value.endswith(".")

    def is_question(self):
        """Return True if value ends with a question mark."""
        return self._value.endswith("?")

    def is_exclamation(self):
        """Return True if value ends with an exclamation mark."""
        return self._value.endswith("!")

    def count_sentences(self):
        """Return number of sentences in value."""
        import re
        sentences = re.split(r'[.!?]', self._value)
        sentences = [s.strip() for s in sentences if s.strip()]
        return len(sentences)
