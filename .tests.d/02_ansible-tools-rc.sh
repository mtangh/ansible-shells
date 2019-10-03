#!/bin/bash
THIS="${BASH_SOURCE##*/}"
CDIR=$([ -n "${BASH_SOURCE%/*}" ] && cd "${BASH_SOURCE%/*}" &>/dev/null; pwd)

# Run tests
echo "[${tests_name}] loading rc" && {

  ( bash -n ./ansible-tools.rc &&
    . ./ansible-tools.rc &&
    declare -F |
    egrep -- ' -f ansible-(get-facts|test-run)$' )

} &&
echo "[${tests_name}] DONE."

# End
exit $?
