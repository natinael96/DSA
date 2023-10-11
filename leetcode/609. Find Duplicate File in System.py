class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dict = {}  # Dictionary 

        for path in paths:
            directory, *files = path.split()  # Split 

            for file in files:
                file_name, cont = file.split('(')  
                cont = cont[:-1]  # Remove ')'

                file_path = directory + '/' + file_name  # file path

                if cont in dict:
                    dict[cont].append(file_path) 
                else:
                    dict[cont] = [file_path] 

        result = [grp for grp in dict.values() if len(grp) > 1]
        return result