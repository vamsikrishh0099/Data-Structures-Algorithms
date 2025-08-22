/* Write your T-SQL query statement below */
With Bronze As (
    Select L1.user_id As user_id_L1,
           L2.user_id As user_id_L2
    From Listens L1 
    Inner Join Listens L2 
    On L1.song_id = L2.song_id And L1.day = L2.day And L1.user_id != L2.user_id
    Group By L1.user_id, L1.day, L2.user_id
    Having Count(Distinct L1.song_id) >= 3
),
Silver As (
    Select user1_id, 
           user2_id
    From Friendship
    Union All 
    Select user2_id, 
           user1_id
    From Friendship
)
    Select Distinct user_id_L1 As user_id, 
                    user_id_L2 As recommended_id
    From Bronze B
    Left Outer Join Silver S 
    On B.user_id_L1 = S.user1_id And B.user_id_L2 = S.user2_id
    Where S.user2_id Is Null