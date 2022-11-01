import random

g_scale = ['1', '2', '3', '4', '5', '6', '7', '8']

jumps = {
    '1': ['3', '5', '7'],
    '2': ['1', '4', '5'],
    '3': ['1', '4', '6'],
    '4': ['2', '6', '8'],
    '5': ['2', '3', '7'],
    '6': ['1', '3', '8'],
    '7': ['3', '5', '8'],
    '8': ['4', '6', '7'],
    '*': ['1', '2', '3', '4', '5', '6', '7', '8'],
}

grammar = {
    '<start>': [['<pattern>', '<pattern>', '<expr>']],
    '<expr>': [['<pattern>', '<expr>']],
    # '<pattern>': [['<quarter>', '<quarter>']],
    '<pattern>': [['<quarter>', '<eighth>', '<eighth>'], ['<eighth>', '<pause>', '<quarter>'], ['<quarter>', '<quarter>'], ['<eighth>', '<eighth>', '<eighth>', '<eighth>']],
    '<quarter>': [['<quarter>']],
    '<eighth>': [['<eighth>']],
    '<pause>': [['<pause>']]
}


def expand_expr(expr):
    expr_list = []
    for elem in expr:
        if '<' in elem:
            expr_list.append(elem)
    return_list = []
    for elem in expr_list:
        if elem not in ['<quarter>', '<eighth>', '<pause>']:
            return_list.append(elem)
    return expr_list


def count_beats(expr):
    beats = 0
    for elem in expr:
        if elem == '<quarter>':
            beats += 1
        if elem == '<eighth>':
            beats += 0.5
        if elem == '<pause>':
            beats += 0.5
    return beats


def grammar_fuzzer(measures):
    term = ['<start>']
    max_beats = measures * 4
    beats = 0
    output_list = []
    while (beats < max_beats):
        remaining_symbols = expand_expr(term)
        symbol_to_expand = random.choice(remaining_symbols)
        expansions = grammar[symbol_to_expand]
        expansion = random.choice(expansions)
        symbol_to_expand_index = term.index(symbol_to_expand)
        term.remove(symbol_to_expand)
        term[symbol_to_expand_index:symbol_to_expand_index] = expansion
        beats = count_beats(term)
    print(term)
    return term


def get_user_input():
    print('Standard notes are written as capitals. Sharps have a # appended. Flats are in lowercase. Ex: A, D#, e')
    print('The app assumes 4/4 time. Beatss are separated by commas. A note being held for a beat uses a -. Ex: F--')
    print('Eighth notes are written together in a beat and separated with a /. Ex: A/B, ')
    print('Eighth note rests are written as *.')
    measures = input('Enter how many measures you would like to generate: ')
    return measures


def clean_fuzzer_output(expr):
    try:
        i = expr.index('<pattern>')
        return expr[:i]
    except ValueError:
        return expr[:-1]


def fill_terminal_symbols(expr):
    output_expr = []
    last_note = random.choice(g_scale)
    for symbol in expr:
        if symbol == '<quarter>':
            note = random.choice(jumps[last_note])
            output_expr.append(note)
            last_note = note
        if symbol == '<eighth>':
            note = random.choice(jumps[last_note])
            output_expr.append(note + '/')
            last_note = note
        if symbol == '<pause>':
            output_expr.append('*')
    return output_expr


def display_output(output_list):
    counter = 0
    output_str = ''
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
    measures = get_user_input()
    melody = grammar_fuzzer(int(measures))
    melody = fill_terminal_symbols(clean_fuzzer_output(melody))
    display_output(melody)


if __name__ == '__main__':
    main()
