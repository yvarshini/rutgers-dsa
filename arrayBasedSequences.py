def paranthesisMatching(seq):
    left_list = ['[', '{', '(']
    right_list = [']', '}', ')']
    temp = ArrayStack()
    for bracket in seq:
        if bracket in left_list:
            temp.push(bracket)
        elif bracket in right_list:
            if temp.is_empty():
                return False
            if left_list.index(temp.pop()) != right_list.index(bracket):
                return False
    return temp.is_empty()

