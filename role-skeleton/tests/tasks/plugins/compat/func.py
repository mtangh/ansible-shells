#!/usr/bin/env python

from __future__ import absolute_import

from os.path import (
  isdir, isfile, isabs,
  exists, lexists, islink,
  samefile, ismount
  )

from re import (
  match, search
  )


def exists(path):
  try:
    return path is not None and exists(path)
  except:
    return False


def lexists(path):
  try:
    return path is not None and lexists(path)
  except:
    return False


def isdir(path):
  try:
    return path is not None and isdir(path)
  except:
    return False


def isfile(path):
  try:
    return path is not None and isfile(path)
  except:
    return False


def islink(path):
  try:
    return path is not None and islink(path)
  except:
    return False


def isabs(path):
  try:
    return path is not None and isabs(path)
  except:
    return False


def ismount(path):
  try:
    return path is not None and ismount(path)
  except:
    return False


def samefile(path1, path2):
  try:
    return \
      path1 is not None and \
      path2 is not None and \
      samefile(path1, path2)
  except:
    return False


def match(input, pattern='', ignorecase=False, multiline=False):
  try:
    re_flags = 0
    re_flags += re.I if (ignorecase) else 0
    re_flags += re.M if (multiline) else 0
    return \
        input is not None and \
        pattern is not None and \
        re.match(pattern, input, re_flags)
  except:
    return False


def search(input, pattern='', ignorecase=False, multiline=False):
  try:
    re_flags = 0
    re_flags += re.I if (ignorecase) else 0
    re_flags += re.M if (multiline) else 0
    return \
        input is not None and \
        pattern is not None and \
        re.search(pattern, input, re_flags)
  except:
    return False


