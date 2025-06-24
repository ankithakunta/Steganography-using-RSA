from PIL import Image

def _int_to_bin(data):
    return ''.join(format(ord(char), '08b') for char in data)

def _bin_to_str(binary):
    chars = [binary[i:i+8] for i in range(0, len(binary), 8)]
    return ''.join(chr(int(b, 2)) for b in chars)

def encode_message(image_path, message, output_path):
    img = Image.open(image_path)
    binary_message = _int_to_bin(message) + '1111111111111110'  # EOF marker

    data = iter(img.getdata())
    new_pixels = []

    for i in range(0, len(binary_message), 3):
        pixels = list(next(data))
        for j in range(3):
            if i + j < len(binary_message):
                pixels[j] = (pixels[j] & ~1) | int(binary_message[i + j])
        new_pixels.append(tuple(pixels))

    img_copy = img.copy()
    img_copy.putdata(new_pixels + list(data))
    img_copy.save(output_path)
    return output_path

def decode_message(image_path):
    img = Image.open(image_path)
    binary = ''
    for pixel in img.getdata():
        for value in pixel[:3]:  # Use RGB values only
            binary += str(value & 1)

    eof = '1111111111111110'
    index = binary.find(eof)
    if index != -1:
        binary = binary[:index]
    return _bin_to_str(binary)

