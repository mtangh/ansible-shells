#!/bin/bash
THIS="${BASH_SOURCE##*/}"
CDIR=$([ -n "${BASH_SOURCE%/*}" ] && cd "${BASH_SOURCE%/*}" &>/dev/null; pwd)

# Run tests
echo "[${tests_name}] ansible-ping" && {

  ( bash -n ./ansible-tools.rc &&
    . ./ansible-tools.rc &&
    ansible-ping localhost 2>&1 |
    grep SUCCESS; )

} &&
echo "[${tests_name}] DONE."

# End
exit $?
