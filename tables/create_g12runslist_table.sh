#!/bin/bash



PREV=0;
PREVC=60
for i in `g12runs -tprod`; do
    THIS=`echo $i | awk '{print $1}'`;
    THISC=`g12runs -tprod -e -r$THIS | awk '{print $2}'`
    if [[ $(($THIS - 1)) -ne $PREV || $THISC -ne $PREVC ]]; then
        echo "";
    fi;
    echo -n "$THIS ";
    PREV=$THIS;
    PREVC=$THISC
done \
| awk '{print $1"-"$NF}' > tmp$$

for i in `cat tmp$$`; do
    A=`echo $i | awk -F- '{print $1}'`
    B=`echo $i | awk -F- '{print $NF}'`
    if [[ $A -ge 56363 ]]; then
        C=`g12runs -tprod -r$A -e | awk '{print $2}'`
        if [[ $A -eq $B ]]; then
            echo "$A $C"
        else
            echo "$A-$B $C"
        fi
    fi
done > g12_prod_runlist.txt

rm tmp$$

