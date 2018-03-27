import re, numpy as np, math

def encode(text):
    text = re.sub(r'\W+', '', text).lower()
    square_size = int(math.ceil(math.sqrt(len(text))))
    text = str.ljust(text, (square_size-1) * square_size)
    np_text = np.array(list(text))
    np_grid = np_text.reshape(-1,square_size)
    np_transposed = np_grid.transpose()

    return_string = ''
    for row in np_transposed:
        return_string += row.ravel().tostring() + ' '

    return re.sub('  $', ' ', return_string)

