#!/bin/sh
awk -e '
{
    sumaliter+=length($0)
    sumaslow+=NF
    for(i=1; i<=NF; i++)
    {
        a[$i]+=1
    }
}

END {
    print(NR, sumaslow, sumaliter+NR)
    for(z in a)
    {
        print(z, a[z])
    }
}
' <$1
