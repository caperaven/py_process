import tokenize
from io import BytesIO
from enum import Enum

TYPE = 0
VALUE = 1
IGNORED_TOKENS = ["}", "{", "$", "utf-8"]

OPERATORS = {
    "eq": " == ",
    "ne": " != ",
    "gt": " > ",
    "ge": " >= ",
    "lt": " < ",
    "le": " <= ",
    "and": " and ",
    "or": " or ",
    "not": " not "
}

PREFIXES = {
    "c": "context.",
    "i": "item.",
    "d": "process.data.",
    "p": "process.parameters."
}


class SanitizeTypes(Enum):
    CONDITION = 0
    SWITCH = 1
    MATCH = 2


def sanitize(expr, san_type=SanitizeTypes.CONDITION):
    tokens = tokenize.tokenize(BytesIO(expr.encode('utf-8')).readline)
    tokens_list = list(tokens)

    if san_type == SanitizeTypes.CONDITION:
        return f"return {tokens_to_condition(tokens_list)}"

    return expr


def tokens_to_condition(tokens):
    expr = []
    prev_token = None
    next_token = None

    count = len(tokens)
    for i in range(0, count):
        # get current token
        current_token = tokens[i]

        # get previous token if exists
        if i > 0:
            prev_token = tokens[i - 1]

        # get next token if exists
        if i < count - 1:
            next_token = tokens[i + 1]

        value = current_token[VALUE]

        # ignore tokens that are not relevant
        if value in IGNORED_TOKENS:
            prev_token = current_token
            continue

        # if value is an operator, append the corresponding python operator
        if value in OPERATORS:
            expr.append(OPERATORS[value])
            prev_token = current_token
            continue

        # the current token presents a prefix for either
        # 1. context - $c{...}
        # 2. item - $i{...}
        # 3. data - $d{...}
        # 4. parameters - $p{...}
        if (prev_token and prev_token[VALUE] == "$") and (next_token and next_token[VALUE] == "{"):
            prefix = PREFIXES.get(value, None)
            if prefix:
                expr.append(prefix)

            continue

        prev_token = current_token
        expr.append(value)

    return "".join(expr)
