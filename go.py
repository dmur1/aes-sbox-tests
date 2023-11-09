import sys
from PIL import Image

def multiply_in_gf2(a, b, mod):
    result = 0
    while b:
        if b & 1:
            result ^= a
        a <<= 1
        if a & 0x100:
            a ^= mod
        b >>= 1
    return result

def aes_mul(a, b, mod):
    return multiply_in_gf2(a, b, mod)

def make_sbox(mod):
    sbox = [0]
    for i in range(0x100):
        for j in range(0x100):
            if aes_mul(i, j, mod) == 1:
                sbox.append(j)
                break
    return sbox

def print_sbox(sbox, mod):
    print(hex(mod))
    for i in range(16):
        for j in range(16):
            sys.stdout.write(f"{sbox[(i * 16) + j]:02x} ")
        sys.stdout.write("\n")

def visualize_sbox(sbox, mod):
    image = Image.new("RGB", (128, 128), "white")
    pixels = image.load()

    for i in range(128):
        for j in range(128):
            value = sbox[((i//8) * 16) + (j//8)]
            intensity = int((value / 255) * 255)
            pixels[j, i] = (intensity, intensity, intensity)

    image.show(str(mod))

default_aes_polynomial = 0x11B
sbox_11b = make_sbox(default_aes_polynomial)
print_sbox(sbox_11b, default_aes_polynomial)
visualize_sbox(sbox_11b, default_aes_polynomial)

alternative_aes_polynomial = 0x11D
sbox_11d = make_sbox(alternative_aes_polynomial)
print_sbox(sbox_11d, alternative_aes_polynomial)
visualize_sbox(sbox_11d, alternative_aes_polynomial)

