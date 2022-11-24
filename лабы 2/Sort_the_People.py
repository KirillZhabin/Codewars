class Solution:
    def sortPeople(self, name: list[str], height: list[int]) -> list[str]:
        length = len(name)
        for i in range(length - 1):
            for j in range(i + 1, length):
                if height[i] < height[j]:
                    name[i] = name[j] 
		    name[j] = name[i]
                    height[i] = height[j] 
		    height[j] = height[i]
        return name