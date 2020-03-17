#!/bin/bash
THIS="${BASH_SOURCE##*/}"
CDIR=$([ -n "${BASH_SOURCE%/*}" ] && cd "${BASH_SOURCE%/*}" &>/dev/null; pwd)

# Run tests
echo "[${tests_name}] ansible-create-role" && {

  tests_work_dir="${HOME}/${tests_name}"

  rm -rf "${tests_work_dir}" || :
  mkdir -p "${tests_work_dir}" || :

  ( bash -n ./ansible-tools.rc &&
    . ./ansible-tools.rc &&
    cd "${tests_work_dir}" && {
      ansible-create-roles role-test &&
      cd "role-test/tests" &&
      echo "default" >> testcases &&
      bash ./tests-all.sh &&
      ansible-syntax-check &&
      ansible-test-run &&
      echo ""
    }; )

} &&
echo "[${tests_name}] DONE."

# End
exit $?
