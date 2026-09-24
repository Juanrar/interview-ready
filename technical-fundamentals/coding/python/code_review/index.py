# Code review exercise: find the problems in this code.
# It is intentionally flawed and is not meant to run.

import logging


# non-declarative naming
def map_array(array):
    return [bool(el) for el in array]


class Player:
    pass


player = None


# declarative naming mismatch
def get_player():
    global player
    if not player:
        player = Player()
    return player


# use named parameters
def evaluate_challenge(challenge, result, candidate, difficulty):
    if challenge == result:
        return f"{candidate} has successfully completed the {difficulty} challenge"
    return f"{candidate}'s submission is incorrect"


# Oversplitting functions - "The rule of 3"


def split_words(string):
    return string.split(" ")


def word_mapper(words):
    global hash_
    hash_ = {}
    result = []
    for word in words:
        hash_[word] = 0 if hash_.get(word) else hash_.get(word, 0) + 1
        result.append(hash_[word])
    return result


def word_counter(string):
    return word_mapper(split_words(string))


# Avoid side effects

tracker = {}


def count_views(key):
    if not tracker.get(key):
        tracker[key] = 0
    tracker[key] += 1
    return tracker[key]


# Variables & Control Flow
"""
- Declarative Variable Naming
- Avoid Magic Numbers
- Avoid comments - code as documentation
- Avoid while loops
- Avoid large Conditional clauses
- Variable scoping
- Do not modify inputs
- Cyclomatic Complexity
    - Early returns
    - Replace nesting with variables or top level fn calls
"""


def parse_people(people):
    group_a = []  # minors
    group_b = []  # adults
    group_c = []  # elderly

    i = 0
    while i < len(people):
        person = people[i]
        if person.get("age") and person["age"] > 18:
            if person.get("age") and person["age"] > 60:
                group_c.append(person)
            else:
                group_b.append(person)
        elif person.get("age"):
            group_a.append(person)
        else:
            people[i] = None  # remove invalid records
        i += 1

    return [group_a, group_b, group_c]


# General Programming

# DRY


def init_tic_tac_toe():
    board = [[None for _ in range(3)] for _ in range(3)]
    board[1][1] = "X"
    return board


def init_connect4():
    board = [[None for _ in range(7)] for _ in range(6)]
    board[0][0] = "O"
    return board


def init_sudoku():
    return [[None for _ in range(9)] for _ in range(9)]


# Over-abstractions


def pass_interview(candidate, interview):
    interview.finished()
    candidate.passed()
    candidate.submit_offer()


def fail_interview(candidate, interview):
    interview.finished()
    candidate.failed()
    candidate.submit_feedback()


def complete_interview(candidate, interview, result):
    interview.finished()

    if result == "passed":
        pass_interview(candidate, interview)
    else:
        fail_interview(candidate, interview)


# Atomicity


def transfer_money(sender, receiver, amount):
    sender.funds -= amount

    if sender.funds < 0:
        sender.funds += amount
        raise Exception("Insufficient funds")

    if receiver.disabled_user():
        raise Exception("Receiver is unable to receive funds")

    receiver.funds += amount
    return [sender, receiver]


# General over specific


def format_serial_names(name, version):
    return f"series-{name}-{version}"


def format_product_names(name, series):
    return f"{series}-product-{name}"


# Error handling

# Defensive Programming (Questionable)


def validate_user(user):
    if not isinstance(user, object) or type(user).__name__ != "User":
        return False
    has_name = bool(user.name)
    return has_name


# Invariant Programming (Good!)


def validate_user(user):  # noqa: F811
    valid_user = type(user).__name__ == "User"
    assert valid_user, f"Invalid user object {user}"
    has_name = bool(user.name)
    return has_name


# Error Management

# Catch what you can handle
# Add context
# Do not eat errors

MAX_RETRIES = 3


async def update_user_bad(user, retries):
    try:
        await API.update_user(user)
    except Exception as e:
        if MAX_RETRIES == 3:
            return

        if is_fetch_error(e):
            return await update_user_bad(user, retries + 1)
        raise

    return user


async def update_user_good(user, retries):
    try:
        await API.update_user(user)
    except Exception as e:
        if MAX_RETRIES == 3:
            raise Exception(
                f"User {user.id} was not updated after {retries} retries."
            ) from e

        if is_fetch_error(e):
            logging.warning(
                f"Updating user {user.id} failed due to a fetch error. "
                f"Retrying... ({retries + 1}/{MAX_RETRIES})"
            )
            return await update_user_good(user, retries + 1)
        logging.error(
            f"Updating user {user.id} failed due to an unexpected error. Retries: {retries}."
        )
        raise

    return user


# Cohesion vs Dependency


class StringUtils:
    def string_cleaner(self, string):
        return string.strip().replace("%20", " ")

    def format_email(self, email_service):
        result = email_service.message
        if email_service.options["trim"]:
            result = string_cleaner(string)
        return result


class EmailService:
    message = None
    options = {"trim": True}

    def __init__(self, message, options):
        self.message = message
        self.options = options

    def send_email(self):
        StringUtils.format_email(self)


email_service = EmailService(" test email ", {"trim": True})
email_service.send_email()
