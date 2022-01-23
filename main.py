import random

g_scale = ['1', '2', '3', '4', '5', '6', '7', '8']

grammar = {
    "<start>": ["<pattern><pattern><expr>"],
    "<expr>": ["<pattern><expr>"],
    "<pattern>" : ["<quarter><eighth><eighth>", "<eighth><pause><quarter>", "<quarter><quarter>", "<eighth><eighth><eighth><eighth>"],
    "<quarter>" : ["<quarter>"],
    "<eighth>" : ["<eighth>"],
    "<pause>": ["*"]

}


def expand_expr(expr):
    expr_list = []
    term = ""
    flag = False
    for char in expr:
        if char == '<':
            flag = True
        if flag:
            term += char
        if char == '>':
            expr_list.append(term)
            term = ""
            flag = False
    return expr_list


def grammar_fuzzer(measures):
    term = "<start>"
    max_beats = measures * 4
    beats = 0
    i = 0
    output_list = []
    while (beats < max_beats):
        remaining_symbols = expand_expr(term)
        symbol_to_expand = random.choice(remaining_symbols)
        print(symbol_to_expand)
        expansions = grammar[symbol_to_expand]
        expansion = random.choice(expansions)
        new_term = term.replace(symbol_to_expand, expansion, 1)
        print(new_term)
        if expansion == "<quarter>":
            scale_note = random.choice(g_scale)
            new_term = new_term.replace(expansion, scale_note + '', 1)
            output_list.append(scale_note)
            beats += 1
        if expansion == "<eighth>":
            scale_note = random.choice(g_scale)
            new_term = new_term.replace(expansion, scale_note + '/', 1)
            output_list.append(scale_note + '/')
            beats += 0.5
        if expansion == "*":
            output_list.append(expansion)
            beats += 0.5
        term = new_term
        i += 1
    return output_list


def get_user_input():
    print('Standard notes are written as capitals. Sharps have a # appended. Flats are in lowercase. Ex: A, D#, e')
    print('The app assumes 4/4 time. Beatss are separated by commas. A note being held for a beat uses a -. Ex: F--')
    print('Eighth notes are written together in a beat and separated with a /. Ex: A/B, ')
    print('Eighth note rests are written as *.')
    measures = input("Enter how many measures you would like to generate: ")
    return measures


def display_output(output_list):
    counter = 0
    output_str = ""
    for symbol in output_list:
        output_str += symbol
        if '/' in symbol or '*' in symbol:
            counter += 0.5
        else:
            counter += 1
        if counter >= 4:
            output_str += ' '
            counter = 0
    print(output_str)


def main():
    melody = grammar_fuzzer(3)
    display_output(melody)


if __name__ == "__main__":
    main()
