#!/bin/bash
#cript must send a POST request with the contents of a file, passed with the filename as the second argument of the script, in the body of the request
curl -s -H "content-type:application/json"  -d @"$2" -X POST "$1"
