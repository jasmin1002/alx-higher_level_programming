#!/bin/bash
# Script displays the size of the body of the response
url=$1
curl $url -w %{size_download}\\n
