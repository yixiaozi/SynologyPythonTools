#!/bin/sh
location="/volume2/homes/yixiaozi/Drive/Docear"
find $location -type d -name "@eaDir" -print0 | xargs -0 rm -rf