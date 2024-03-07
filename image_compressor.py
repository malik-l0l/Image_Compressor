import os

import PIL
from PIL import Image
from tkinter.filedialog import askopenfilenames

# ----GLOBALS--------------------------------------------------------
FILE_NAME_AFTER_COMPRESSION = 'compressed_image.png'
SAVE_FILE_IN = f"{os.path.abspath(f'{FILE_NAME_AFTER_COMPRESSION}')}"


# ----END GLOBALS----------------------------------------------------

# ===========MAIN=========================================
def main():
    try:
        fl = askopenfilenames()  # opens window to select image file

        img = Image.open(fl[0])
        img.save(SAVE_FILE_IN,
                 optimize=True,
                 quality=30)  # quality is reduced here

    except (KeyError, ValueError):
        print('please specify the image extension!')
    except (IndexError, PIL.UnidentifiedImageError):
        print("You didn't choose a image file!")


# ===========END MAIN=====================================


if __name__ == '__main__':
    main()
