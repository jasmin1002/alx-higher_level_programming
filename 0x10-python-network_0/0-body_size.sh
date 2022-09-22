#!/bin/bash
# Script displays the size of the body of the response
curl -s $1 -w %{size_download}\\n
