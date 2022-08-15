from PIL import Image
import os
import sys


def read_duration():
    default_duration = 100
    if len(sys.argv) == 1:
        return default_duration

    try:
        return int(sys.argv[1])
    except ValueError:
        print('bad duration:', sys.argv[1], ', defaulting to', default_duration, 'ms')
        return default_duration


def read_images():
    result = []
    images_directory = "./data"

    if not os.path.exists(images_directory):
        return result

    for file in sorted(os.listdir(images_directory)):
        ext = os.path.splitext(file)[1]
        if ext.lower() != ".png":
            continue
        result.append(Image.open(os.path.join(images_directory, file)))
    return result


if __name__ == '__main__':
    duration = read_duration()
    print('reading images...')
    images = read_images()
    print('generating GIF...')
    images[0].save("result.gif", save_all=True, append_images=images[1:], duration=duration)
    print('done!')
