# As the engeneering

## learn about others

https://elevatorworld.com/article/optimization-of-elevator-dispatching-by-using-genetic-algorithm-in-python/


## Code review



There are three types of elevator control systems that I am aware of: rheostat, push-button, and destination-control. Your simulator does not simulate any one of those three types.

I suggest you try to implement a simulation closer to whatever elevator model you actually have in mind. Be LITERAL! If you want to simulate a push-button elevator, with [UP] and [DN] buttons on each floor, then do that! Create floors. Give them an up and a down button. Give them lights. Provide an elevator cab interface with buttons, and the super-irritating "door open" and "door close" buttons that don't appear to do anything.

Next, implement the strategy pattern to make the elevator control algorithm pluggable. There are a number of competing algorithms for elevators, so why not support more than one?

You might consider threads, or async, in order to support some simultaneity: you want to be able to handle buttons pressed while the elevator is moving.

Finally, move your argument parsing setup into main(). And get rid of namespace - use args or something more comprehensible.


## which algorythm

- LOOK
- KNN
