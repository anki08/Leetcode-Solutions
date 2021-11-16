from collections import defaultdict
class Solution:
    def sum(self, array):
        hashmap = {}
        hashmap_index = defaultdict(list)
        for i in range(len(array)):
            for j in range(i+1, len(array)):
                sum = array[i]+array[j]
                if sum in hashmap and sum in hashmap_index and i not in hashmap_index[sum] and j not in hashmap_index[sum]:
                    hashmap[sum] += 1
                    hashmap_index[sum].append(i)
                    hashmap_index[sum].append(j)

                elif sum in hashmap and sum in hashmap_index and i in hashmap_index[sum] or j in hashmap_index[sum]:
                    continue
                elif sum not in hashmap:
                    hashmap[sum] = 1
                    hashmap_index[sum] = [i]
                    hashmap_index[sum].append(j)

        max_val = max(hashmap.values())
        print(hashmap)
        for key, val in hashmap.items():
            if val == max_val:
                return hashmap[key]

if __name__ == '__main__':
    sol = Solution()
    # print(sol.sum([1,9,8,100, 2]))
    print(sol.sum([2,2,3,2,3]))
    # print(sol.sum([5,5]))
    # print(sol.sum([5,5,5]))
    # print(sol.sum([5,5,5,5]))
