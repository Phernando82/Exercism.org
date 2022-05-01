"""
Instructions
In this exercise, you need to implement some rules from Pac-Man, the classic 1980s-era arcade-game.
You have four rules to implement, all related to the game states.
Do not worry about how the arguments are derived, just focus on combining the arguments to return the intended result.

1. Define if Pac-Man eats a ghost
Define the eat_ghost() function that takes two parameters (if Pac-Man has a power pellet active and if Pac-Man is touching
a ghost) and returns a Boolean value if Pac-Man is able to eat the ghost. The function should return True only if Pac-Man
has a power pellet active and is touching a ghost.

>>> eat_ghost(False, True)
False

2. Define if Pac-Man scores
Define the score() function that takes two parameters (if Pac-Man is touching a power pellet and if Pac-Man is touching
a dot) and returns a Boolean value if Pac-Man scored. The function should return True if Pac-Man is touching a power pellet
or a dot.

>>> score(True, True)
True

3. Define if Pac-Man loses
Define the lose() function that takes two parameters (if Pac-Man has a power pellet active and if Pac-Man is touching a
ghost) and returns a Boolean value if Pac-Man loses. The function should return True if Pac-Man is touching a ghost and
does not have a power pellet active.

>>> lose(False, True)
True

4. Define if Pac-Man wins
Define the win() function that takes three parameters (if Pac-Man has eaten all of the dots, if Pac-Man has a power pellet
 active, and if Pac-Man is touching a ghost) and returns a Boolean value if Pac-Man wins. The function should return True
 if Pac-Man has eaten all of the dots and has not lost based on the parameters defined in part 3.

>>> win(False, True, False)
False

"""
#######################################################################################################################

"""Functions for implementing the rules of the classic arcade game Pac-Man."""


def eat_ghost(power_pellet_active, touching_ghost):
    """Verify that Pac-Man can eat a ghost if he is empowered by a power pellet.

           :param power_pellet_active: bool - does the player have an active power pellet?
           :param touching_ghost: bool - is the player touching a ghost?
           :return: bool - can the ghost be eaten?
    """
    if power_pellet_active and touching_ghost:
        return True

    return False


def score(touching_power_pellet, touching_dot):
    """Verify that Pac-Man has scored when a power pellet or dot has been eaten.

            :param touching_power_pellet: bool - does the player have an active power pellet?
            :param touching_dot: bool - is the player touching a dot?
            :return: bool - has the player scored or not?
    """
    if touching_power_pellet or touching_dot:
        return True

    return False


def lose(power_pellet_active, touching_ghost):
    """Trigger the game loop to end (GAME OVER) when Pac-Man touches a ghost without his power pellet.

            :param power_pellet_active: bool - does the player have an active power pellet?
            :param touching_ghost: bool - is the player touching a ghost?
            :return: bool - has the player lost the game?
    """
    if not power_pellet_active and touching_ghost:
        return True

    return False


def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    """Trigger the victory event when all dots have been eaten.

                  :param has_eaten_all_dots: bool - has the player "eaten" all the dots?
                  :param power_pellet_active: bool - does the player have an active power pellet?
                  :param touching_ghost: bool - is the player touching a ghost?
                  :return: bool - has the player won the game?
    """
    if not power_pellet_active and touching_ghost:
        lost = True
    else:
        lost = False

    if has_eaten_all_dots and not lost:
        return True

    return False
