# coding:utf8
# Author:Floyda

import os
import re

import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '.'))

KEYWORD_FILE_PATH = "./snippets_raw"
OUTPUT_DIR_PATH = "./odps_functions_snippets"
SUFFIX = "sql"

SNIPPET_TEMPLATE = """\
<snippet>
    <content><![CDATA[
%s
]]></content>
    <tabTrigger>%s</tabTrigger>
    <scope>source.%s</scope>
    <description>%s</description>
</snippet>\
"""


def get_snippet_tempate(trigger, content):
    return SNIPPET_TEMPLATE % (content, trigger, SUFFIX, trigger)


def get_word_list(path):
    rlist = set([])
    with open(path, 'r') as fp:
        for word in fp.readlines():
            rlist.add(re.sub('\n', '', word))
    return rlist


def generate_snippet(word):
    # word = re.sub(' ', '', word)
    trigger = word.split(';')[0]
    content = word.split(';')[1]
    file_name = trigger + '.sublime-snippet'
    path = os.path.join(OUTPUT_DIR_PATH, file_name)
    with open(path, 'w') as fp:
        fp.write(get_snippet_tempate(trigger, content))

    print("%s is OK ..." % file_name)


if __name__ == '__main__':
    try:
        os.mkdir(OUTPUT_DIR_PATH)
    except:
        pass

    for word in get_word_list(KEYWORD_FILE_PATH):
        generate_snippet(word)

    print("OK")
