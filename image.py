#!/usr/bin/python
#ecoding=utf-8

#图像处理
import Image;
im = Image.open("1.jpg");
print im.format,im.size,im.mode;
im.thumbnail((200, 100));
im.save('1mini.jpg', 'JPEG');
