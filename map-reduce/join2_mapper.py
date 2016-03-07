#!/usr/bin/env python
# -*- coding: utf-8 -*-


# when value is a digit, the line format is <show_title, view_count>
# when value is a channel, the line format is <show_title, channel>

import sys

for line in sys.stdin:
    show_title, value = line.split(',')
    show_title = show_title.strip()
    value = value.strip()


    if value.isdigit() or value == 'ABC':
        print('{0}\t{1}'.format(show_title, value))
