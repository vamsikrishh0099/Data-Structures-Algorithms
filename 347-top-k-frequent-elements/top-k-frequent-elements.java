class Solution {
    public int[] topKFrequent(int[] nums, int k) {

    //     int[] ans = new int[k];
    //    PriorityQueue<List<Integer>> pq = new PriorityQueue<>((list1, list2) -> Integer.compare(list2.get(1), list1.get(1)));
    //    Map<Integer, Integer> mp = new HashMap<>();

    //    for (int x: nums) mp.put(x,mp.getOrDefault(x,0)+1);

    //    for (Map.Entry<Integer, Integer> etr: mp.entrySet()){
    //        int num = etr.getKey();
    //        int freq = etr.getValue();

    //        pq.offer(Arrays.asList(num,freq));
    //    }


    //    for (int i = 0;i<k;i++){
    //        ans[i] = pq.poll().get(0);
    //    }

    //    return ans;


       int[] ans = new int[k];
       
       Map<Integer, Integer> mp = new HashMap<>();

       for (int x: nums) mp.put(x,mp.getOrDefault(x,0)+1);
       int maxcount = 0;
       for (Map.Entry<Integer,Integer> etr: mp.entrySet()){
           maxcount = Math.max(maxcount,etr.getValue());
       }
       List<List<Integer>> counter = new ArrayList<>();
       for (int i = 0;i<maxcount;i++){
           counter.add(new ArrayList<Integer>());
       }
       
       for (Map.Entry<Integer,Integer> etr: mp.entrySet()){
           int val = etr.getKey();
           int freq = etr.getValue();
           counter.get(freq-1).add(val);
           
       }
       
       int j = 0;
       for (int i = counter.size()-1;i >=0;i--){
           if (k == 0) break;

           List<Integer> cur = counter.get(i);
           for (int x: cur){
               if (k == 0) return ans;
               ans[j++] = x;
               k--;
           }
       }

       return ans;
       

       





    }
}