from PIL import Image, ImageDraw, ImageFont
import pandas as pd

in_form=input("Enter name excel file:")

name=input("Enter field name in excel:")

pic=input("Enter certificate (.jpg) name:")

x_axis=input("Enter X-Axis Co-ordinate:")
y_axis=input("Enter Y-Axis Co-ordinate:")

font_name=input("Enter font name:")
font_size=input("Enter font size:")

form = pd.read_excel(in_form)
name_list = form[name].to_list()

color=[]
print("Enter color(R,G,B):")
for i in range(3):
    p=int(input())
    color.append(p)


text_color = (color[0],color[1],color[2])

for i in name_list:
    p=i.split()
    print(p)
    if len(p)>=3:
        im = Image.open(pic)#input should be a jpg file
        d = ImageDraw.Draw(im)
        k=str(str(p[0])+" "+str(p[1]))
        location = (x_axis, y_axis)
        location2 =(x_axis, y_axis+100)
        k=str(str(p[0])+" "+str(p[1]))
        final_name=str(p[2])
        font = ImageFont.truetype(font_name, font_size)
        d.text(location, k, fill=text_color,font=font)
        d.text(location2, final_name, fill=text_color,font=font)
        im.save("certificate_"+i+".pdf")

    else:
        im = Image.open("cert.jpg")
        d = ImageDraw.Draw(im)
        location = (x_axis,y_axis)
        
        font = ImageFont.truetype(font_name, font_size)
        d.text(location, i, fill=text_color,font=font)
        im.save("certificate_"+i+".pdf")