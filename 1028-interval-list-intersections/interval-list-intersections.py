class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        """
        2 pointers at start of both lists
        find intersection. 
        if intersection >= 0, add to answer
        move whichever end is smaller
        """
        first_len = len(firstList)
        second_len = len(secondList)

        i = 0
        j = 0
        ans = []

        while i < first_len and j < second_len:
            first_item = firstList[i]
            second_item = secondList[j]

            intersection = min(first_item[1], second_item[1]) - max(first_item[0], second_item[0])

            if intersection >= 0:
                ans.append([max(first_item[0], second_item[0]), min(first_item[1], second_item[1])])

            if first_item[1] < second_item[1]:
                i += 1
            else:
                j += 1

        return ans










