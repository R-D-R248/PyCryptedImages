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
    
def Decode(*, path, name):
    path = path.replace("/", "\\")

    if os.path.exists(path):
        if path[-1] == "\\":
            Open_Path = path + name + ".jpg"
        else:
            Open_Path = path + "\\" + name + ".jpg"
        
        try:
            with open(Open_Path, 'r') as file:
                content = file.read()
                print(content)
        except:
            raise FileNotFoundError(f"Error: The File '{Open_Path}' is not valid.")
    else:
        raise FileNotFoundError(f"Error: The location '{path}' is not valid.")
