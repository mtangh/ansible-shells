#!/bin/bash
THIS="${BASH_SOURCE##*/}"
CDIR=$([ -n "${BASH_SOURCE%/*}" ] && cd "${BASH_SOURCE%/*}" &>/dev/null; pwd)

# Run tests
echo "[${tests_name}] ansible-get-facts" && {

  ( bash -n ./ansible-tools.rc &&
    . ./ansible-tools.rc &&
    ansible-get-facts localhost 2>&1 )

} &&
echo "[${tests_name}] DONE."

# End
exit $?
