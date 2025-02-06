"""PyCrypted Images"""

import os

def Encode(* , path, name):
    path = path.replace("/", "\\")

    if os.path.exists(path):
        if path[-1] == "\\":
            pycrypt_image = path + name + ".jpg"
        else:
            pycrypt_image = path + "\\" + name + ".jpg"
        return pycrypt_image
    else:
        raise FileNotFoundError(f"Error: The location '{path}' is not valid.")


def Save(*, text, pycrypt_image):
    with open(pycrypt_image, "w") as file:
        file.write(text)

def EncodeFile(*, text, path, name):
    path = path.replace("/", "\\")

    if os.path.exists(path):
        if path[-1] == "\\":
            pycrypt_image = path + name + ".jpg"
        else:
            pycrypt_image = path + "\\" + name + ".jpg"
        with open(pycrypt_image, "w") as file:
            file.write(text)
    else:
        raise FileNotFoundError(f"Error: The location '{path}' is not valid.")
