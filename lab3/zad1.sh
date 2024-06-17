#!/bin/sh
sed -e 's/,[[:blank:]]*,/,/' <$1 | awk -F, '{if (NF!=10) {print $0}}'
