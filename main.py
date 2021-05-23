import math

def compute_probability(symbol, text_list, n):
    probability = text_list.count(symbol) / n
    return round(probability, 3)


def output_probabilities(text):
    symbols = list(set(text))
    n = len(text)
    text_list = list(text)
    probabilities = {}
    for symbol in symbols:

        probabilities[symbol] = compute_probability(symbol, text_list, n)
        if symbol == ' ':
            probabilities['space'] = probabilities[' ']
            del probabilities[' ']
        if symbol == '\n':
            probabilities['newline'] = probabilities['\n']
            del probabilities['\n']
        if symbol == '\t':
            probabilities['tab'] = probabilities['\t']
            del probabilities['\t']
        if symbol == "','":
            probabilities['","'] = probabilities[',']
            del probabilities[',']

    return dict(sorted(probabilities.items(), key=lambda item: item[1], reverse=True))

def compute_entropy(probabilities):
    print('Probabilities from assignment 2:')
    entropy = 0
    for key in probabilities.keys():
        print(f'{key} - {probabilities[key]}')
        entropy += -probabilities[key] * math.log(probabilities[key], 2)
    print(f'\nH = {round(entropy, 3)} bits/symbol')
    return entropy



def main(filename):
    with open(filename, 'r') as file:
        data = file.read()
        entropy = compute_entropy(output_probabilities(data))


if __name__ == "__main__":
    filename = "Text.txt"
    main(filename)