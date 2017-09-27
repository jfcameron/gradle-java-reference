#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import argparse

parser = argparse.ArgumentParser("makes a new project at the given location")
parser.add_argument('-projectname',     required=True, type=str, help='name of project')
parser.add_argument('-packagename',     required=True, type=str, help='name of package')
parser.add_argument('-copyrightholder', required=True, type=str, help='name of copyrightholder')
parser.add_argument('-classname',       required=True, type=str, help='name of class')
parser.add_argument('-outputdir',       required=True, type=str, help='directory where java file should be made')
args = parser.parse_args()

_template = \
"""
// © ${YEAR} ${COPYRIGHTHOLDER} - All Rights Reserved
// Project: ${PROJECTNAME}
// Created on ${YMD}.
package ${PACKAGENAME};

/**
 * No description provided for ${CLASSNAME}
 */
public class ${CLASSNAME}
{

}

"""

_output = _template\
.replace("${YEAR}",        str(datetime.date.today().year))\
.replace("${YMD}",         str(datetime.date.today()))\

for arg in vars(args):
    print(arg + ": " + getattr(args, arg))
    _output = _output.replace("${" + arg.upper() + "}", getattr(args, arg))

print (_output)

text_file = open(args.outputdir+"/"+args.classname+".java", "w")
text_file.write(_output)
text_file.close()
