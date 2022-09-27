#!/bin/bash
# cURL a JSON file
curl -sX POST --data-urlencode @$2 $1
