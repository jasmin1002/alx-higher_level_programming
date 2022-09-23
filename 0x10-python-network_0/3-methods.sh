#!/bin/bash
# Script displays all http methods support by server
curl -sI $1 | grep 'Allow' | cut -d ' ' -f2-
