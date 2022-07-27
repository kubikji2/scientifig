#!/bin/bash

pandoc $1 -f markdown -t dokuwiki > "${1%.*}.dw"
