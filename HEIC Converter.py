from PIL import Image
import pillow_heif
import os
import re

base_dir = os.listdir('./heic_files/')

output_dir = os.path.join('./png_files/')

for i in os.listdir(base_dir):
    
    name = i
    rule = "(?<=\.)[^.]*$"
    result = re.split(rule,name)


    heif_file = pillow_heif.read_heif("./heic_files/"+i)
    image = Image.frombytes(
        heif_file.mode,
        heif_file.size,
        heif_file.data,
        "raw",
    )

    print(i+" Converted to PNG format") 



    image.save(output_dir+result[0]+"png", format="png")
