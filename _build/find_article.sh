#!/bin/bash

echo "This script find some keywords in articles"

if [ "${1}" == "" ]; then
  read keyword
else
  keyword="${1}"
fi

pushd .. >> /dev/null
echo "Keyword : ${keyworkd}"
grep -rn ${keyword}
popd >> /dev/null
