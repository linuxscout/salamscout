#************************************************************************
# $Id: scoutgame_main.py,v 0.7 2009/06/02 01:10:00 Taha Zerrouki $
#
# ------------
# Description:
# ------------
#  Copyright (c) 2009, Arabtechies, Arabeyes Taha Zerrouki
#
#  This file is used by the web interface to execute verb conjugation
#
# -----------------
# Revision Details:    (Updated by Revision Control System)
# -----------------
#  $Date: 2009/06/02 01:10:00 $
#  $Author: Taha Zerrouki $
#  $Revision: 0.7 $
#  $Source: arabtechies.sourceforge.net
#
#***********************************************************************/
from pysqlite2 import dbapi2 as sqlite
import sys,re,string
import sys, os
from ar_ctype import *
from morse import *
from semaphore import *
from codepoint import *

FILE_DB=u"data/officelexique.db"

def convert_text(text,language,lexique="default",explicated=False):
##    print lexique;
    if lexique=="morse":
        coded= morse(text,explicated);
    elif lexique=="codepoint":
        coded= codepoint(text,explicated);
    elif lexique=="semaphore":
        coded= semaphore(text,explicated);
    else:
        coded= codepoint(text,explicated);
##    print coded;
    return coded;



format_table={
"TEXT":
    {
    "table":"",
    "/table":"",
    "tr":"",
    "/tr":"\n",
    "td":"",
    "/td":"\t",
    },
"CSV":
    {
    "table":"",
    "/table":"",
    "tr":"",
    "/tr":"\n",
    "td":"",
    "/td":"\t",
    },
"HTML":
    {
    "table":"<html> <body dir='rtl'><table>",
    "/table":"</table></body></html>",
    "tr":"<tr>",
    "/tr":"</tr>",
    "td":"<td>",
    "/td":"</td>",
    },
"XML":
    {

    "table":"<?xml encoding='utf-8'><lexique>",
    "/table":"</lexique></xml>",
    "tr":"<term>",
    "/tr":"</term>",
    "td":"<language>",
    "/td":"</language>",
    },
}
def display_format(table,formatting):
    if not format_table.has_key(formatting):
        frmatting="TEXT";
    start_tag=format_table[formatting]["table"];
    end_tag=format_table[formatting]["/table"];
    start_line_tag=format_table[formatting]["tr"];
    end_line_tag=format_table[formatting]["/tr"];
    start_data_tag=format_table[formatting]["td"];
    end_data_tag=format_table[formatting]["/td"];
    text=""
    text+=start_tag;
    for i in range(len(table)):
        text+=start_line_tag;
        for v in table[i].values():
            text+=start_data_tag;
            text+=v;
            text+=end_data_tag;
        text+=end_line_tag;
    text+=end_tag;
    return text;
##table={
##0:{0:'A',1:'B',2:'C'},
##1:{0:'A',1:'B',2:'C'},
##2:{0:'A',1:'B',2:'C'},
##}
##print display_format(table,"TEXT");
##print "-------------------------"
##print display_format(table,"XML");
##print "-------------------------"
##print display_format(table,"HTML");
##print "-------------------------"
##print display_format(table,"CSV");
##

