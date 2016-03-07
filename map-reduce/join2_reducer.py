#!/usr/bin/env python
# -*- coding: utf-8 -*-

# When value is a digit, the line format is <show_title, view_count>
# When value is a channel, the line format is <show_title, channel>

import sys

previous_show = ""
channel_found = False
current_total = 0
line_count = 0

for line in sys.stdin:
    line_count += 1
    line = line.strip()
    current_show, value = line.split('\t')

    if current_show != previous_show:
        if line_count > 1:
            if channel_found:
                print('{0} {1}'.format(previous_show, current_total))
            channel_found = False
            current_total = 0
        previous_show = current_show

    if value.isdigit():
        current_total += int(value)

    if value == "ABC":
        channel_found = True

if channel_found:
    print('{0} {1}'.format(previous_show, current_total))
