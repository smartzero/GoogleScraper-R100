#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# pylint: disable=invalid-name,bad-builtin,missing-docstring
from subprocess import call
from os import listdir


def main():
    for fn in [x for x in listdir('.') if x[-1].isdigit()]:
        call(
            'uniq "{0}" > tmp.tmp.tmp && mv tmp.tmp.tmp "{0}"'.format(fn),
            shell=True)


main()
