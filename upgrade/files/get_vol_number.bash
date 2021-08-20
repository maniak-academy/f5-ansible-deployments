OLDIFS="$IFS"
IFS=$'\n'
disk=$(tmsh show sys sof status | awk '/.D[1-9]/{print substr($1,1,4)}' | head -n1)
maxvnumber=0
for vnumber in $(tmsh show sys sof status | grep complete)
    do
        vnumber=${vnumber:4:2}
        vnumber=${vnumber// /}
        if (( vnumber > maxvnumber )); then
            maxvnumber=$vnumber
        fi
done
volume=$disk$((maxvnumber + 1))
echo -n $volume
IFS="$OLDIFS"

Prerequisites

You must meet the