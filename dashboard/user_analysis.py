

def parse_user_input(input):
    if input[:4] == "http":
        input = input.split('/')[-1]
    return input
