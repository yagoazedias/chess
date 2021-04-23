#!/bin/bash
dir=`pwd`
sed -i -e "s?{changeme}?$dir?g" main.spec
