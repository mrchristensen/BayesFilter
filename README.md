# Bayes Filter
In this example a robot is placed randomly in the world and tries to figure out where it is.
The robot is able to move (north, south, east, west) or stay in place and also have the ability
to sense if there is a wall nearby (in front, behind, left, or right).  However, movement and sensors
have a probability of misbehaving, adding randomness to the model.

We use [Bayes Rule](https://en.wikipedia.org/wiki/Bayes%27_theorem) to create positional probabilities that are updated after each action are taken.
Used are a combination of the transition model (to probability of moving to a new square given previous positional
probabilities — ```p(xₜ | aₜ, xₜ₋₁)```), and a sensor model (which updates the probability with the likelihood that a
given position matches the observed sensor readings — ```p(zₜ | xₜ)```), to figure out where the robot is in the world.

![](https://github.com/mrchristensen/BayesFilter/blob/master/images/BayesFilter.PNG)

Here, ```Bel(Xₜ₋₁)``` is the robot’s beliefs about where it is in the world (over its possible set of states ```Xₜ₋₁```),
at is the action taken at time ```ₜ```, and ```zₜ``` is the sonar reading taken after moving in time ```ₜ```. Also, the
variable ```η```, is a normalization factor, as ```Bel(xₜ)``` will not define a legal probability distribution.

# Value Iteration
Additionally, the robot is able to move on its own by making action decisions through a [value iteration algorithm](https://en.wikipedia.org/wiki/Markov_decision_process#Value_iteration).
The value iteration algorithm is a [Markov Decision Process](https://en.wikipedia.org/wiki/Markov_decision_process) (MDP), where each state is given a utility based of off a
current and future reward.  Specific to the value iteration implementation of the MDP, we introduce a function ```π```,
which decreases the value of utility over time (which guarantees that utilities will never grow to infinity).

![](https://github.com/mrchristensen/BayesFilter/blob/master/images/value%20iteration.jpg)

Here, ```Pₔ(s,s')``` represents the probability of getting to state ```s'``` from ```s``` with the action ```ₔ```,
```Rₔ(s,s')``` represents the utility function/value for state ```s``` (we use a simplified model that doesn't require ```s'```),
and ```π Vᵢ(s')``` represents the implied future reward of moving to state ```s'```, with the damping factor of ```π```
(with ```ᵢ``` representing the current iteration).

We iteratively apply this algorithm until the utility map is not updated (in which case we have finish).

The algorithm finds the space with the highest probability, and then checks which action would move the robot to the
state with the highest utility.

For this project, we chose to give open spaces an immediate reward utility value of -1, stairwells a value of -10000,
and the goal a value of 10000.

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

## Automatic (value iteration algorithm decides where to go):

### mundo_maze.txt 1 1 known
![](https://github.com/mrchristensen/BayesFilter/blob/master/images/automatic/mundo_maze.txt%201%201%20known.gif)

### mundo_maze2.txt .8 .8 unknown
![](https://github.com/mrchristensen/BayesFilter/blob/master/images/automatic/mundo_maze2.txt%20.8%20.8%20unknown.gif)

### mundo_15_15.txt .9 .9 unknown
![](https://github.com/mrchristensen/BayesFilter/blob/master/images/automatic/mundo_15_15.txt%20.9%20.9%20unknown.gif)

### mundo_30_30.txt .9 .9 unknown
![](https://github.com/mrchristensen/BayesFilter/blob/master/images/automatic/mundo_30_30.txt%20.9%20.9%20unknown.gif)

# How to run:

Server: ```java BayesWorld [world] [motor_probability] [sensor_probability] [known/unknown]``` (For example, ```java BayesWorld mundo_maze.txt 0.9 0.8 unknown```)

The "world" param can be any of the worlds specified in the “Mundo” directory,[motor_probably] is a
value between 0 and 1 specifying pm, [sensor_probability] is a value between 0 and 1 specifying
ps, and “known” specifies that the robot’s initial position is given to the robot at the start of the
simulation, and “unknown” is specified to say that the robot’s initial position is not given to the robot at
the start of the simulation.

Client: ```java theRobot [manual/automatic] [decisionDelay]``` (For example, ```java theRobot manual 0```)

The “manual” param specifies that the user (you) will specify the robot’s actions, “automatic” specifies that
the robot will control its own actions, and [decisionDelay] is a time in milliseconds used to slow
down the robot’s movements when it chooses automatically (so you can see it move). In manual mode,
you press keys to have the robot move when the client GUI window is active. ```i``` is up, ```,``` is down, ```j``` is
left, ```l``` is right, and ```k``` is stay. Note that the client GUI must be the active window in order for the key
commands to work.


## Dev Notes

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
