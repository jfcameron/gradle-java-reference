#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import argparse

parser = argparse.ArgumentParser("makes a new java class file at the given location")
parser.add_argument('-projectname',     required=True, type=str, help='name of project')
parser.add_argument('-packagename',     required=True, type=str, help='name of package')
parser.add_argument('-copyrightholder', required=True, type=str, help='name of copyrightholder')
parser.add_argument('-classname',       required=True, type=str, help='name of class')
parser.add_argument('-outputdir',       required=True, type=str, help='directory where java file should be made')
args = parser.parse_args()

_variables =\
{
    "year": str(datetime.date.today().year),
    "year-month-day": str(datetime.date.today())
}

_template =\
"""
// © ${YEAR} ${COPYRIGHTHOLDER} - All Rights Reserved
// Project: ${PROJECTNAME}
// Created on ${YEAR-MONTH-DAY}.
package ${PACKAGENAME};

/**
 * No description provided for ${CLASSNAME}
 */
public class ${CLASSNAME}
{
    
}
""".split("\n",2)[2]

_output = _template

for key, value in _variables.items():
    _output = _output.replace("${" + key.upper() + "}", value)

for arg in vars(args):
    _output = _output.replace("${" + arg.upper() + "}", getattr(args, arg))

text_file = open(args.outputdir+"/"+args.classname+".java", "w")
text_file.write(_output)
text_file.close()
