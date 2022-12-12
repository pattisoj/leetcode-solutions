class Solution(object):
    def simplifyPath(self, path):
        directory_list = path.split("/")
        stack = []
        for directory in directory_list:
            if directory == "..":
                if len(stack)>0:
                    stack.pop()
            elif directory != "." and len(directory)>0:
                stack.append(directory)
        
        return "/"+"/".join(stack)