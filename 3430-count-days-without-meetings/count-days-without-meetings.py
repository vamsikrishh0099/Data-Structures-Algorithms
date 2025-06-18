class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        """
        first merge intervals.
        and count gaps

        """
        # Handle empty meetings case
        if not meetings:
            return days
        
        # Sort meetings by start time
        meetings.sort(key=lambda x: x[0])
        
        free = 0
        # Days before the first meeting
        free += max(0, meetings[0][0] - 1)
        
        # Track current merged interval
        curr_start, curr_end = meetings[0]
        
        # Process each meeting
        for start, end in meetings[1:]:
            if curr_end >= start:  # Overlapping or touching intervals
                curr_end = max(curr_end, end)
            else:  # Non-overlapping, calculate gap
                free += start - curr_end - 1
                curr_start, curr_end = start, end
        
        # Days after the last merged interval
        free += max(0, days - curr_end)
        
        return free