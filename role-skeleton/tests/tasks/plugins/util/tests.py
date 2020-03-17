# Make coding more python3-ish
from __future__ import absolute_import

import sys
import os
import re


SCRIPT_DIR_PATH = os.path.dirname(__file__)

TESTS_ROOT_PATH = os.path.abspath('%s/../../..' % SCRIPT_DIR_PATH)

LOOKUP_DIR_NAME = 'testcases.d'


def task_eq_setup(input):
  try:
    return input is not None and \
      re.match('^setup$', str(input).strip(), re.I)
  except:
    return False


def task_eq_teardown(input):
  try:
    return input is not None and \
      re.match('^teardown$', str(input).strip(), re.I)
  except:
    return False


def task_valid(input):
  try:
    return input is not None and \
      (task_eq_setup(input) or task_eq_teardown(input))
  except:
    return False


def lookup_yml_files(casename, taskname, typename):
  try:

    if casename is not None:
      casename = str(casename).strip()
    else:
      return []

    if taskname is not None:
      taskname = (str(taskname).strip()).lower()
    else:
      return []

    if typename is not None:
      typename = (str(typename).strip()).lower()
    else:
      return []

    lookup_files = []

    lookup_dir_path = '%s/%s' % (TESTS_ROOT_PATH, LOOKUP_DIR_NAME)

    lookup_dir_list = [('%s/all/%s' % (lookup_dir_path, typename)), (
      '%s/all/%s/%s' % (lookup_dir_path, typename, taskname)),
                       ('%s/%s/%s' % (lookup_dir_path, casename, typename)), (
                         '%s/%s/%s/%s' % (lookup_dir_path, casename, typename,
                                          taskname)), None]

    for lookup_dir in lookup_dir_list:
      if lookup_dir is None:
        break
      list_dir_items = (
        os.listdir(lookup_dir)
        if os.path.isdir(lookup_dir) else [])
      for dir_item in sorted(list_dir_items):
        if dir_item is None:
          continue
        if not os.path.isfile(dir_item):
          continue
        if not re.search('\.yml$', str(dir_item), re.I):
          continue
        lookup_files += [dir_item]

    return lookup_files

  except:
    return []


def has_yml_files(casename, taskname, typename):
  return len(lookup_yml_files(casename, taskname, typename))


def lookup_files_dir(casename, taskname):
  try:

    if casename is not None:
      casename = str(casename).strip()
    else:
      return []

    if taskname is not None:
      taskname = (str(taskname).strip()).lower()
    else:
      return []

    lookup_dirs = []

    lookup_dir_path = '%s/%s' % (TESTS_ROOT_PATH, LOOKUP_DIR_NAME)

    lookup_dir_list = [('%s/all/files/%s' % (lookup_dir_path, typename)), (
      '%s/%s/files/%s' % (lookup_dir_path, casename, taskname)), None]

    for lookup_dir in lookup_dir_list:
      if lookup_dir is None:
        break
      list_dir_items = (
        os.listdir(lookup_dir)
        if os.path.isdir(lookup_dir) else [])
      for dir_item in sorted(list_dir_items):
        if dir_item is None:
          continue
        if os.path.isdir(dir_item):
          continue
        lookup_dirs += [dir_item]

    return lookup_dirs

  except:
    return []


def has_files_dir(casename, taskname, typename):
  return len(lookup_files_dir(casename, taskname, typename))

