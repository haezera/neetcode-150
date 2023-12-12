class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create an array of dictionaries for each strs char frequency O(n)
        array_of_dicts = []
        for i in strs:
            dict_of_chars = self.createDict(i)
            array_of_dicts.append(dict_of_chars)
        
        solution_array = []
        # Now loop through str list again: nested for loops to check any matches. If any matches
        # occurs, add them to the solution array.
        used_array = [False for i in range(0, len(strs))]


        for i in range(0, len(strs)):
            if used_array[i] is True:
                continue

            new_solution = []
            used_array[i] = True
            new_solution.append(strs[i])
            # Create a new solution array, appending the "static" word
            for j in range(i + 1, len(strs)):
                if used_array[j] is True:
                    continue
                
                if array_of_dicts[i] == array_of_dicts[j]:
                    used_array[j] = True
                    new_solution.append(strs[j])

            solution_array.append(new_solution)

        return solution_array

                

                


    def createDict(self, string: str) -> dict:
        newDict = {}
        for i in range(0, len(string)):
            if string[i] in newDict:
                newDict[string[i]] += 1
            else:
                newDict[string[i]] = 1

        return newDict
