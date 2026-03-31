from PIL import Image
import csv
import json
import os

def jpg_to_png(input_path,output_path):
    img=Image.open(input_path)
    img=img.convert("RGB")
    img.save(output_path,"PNG")

def csv_to_json(input_path,output_path):
    data=[]
    with open(input_path,"r") as csv_file:
        reader=csv.DictReader(csv_file)
        for row in reader:
            data.append(row)
    with open(output_path,"w") as json_file:
        json.dump(data,json_file,indent=4)

def convert_file(input_path):
    filename=os.path.basename(input_path)
    if filename.endswith(".jpg"):
        output_path=input_path.replace(".jpg",".png")
        jpg_to_png(input_path,output_path)
        return output_path
    if filename.endswith(".csv"):
        output_path=input_path.replace(".csv",".json")
        csv_to_json(input_path,output_path)
        return output_path
    return None