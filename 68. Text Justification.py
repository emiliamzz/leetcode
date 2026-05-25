class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        output = []
        while len(words) > 0:
            length = len(words[0])
            line = [words.pop(0)]
            while len(words) > 0:
                if length + len(words[0]) + 1 > maxWidth:
                    break
                length += len(words[0]) + 1
                line.append(words.pop(0))
            if len(words) == 0:
                # last line -> left-justified
                string = ' '.join(line)
                if len(string) < maxWidth:
                    string += ''.join([' '] * (maxWidth - len(string)))
                output.append(string)
                return output
            if len(line) == 1:
                # only one word -> left justify
                string = line[0]
                if len(string) < maxWidth:
                    string += ''.join([' '] * (maxWidth - len(string)))
                output.append(string)
            else:
                string_space = maxWidth - length + len(line) - 1
                space = string_space // (len(line) - 1)
                remainder = string_space % (len(line) - 1)
                string = line.pop(0)
                while len(line) > 0:
                    spaces = ''.join([' '] * space)
                    if remainder > 0:
                        spaces += ' '
                        remainder -= 1
                    string += spaces + line.pop(0)
                output.append(string)