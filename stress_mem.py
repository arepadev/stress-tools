#!/usr/bin/python
# -*- coding: utf-8 -*-

objects = []
while 1:
    fd = open('test.jpg', 'rb')
    image = fd.read()
    objects.append(image)
    print len(objects)
