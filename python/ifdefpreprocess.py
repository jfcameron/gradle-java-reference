#!/usr/bin/env python
# -*- coding: utf-8 -*-
_input =\
"""
// Project: GDK
// Created on 2017-09-27.
package com.grimhaus.gdk;

public class Platform
{
    public string getName()
    {
        string output =
        //#define Win32
            //"Windows"
        //#elif OSX
            //"Mac"
        //#elif Linux
            //"Linux"
        //#elif Android
            //"Android"
        //#else
            //"Unknown"
        //#end
        ;
    }
}
""".split("\n",2)[2].split('\n')

_output = _input

for line in _output:
    print (line)

_output = "\n".join(_output)

"""
text_file = open("ifdeftestoutput.java", "w")
text_file.write(_output)
text_file.close()
"""

print("\n========================================\n")

print(_output)
