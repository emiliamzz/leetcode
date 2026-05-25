class Solution:
    def simplifyPath(self, path: str) -> str:
        arr = path.split('/')
        new_arr = []
        for item in arr:
            if item == '..':
                if len(new_arr) > 0:
                    new_arr.pop(-1)
            elif item != '' and item != '.':
                new_arr.append(item)
        return '/' + '/'.join(new_arr)