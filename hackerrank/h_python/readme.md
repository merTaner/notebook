## Best Practice Python

* Ascii Function
Return reable type any object (int, list, str...) 

* __function__
Methods with a double underscore before and after their name are considered as built-in methods. They are used by interpreters and are generally used in the implementation of overloaded operators or other built-in functionality.
__add__-> Can be overloaded for + operation
__sub__ -> Can be overloaded for - operation

* “Dunder Method” (Double Underscore Method” (also called “magic method”))
we should use 'return Points()' statement because __sub__ function calculates subtraction from two points object and return it.

* Power of Lambda Function <br>
`
for list_items in sorted(arr, key=lambda x: x[k]):
    print(*list_items)
`

#### Regex

+ --> 1 or more occurrences of the pattern to its left e.x : "^[789]\d{9}+$"
* --> 0 or more occurrences of the pattern to its left
? --> match 0 or 1 occurrences of the pattern to its left

#### functools

- reduce -> like map func but usually used for math compute.

Also the function do cumulative calculation.


