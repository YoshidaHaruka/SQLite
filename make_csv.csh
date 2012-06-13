#!/bin/csh -f

cat ske.dat \
    | grep -v \# \
    | sed 's/\//-/g' \
    | sed 's/\t\t/\t/g' \
    | cut -f -12 \
    | sed 's/\t/,/g' \
    | sed 's/-\([0-9]\)-/-0\1-/g' \
    | sed 's/-\([0-9]\),/-0\1,/g' \
    > ske.csv
