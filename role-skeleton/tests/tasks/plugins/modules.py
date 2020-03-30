# plugins/modules.py

# Make coding more python3-ish
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


import os
import re


SCRIPT_DIR_PATH = os.path.dirname(__file__)

TESTS_ROOT_PATH = os.path.abspath('%s/../..' % SCRIPT_DIR_PATH)

LOOKUP_DIR_NAME = 'testcases.d'


def util_task_eq_setup(input):
  try:
    return input is not None and \
      re.match('^setup$', str(input).strip(), re.I)
  except:
    return False


def util_task_eq_teardown(input):
  try:
    return input is not None and \
      re.match('^teardown$', str(input).strip(), re.I)
  except:
    return False


def util_task_valid(input):
  try:
    return input is not None and \
      (util_task_eq_setup(input) or util_task_eq_teardown(input))
  except:
    return False


def util_lookup_yml_files(casename, taskname, typename):
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


def util_has_yml_files(casename, taskname, typename):
  return len(util_lookup_yml_files(casename, taskname, typename))


def util_lookup_files_dir(casename, taskname):
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

    lookup_dir_list = [('%s/all/files/%s' % (lookup_dir_path, taskname)), (
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


def util_has_files_dir(casename, taskname, typename):
  return len(util_lookup_files_dir(casename, taskname, typename))


def compat_exists(path):
  try:
    return path is not None and os.path.exists(path)
  except:
    return False


def compat_lexists(path):
  try:
    return path is not None and os.path.lexists(path)
  except:
    return False


def compat_isdir(path):
  try:
    return path is not None and os.path.isdir(path)
  except:
    return False


def compat_isfile(path):
  try:
    return path is not None and os.path.isfile(path)
  except:
    return False


def compat_islink(path):
  try:
    return path is not None and os.path.islink(path)
  except:
    return False


def compat_isabs(path):
  try:
    return path is not None and os.path.isabs(path)
  except:
    return False


def compat_ismount(path):
  try:
    return path is not None and os.path.ismount(path)
  except:
    return False


def compat_samefile(path1, path2):
  try:
    return \
      path1 is not None and \
      path2 is not None and \
      os.path.samefile(path1, path2)
  except:
    return False


def compat_match(input, pattern='', ignorecase=False, multiline=False):
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


def compat_search(input, pattern='', ignorecase=False, multiline=False):
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


class FilterModule(object):

  def filters(self):
    return {
      # tests utilities
      'tt_valid': util_task_valid,
      'tt_eq_setup': util_task_eq_setup,
      'tt_eq_teardown': util_task_eq_teardown,
      'tt_lookup_yml_files': util_lookup_yml_files,
      'tt_has_yml_files': util_has_yml_files,
      'tt_lookup_files_dir': util_lookup_files_dir,
      'tt_has_files_dir': util_has_files_dir,
      # file testing
      'is_dir': compat_isdir,
      'is_file': compat_isfile,
      'is_link': compat_islink,
      'exists': compat_exists,
      'link_exists': compat_lexists,
      # path testing
      'is_abs': compat_isabs,
      'is_same_file': compat_samefile,
      'is_mount': compat_ismount,
      # regexp
      'match': compat_match,
      'search': compat_search,
    }


class TestModule(object):

  def tests(self):
    return {
      # tests utilities
      'tt_valid': util_task_valid,
      'tt_eq_setup': util_task_eq_setup,
      'tt_eq_teardown': util_task_eq_teardown,
      'tt_has_yml_files': util_has_yml_files,
      'tt_has_files_dir': util_has_files_dir,
      # file testing
      'is_dir': compat_isdir,
      'directory': compat_isdir,
      'is_file': compat_isfile,
      'file': compat_isfile,
      'is_link': compat_islink,
      'link': compat_islink,
      'exists': compat_exists,
      'link_exists': compat_lexists,
      # path testing
      'is_abs': compat_isabs,
      'abs': compat_isabs,
      'is_same_file': compat_samefile,
      'same_file': compat_samefile,
      'is_mount': compat_ismount,
      'mount': compat_ismount,
      # regexp
      'match': compat_match,
      'search': compat_search,
    }

