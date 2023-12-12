class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Add everything to hash table for O(1) lookup

        hash_table = collections.defaultdict(int)

        for i in nums:
            if i in hash_table:
                hash_table[i] += 1
            else:
                hash_table[i] = 1

        hash_table = sorted(hash_table.items(), key = lambda x:x[1], reverse=True)
        print(hash_table)
        solution_list = []

        for i in range(0, k):
            solution_list.append(hash_table[i][0])

        return solution_list
