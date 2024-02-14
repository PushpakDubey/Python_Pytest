class StringUtils:
    def reverse_string(self, s):
        s = list(s)
        l = len(s)
        for n1 in range(l):
            for n2 in range(0, l - n1 - 1):
                s[n2], s[n2 + 1] = s[n2 + 1], s[n2]
        return ''.join(s)

    def is_palindrome(self, s):
        if s == self.reverse_string(s):
            return True
        else:
            return False

    def is_anagram(self, s1, s2):
        return sorted(s1) == sorted(s2)

    def is_pangram(self, s):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        for char in alphabet:
            if char not in s.lower():
                return False
        return True

    def is_isogram(self, s):
        s = s.lower()
        for char in s:
            if s.count(char) > 1:
                return False
        return True

    def is_vowel(self, c):
        return c.lower() in "aeiou"

    def is_consonant(self, c):
        return c.lower() in "bcdfghjklmnpqrstvwxyz"

    def is_numeric(self, s):
        return s.isnumeric()

    def is_alpha(self, s):
        return s.isalpha()

    def is_alphanumeric(self, s):
        return s.isalnum()

    def is_lower(self, s):
        return s.islower()

    def is_upper(self, s):
        return s.isupper()

    def to_upper(self, s):
        return s.upper()

    def to_lower(self, s):
        return s.lower()

    def capitalize(self, s):
        return s.capitalize()

    def title(self, s):
        return s.title()

    def swap_case(self, s):
        return s.swapcase()

    def reverse_words(self, s):
        return ' '.join(s.split()[::-1])

    def reverse_words_in_sentence(self, s):
        return ' '.join([self.reverse_string(word) for word in s.split()])

    def count_vowels(self, s):
        return sum([1 for char in s if self.is_vowel(char)])

    def count_consonants(self, s):
        return sum([1 for char in s if self.is_consonant(char)])

    def count_digits(self, s):
        return sum([1 for char in s if char.isdigit()])

    def count_alpha(self, s):
        return sum([1 for char in s if char.isalpha()])

    def count_alphanumeric(self, s):
        return sum([1 for char in s if char.isalnum()])

    def count_words(self, s):
        return len(s.split())

    def count_sentences(self, s):
        return len(s.split('.'))

    def count_paragraphs(self, s):
        return len(s.split('\n'))

    def count_occurrences(self, s, sub):
        return s.count(sub)

    def count_occurrences_insensitive(self, s, sub):
        return s.lower().count(sub.lower())

    def remove_whitespace(self, s):
        return ''.join(s.split())

    def remove_whitespace_left(self, s):
        return s.lstrip()

    def remove_whitespace_right(self, s):
        return s.rstrip()

    def remove_whitespace_both(self, s):
        return s.strip()

    def remove_whitespace_multiple(s):
        return ' '.join(s.split())

    def remove_whitespace_all(self, s):
        return ''.join(s.split())

    def base64_encode(self, s):
        return s.encode('base64')
