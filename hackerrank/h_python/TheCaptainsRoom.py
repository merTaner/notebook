"""
Mr. Anant Asankhya is the manager at the INFINITE hotel. The hotel has an infinite amount of rooms.

One fine day, a finite number of tourists come to stay at the hotel.
The tourists consist of:
→ A Captain.
→ An unknown group of families consisting  K of  members per group where K ≠ 1.

The Captain was given a separate room, and the rest were given one room per group.

Mr. Anant has an unordered list of randomly arranged room entries. 
The list consists of the room numbers for all of the tourists. 
The room numbers will appear K times per group except for the Captain's room.

Mr. Anant needs you to help him find the Captain's room number.
The total number of tourists or the total number of groups of families is not known to you.
You only know the value of K and the room number list.

Sample Input

5
1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2 

Sample Output

8

"""


# from collections import Counter

# gruop_size = int(input())
# room_numbers = Counter(list(map(int, input().split())))
# print(room_numbers)
# print(room_numbers.most_common()[:-2:-1][0][0])

k = int(input())

rooms = list(map(int, input().split()))

rooms_set = set(rooms)

for room in rooms_set:
    rooms.remove(room)

room_set2 = set(rooms)

print(*rooms_set.difference(room_set2))
