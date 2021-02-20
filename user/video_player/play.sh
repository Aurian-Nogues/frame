#!/bin/bash
trap "rm -f $1" EXIT
omxplayer --loop $1
