#!/bin/sh
awk -F, -e '
NR>6 {
a[$8]+=1
}
END {
    print("Kody pocztowe z mniej niż lub dokładnie 10 wystąpieniami:")
    max=0
    maxi=0
    for(i in a) {
        if(a[i]<11){
            print(i)
        }
        if(a[i]>max){
            max=a[i]
            maxi=i
        }
    }
    print("Kod, który wystąpił najczęściej to ", maxi, " z ", max, " wystąpieniami.")
}' <$1
