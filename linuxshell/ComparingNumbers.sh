# Given two integers, X and Y, identify whether X < Y or X > Y or X = Y.

# Exactly one of the following lines:
# - X is less than Y
# - X is greater than Y
# - X is equal to Y

read X 
read Y

# if you want show to that experation -> (()) 
if (($X > $Y)) 
then
    echo "X is greater than Y"
elif (($X < $Y)) 
then
    echo "X is less than Y"
else
    echo "X is equal to Y"
fi