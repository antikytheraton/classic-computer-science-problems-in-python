from typing import List
from hanoi import Stack

num_discs: int = 2
tower_a: Stack[int] = Stack()
tower_b: Stack[int] = Stack()
tower_c: Stack[int] = Stack()
for i in range(1, num_discs + 1):
    tower_a.push(i)

def hanoi(begin: Stack[int], end: Stack[int], temp: Stack[int], n: int) -> None:
    '''
        Steps:
            1. Move the upper n-1 discs from tower A to B (the temporary tower),
                using C as the in-between.
            2. Move the single lowest disc from A to C.
            3. Move the n-1 discs from tower B to C, using A as the in-between
    '''

    for _ in range(1, n-1):
        end.push(begin.pop())
        temp.push(begin.pop())
        temp.push(end.pop())

    end.push(begin.pop())

    for _ in range(1, n-1):
        begin.push(temp.pop())
        end.push(temp.pop())
        end.push(begin.pop())

    

if __name__ == "__main__":
    print(f'A: {tower_a},\t\t B: {tower_b},\t\t C: {tower_c}')
    hanoi(tower_a, tower_c, tower_b, num_discs)
    print(f'A: {tower_a},\t\t B: {tower_b},\t\t C: {tower_c}')
