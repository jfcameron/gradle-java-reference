#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import argparse

_Help =\
"makes a new java class file at the given location"

# ==================
# Templates
# ==================
_template =\
"""
// © ${YEAR} ${COPYRIGHTHOLDER} - All Rights Reserved
// Project: ${PROJECTNAME}
// Created on ${YEAR-MONTH-DAY}.
package ${PACKAGENAME};

/**
 * No description provided for ${CLASSNAME}
 */
public final abstract class ${CLASSNAME} 
{

}
""".split("\n",2)[2]

# ==================
# Symbols
# ==================
_args =\
[
    ["projectname",     "name of project"],
    ["packagename",     "name of package"],
    ["classname",       "name of class"],
    ["copyrightholder", "name of copyrightholder"]
]

_variables =\
{
    "year":           str(datetime.date.today().year),
    "year-month-day": str(datetime.date.today())
}

# ==============
# Program
# ==============
parser = argparse.ArgumentParser(_Help)
_args.append(["outputdir", "directory where the class file should be made"])

for arg in _args:
    parser.add_argument(str("-" + arg[0]), required=True, type=str, help=str(arg[1]))

args = parser.parse_args()

_output = _template

for key, value in _variables.items():
    _output = _output.replace("${" + key.upper() + "}", value)

for arg in vars(args):
    _output = _output.replace("${" + arg.upper() + "}", getattr(args, arg))

text_file = open(args.outputdir+"/"+args.classname+".java", "w")
text_file.write(_output)
text_file.close()
