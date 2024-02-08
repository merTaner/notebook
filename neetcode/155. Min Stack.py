"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

    MinStack() initializes the stack object.
    void push(int val) pushes the element val onto the stack.
    void pop() removes the element on the top of the stack.
    int top() gets the top element of the stack.
    int getMin() retrieves the minimum element in the stack.

You must implement a solution with O(1) time complexity for each function.

 

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2

 

Constraints:

    -231 <= val <= 231 - 1
    Methods pop, top and getMin operations will always be called on non-empty stacks.
    At most 3 * 104 calls will be made to push, pop, top, and getMin.


Takeaway:


"""

class MinStack:

    def __init__(self):
        """Create empty stack"""
        self._stack = []

    def push(self, val: int) -> None:
        """Add element to the top of the stack"""
        self._stack.append(val)

    def pop(self) -> None:
        """Remove and return the element from the top of the stack"""
        if len(self._stack) == 0:
            raise 'Stack is empty'
        self._stack.pop()

    def top(self) -> int:
        """Return(but do not remove) top items of the stack."""
        if len(self._stack) == 0:
            raise 'Stack is empty'
        return self._stack[-1]

    def getMin(self) -> int:
        pass


    
if __name__ == '__main__':
    obj = MinStack()
    print(obj.push(-2))
    print(obj.push(0))
    print(obj.push(3))
    print(obj.getMin())
    print(obj.pop())
    print(obj.top())
    print(obj.getMin())
