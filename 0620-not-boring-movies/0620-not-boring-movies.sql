# Write your MySQL query statement below
SELECT * FROM CINEMA WHERE MOD(ID,2)!=0 AND DESCRIPTION !='boring' order by  rating desc;