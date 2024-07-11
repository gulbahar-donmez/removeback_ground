from rembg import remove

input_path="fil2.jpg"
output="output.png"

with open(input_path,'rb') as i:
    with open(output,'wb') as o:
        input_file=i.read()
        output_file=remove(input_file)
        o.write(output_file)
