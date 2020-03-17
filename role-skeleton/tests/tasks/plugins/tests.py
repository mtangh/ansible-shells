# plugins/tests.py

# Make coding more python3-ish
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import util.tests as t
import compat.func as f

class TestModule(object):

  def tests(self):
    return {
      # tests utilities
      'tt_valid': t.task_valid,
      'tt_eq_setup': t.task_eq_setup,
      'tt_eq_teardown': t.task_eq_teardown,
      'tt_has_yml_files': t.has_yml_files,
      'tt_has_files_dir': t.has_files_dir,
      # file testing
      'is_dir': f.isdir,
      'directory': f.isdir,
      'is_file': f.isfile,
      'file': f.isfile,
      'is_link': f.islink,
      'link': f.islink,
      'exists': f.exists,
      'link_exists': f.lexists,
      # path testing
      'is_abs': f.isabs,
      'abs': f.isabs,
      'is_same_file': f.samefile,
      'same_file': f.samefile,
      'is_mount': f.ismount,
      'mount': f.ismount,
      # regexp
      'match': f.match,
      'search': f.search,
    }

