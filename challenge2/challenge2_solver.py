__author__ = 'Nicholas McKinney'

data = [
    0XA8, 0X9A, 0X90, 0XB3, 0XB6,
    0XBC, 0XB4, 0XAB, 0X9D, 0XAE,
    0XF9, 0XB8, 0X9D, 0XB8, 0XAF,
    0XBA, 0XA5, 0XA5, 0XBA, 0X9A,
    0XBC, 0XB0, 0XA7, 0XC0, 0X8A,
    0XAA, 0XAE, 0XAF, 0XBA, 0XA4,
    0XEC, 0XAA, 0XAE, 0XEB, 0XAD, 0xAA, 0XAF, 0xAA
]

possible_characters = [
    45,46,48, 95, 64
] + [i for i in range(49,91)] + [i for i in range(97,123)]

def challenge_iter(d, bx):
    dx = bx & 0x03
    cx = dx
    cl = cx & 0x00ff
    ax = 0x1c7
    ax = (ax & 0x0f00) | d
    ax = ax ^ 0xc7
    ah = 0xff00 & ax
    ah = ah << cl
    al = ax & 0x00ff
    ah = ah >> 8
    al += ah + 1
    ax = al
    ax = ax & 0x00ff
    bx += ax
    return bx, ax


def main():
    bx = 0
    dx = 0
    result = ''
    cx = len(data)
    bx, ax = challenge_iter(97, bx)
    bx, ax = challenge_iter(ord('_'), bx)
    bx = 0
    ax = 0
    for i in range(0, len(data)):
        for c in possible_characters:
            new_bx, result_add = challenge_iter(c, bx)
            if data[i] == result_add:
                bx = new_bx
                result += chr(c)
                print result
                break
    print result

if __name__ == '__main__':
    main()