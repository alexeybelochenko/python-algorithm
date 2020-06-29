# I'm sure, you know Google's "Did you mean ...?", when you entered a search term and mistyped a word. In this kata we want to implement something similar.

# You'll get an entered term (lowercase string) and an array of known words (also lowercase strings). Your task is to find out, which word from the dictionary is most similar to the entered one. The similarity is described by the minimum number of letters you have to add, remove or replace in order to get from the entered word to one of the dictionary. The lower the number of required changes, the higher the similarity between each two words.

# Same words are obviously the most similar ones. A word that needs one letter to be changed is more similar to another word that needs 2 (or more) letters to be changed. E.g. the mistyped term berr is more similar to beer (1 letter to be replaced) than to barrel (3 letters to be changed in total).

# Extend the dictionary in a way, that it is able to return you the most similar word from the list of known words.


class Dictionary:
    def __init__(self, words):
        self.words = words 

    def find_most_similar(self, term):
        mw = len(term)
        word = ''
        for w in self.words:
            ld = Dictionary.levenshetein(term, w)
            if ld < mw:
                mw = ld
                word = w
        
        return word


    @staticmethod
    def levenshetein(s1, s2):
        if len(s1) < len(s2):
            return Dictionary.levenshetein(s2, s1)
        
        if len(s2) == 0:
            return len(s1)
        

        previous_row = range(len(s2)+1)
        for i, c1 in enumerate(s1):
            current_row = [i + 1]
            for j, c2 in enumerate(s2):
                insertions = previous_row[j + 1] + 1
                deletions = current_row[j] + 1
                substitutions = previous_row[j] + (c1 != c2)
                current_row.append(min(insertions, deletions, substitutions))
            previous_row = current_row


        return previous_row[-1]
