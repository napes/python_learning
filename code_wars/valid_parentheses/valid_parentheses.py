def valid_parentheses(string):
    open = 0
    close = 0

    for x in string:
        if close > open:  ## this outputs to False if there are ever opens before close
            return False
        elif x == '(':
            open += 1
        elif x == ')':
            close += 1
        elif close > open:
            return False
        # print(open, close)

    if open != close: ## final validation of symmetry open == close
        return False
    else:
        return True