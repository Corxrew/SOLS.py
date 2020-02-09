"""
Planner for Yahtzee by Ayush
Simplifications:  only allow discard and roll, only score against upper level
"""

# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(20)

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """

    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set



def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.
    hand: full yahtzee hand
    Returns an integer score
    """
    # a score list
    # list[0] = score at ones
    # list[1] = score at twos
    # list[2] = score at threes
    # list[3] = score at fours
    # ....
    # score_list = [0 for score_idx in range(4)]
    score_tuple = ()

    for dice in hand:
        temp = dice * hand.count(dice)
        score_tuple = score_tuple + (temp,)

    return max(score_tuple)


def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value of the held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.
    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled
    Returns a floating point expected value
    """
    # should assert that if held_dice + num_free_dice == the total number of dice
    outcomes = [number + 1 for number in range(num_die_sides)]

    possible_rolls = gen_all_sequences(outcomes, num_free_dice)
    exp_value = 0
    total_score = 0
    for roll in possible_rolls:
        total_dice = held_dice + roll
        total_score += score(total_dice)

    exp_value += total_score / float(len(possible_rolls))

    return exp_value


def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.
    hand: full yahtzee hand
    Returns a set of tuples, where each tuple is dice to hold
    """
    holds = set([()])

    if len(hand) == 0:
        return holds
    else:
        temp = hand[:-1]
        for tuplez in gen_all_holds(temp):
            holds.add(tuplez)
            holds.add((tuplez + (hand[-1],)))

    return holds


def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.
    hand: full yahtzee hand
    num_die_sides: number of sides on each die
    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    holds_dict = {}
    possible_hold = gen_all_holds(hand)

    for hold in possible_hold:
        exp_val = expected_value(hold, num_die_sides, len(hand) - len(hold))
        holds_dict[hold] = holds_dict.get(hold, exp_val)

    temp_list = []
    for key, value in holds_dict.items():
        temp_list.append((value, key))

    return sorted(temp_list, reverse = True)[0]


def test_strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.
    hand: full yahtzee hand
    num_die_sides: number of sides on each die
    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    holds_dict = {}
    possible_hold = gen_all_holds(hand)

    for hold in possible_hold:
        exp_val = expected_value(hold, num_die_sides, len(hand) - len(hold))
        holds_dict[hold] = holds_dict.get(hold, exp_val)

    return holds_dict


def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    hand = (1, 1, 1, 5, 6)
    hand_score, hold = strategy(hand, num_die_sides)
    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score

run_example()


#import poc_holds_testsuite
#poc_holds_testsuite.run_suite(gen_all_holds)
