class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        """
        for each user --> [websites list]
        [w1, w2, w3, w5, w2, w4]
        ...

        subsequence of length 3 that is present in most user's list 

        generate all subsequences of length 3 per user --> update hash map
        """

        

        def get_subsequences(web_list, counter):
            ans = set()
            web_list.sort(key = lambda x: x[1])
            total_visited = len(web_list)

            if total_visited < 3: 
                return
            
            for i in range(total_visited):
                for j in range(i + 1, total_visited):
                    for k in range(j + 1, total_visited):
                        tup = (web_list[i][0], web_list[j][0], web_list[k][0])
                        ans.add(tup)
            for t in ans:

                counter[t] = counter.get(t, 0) + 1

        user_web_map = {}

        for i in range(len(username)):
            uname = username[i]
            web = website[i]
            time = timestamp[i]
            user_web_map[uname] = user_web_map.get(uname, [])
            user_web_map[uname].append((web, time))

        counter = {}

        for user, web_list in user_web_map.items():
            get_subsequences(web_list, counter)

        max_freq = 0
        ans = None

        for tup, count in counter.items():
            if max_freq < count or (max_freq == count and ans > tup ):
                ans = tup
                max_freq = count
           

        
        return list(ans)