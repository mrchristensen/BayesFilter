# Bayes Filter
In this example a robot is placed randomly in the world and tries to figure out where it is.
The robot is able to move (north, south, east, west) or stay in place and also have the ability
to sense if there is a wall nearby (in front, behind, left, or right).  However, movement and sensors
have a probability of misbehaving, adding randomness to the model.

We use Bayes Rule to create positional probabilities that are updated after each action are taken.
Used are a combination of the transition model (to probability of moving to a new square given previous positional
probabilities — ```p(xₜ | aₜ, xₜ₋₁)```), and a sensor model (which updates the probability with the likelihood that a given position matches
the observed sensor readings — ```p(zₜ | xₜ)```), to figure out where the robot is in the world.

![](https://github.com/mrchristensen/BayesFilter/blob/master/images/BayesFilter.PNG)

Here, ```Bel(Xₜ₋₁)``` is the robot’s beliefs about where it is in the world (over its possible set of states ```Xₜ₋₁```),
at is the action taken at time ```ₜ```, and ```zₜ``` is the sonar reading taken after moving in time ```ₜ```. Also, the
variable ```η```, is a normalization factor, as ```Bel(xₜ)``` will not define a legal probability distribution.

# Recordings

## Manual (player inputted decisions):

### mundo_maze.txt .95 .9 unknown
![](https://github.com/mrchristensen/BayesFilter/blob/master/images/manual/mundo_maze.txt%20.95%20.9%20unknown.gif)

### mundo_maze2.txt .8 .8 unknown
![](https://github.com/mrchristensen/BayesFilter/blob/master/images/manual/mundo_maze2.txt%20.8%20.8%20unknown.gif)

### mundo_15_15.txt .9 .9 unknown
![](https://github.com/mrchristensen/BayesFilter/blob/master/images/manual/mundo_15_15.txt%20.9%20.9%20unknown.gif)

### mundo_30_30.txt .85 .8 unknown
![](https://github.com/mrchristensen/BayesFilter/blob/master/images/manual/mundo_30_30.txt%20.85%20.8%20unknown.gif)


# How to run:

Server: ```java BayesWorld [world] [motor_probability] [sensor_probability] [known/unknown]``` (For example, ```java BayesWorld mundo_maze.txt 0.9 0.8 unknown```)

The "world" param can be any of the worlds specified in the “Mundo” directory,[motor_probably] is a
value between 0 and 1 specifying pm, [sensor_probability] is a value between 0 and 1 specifying
ps, and “known” specifies that the robot’s initial position is given to the robot at the start of the
simulation, and “unknown” is specified to say that the robot’s initial position is not given to the robot at
the start of the simulation.

Client: ```java theRobot [manual/automatic] [decisionDelay]``` (For example, ```java theRobot manual 0```)

The “manual” param specifies that the user (you) will specify the robot’s actions, “automatic” specifies that
the robot will control it’s own actions, and [decisionDelay] is a time in milliseconds used to slow
down the robot’s movements when it chooses automatically (so you can see it move). In manual mode,
you press keys to have the robot move when the client GUI window is active. ‘i’ is up, ‘,’ is down, ‘j’ is
left, ‘l’ is right, and ‘k’ is stay. Note that the client GUI must be the active window in order for the key
commands to work.


## Remember

0's are open
1's are walls
2's are traps
3's are the goal

NORTH = 0
SOUTH = 1
EAST = 2
WEST = 3
STAY = 4

sonar string 1001, specifies:
wall in the North and West directions
but not in the South and East directions



Thinks:
up is left
Right is down,
Down if right
Left is up