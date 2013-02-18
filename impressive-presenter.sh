#!/bin/bash

# impressive-presenter
# http://github.com/flobosg/impressive-presenter
# An HTML presenter screen for Impressive

if { [ -z "$1" ] && [ -t 0 ] ; } || [ "$1" == '-h' ]
then
	cat <<EOF

  USAGE:
    impressive-presenter FILE...

EOF
	exit
fi

SCRIPTDIR=$(dirname $0)
SLIDESDIR=$(dirname $1)/slides
mkdir -p $SLIDESDIR
if [[ "$(ls -A $SLIDESDIR)" ]]; then
	echo Emptying previews directory...
	rm $SLIDESDIR/slide-*.png
fi
echo Generating slide previews...
convert $1 -density 100 $SLIDESDIR/slide.png
echo Generating .info file...
python $SCRIPTDIR/makeinfo.py $1
echo Copying presenter.html...
cp $SCRIPTDIR/presenter.html $(dirname $1)
echo Copying jquery-1.3.2.min.js...
cp $SCRIPTDIR/jquery-1.3.2.min.js $(dirname $1)