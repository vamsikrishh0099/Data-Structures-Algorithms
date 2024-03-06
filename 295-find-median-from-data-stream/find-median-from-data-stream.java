class MedianFinder {
     Queue<Integer> minheap;
     Queue<Integer> maxheap;
    public MedianFinder() {
        minheap = new PriorityQueue<Integer>();
        maxheap = new PriorityQueue<Integer>(Collections.reverseOrder());

    }
    
    public void addNum(int num) {

        minheap.add(num);

        maxheap.add(minheap.peek());
        minheap.poll();

        if (maxheap.size() > minheap.size() + 1){
            minheap.add(maxheap.poll());
        }

      

    }
    
    public double findMedian() {
        
        if (minheap.size() == maxheap.size()){
            return (double)((minheap.peek() + maxheap.peek())*0.5);
        }
        else if (minheap.size() > maxheap.size()){
            return minheap.peek();
        }
        else return maxheap.peek();
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */