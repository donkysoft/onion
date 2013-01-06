#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

def set_adjust_path(text, filedir=[]):
    level = len(filedir)
    if level <= 0:
        # no change
        return text
    results = re.finditer(r"(src|href)\s*=\s*\"(.*?)\"", text, re.IGNORECASE)
    if not results:
        # no match
        return text
    for m in results:
        uri = m.group(2)
        # sharp
        if uri[0] == '#':
            continue
        # slash top
        if uri[0] == '/':
            continue
        # include '://'
        if uri.find('://') != -1:
            continue
        # uri
        uri = '/'.join(filedir) + '/' + uri
        # replace
        text = text.replace(m.group(0), m.group(1) + '="' + uri + '"')
    return text

def set_adjust_tpl(text, filedir=[]):
    level = len(filedir)
    if level <= 0:
        # no change
        return text
    results = re.finditer(r"(src|href)\s*=\s*\"(.*?)\"", text, re.IGNORECASE)
    if not results:
        # no match
        return text
    for m in results:
        uri = m.group(2)
        # sharp
        if uri[0] == '#':
            continue
        # slash top
        if uri[0] == '/':
            continue
        # include '://'
        if uri.find('://') != -1:
            continue
        # uri
        uri = '../' * level + uri
        # replace
        text = text.replace(m.group(0), m.group(1) + '="' + uri + '"')
    return text

