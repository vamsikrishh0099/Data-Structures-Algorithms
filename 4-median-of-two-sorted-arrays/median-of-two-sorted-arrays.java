class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        PriorityQueue<Pair> minheap = new PriorityQueue<>((a,b) -> a.val - b.val);
        int total = nums1.length + nums2.length;
        int ansIndex = 0;
        boolean avg = false;
        if (total %2 != 0 ){
           ansIndex = total/2;
        }
        else{
            ansIndex = total/2;
            avg = true;
        }
        if (nums1.length > 0){
              minheap.offer(new Pair(nums1[0], 0, nums1));
        }
        if (nums2.length > 0){
            minheap.offer(new Pair(nums2[0], 0, nums2));
        }
        
        int c = 0;
        int prev = 0;
        while (!minheap.isEmpty()){
            Pair p = minheap.poll();
            System.out.println(p.val);
            if (c == ansIndex){
                if (avg){
                    return (double)(p.val + prev)/2; 
                }
                else{
                    return (double)(p.val);
                }
            }
            else{
                prev = p.val;
                c++;
                if (p.id < p.arr.length-1){
              minheap.offer(new Pair(p.arr[p.id + 1], p.id + 1, p.arr ));
                }
              
            }

        }
        return prev;

    }

    class Pair{
        int val;
        int id;
        int[] arr;
        public Pair(int val, int id, int[] arr){
            this.val = val;
            this.id = id;
            this.arr = arr;
        }
    }
}