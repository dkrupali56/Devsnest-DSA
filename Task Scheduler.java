static int solve(int n, String[] tasks, int k){
            int[] counter = new int[26];
        int max = 0;
        int maxCount = 0;
        for(String task : tasks) {
            char ch=task.charAt(0);
            counter[ch - 'A']++;
            if(max == counter[ch - 'A']) {
                maxCount++;
            }
            else if(max < counter[ch - 'A']) {
                max = counter[ch - 'A'];
                maxCount = 1;
            }
        }
        
        int partCount = max - 1;
        int partLength = k - (maxCount - 1);
        int emptySlots = partCount * partLength;
        int availableTasks = tasks.length - max * maxCount;
        int idles = Math.max(0, emptySlots - availableTasks);
        
        return tasks.length + idles;
}
