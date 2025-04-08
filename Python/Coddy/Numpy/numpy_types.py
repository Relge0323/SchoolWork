import numpy as np
def dtype_converter(bits, value):
    value += 1

    if bits == 8:
        return np.array(value, dtype=np.int8)
    elif bits == 16:
        return np.array(value, dtype=np.int16)
    elif bits == 32:
        return np.array(value, dtype=np.int32)
    elif bits == 64:
        return np.array(value, dtype=np.int64)
    else:
        print("invalid entry")
