#!/bin/sh
sed -e 's/-/;/' -e 's/-/;/' <$1 | awk -F\; -e '
{
    a[$2]+=1.0*$5
    b[$4]+=1.0*$5
}
END {
    print("1 ", a["01"])
    print("2 ", a["02"])
    print("3 ", a["03"])
    print("4 ", a["04"])
    print("5 ", a["05"])
    print("6 ", a["06"])
    print("7 ", a["07"])
    print("8 ", a["08"])
    print("9 ", a["09"])
    print("10 ", a["10"])
    print("11 ", a["11"])
    print("12 ", a["12"])
    print("-------------")
    print("00:00 ", b["00:00"])
    print("01:00 ", b["1:00"])
    print("02:00 ", b["2:00"])
    print("03:00 ", b["3:00"])
    print("04:00 ", b["4:00"])
    print("05:00 ", b["5:00"])
    print("06:00 ", b["6:00"])
    print("07:00 ", b["7:00"])
    print("08:00 ", b["8:00"])
    print("09:00 ", b["9:00"])
    print("10:00 ", b["10:00"])
    print("11:00 ", b["11:00"])
    print("12:00 ", b["12:00"])
    print("13:00 ", b["13:00"])
    print("14:00 ", b["14:00"])
    print("15:00 ", b["15:00"])
    print("16:00 ", b["16:00"])
    print("17:00 ", b["17:00"])
    print("18:00 ", b["18:00"])
    print("19:00 ", b["19:00"])
    print("20:00 ", b["20:00"])
    print("21:00 ", b["21:00"])
    print("22:00 ", b["22:00"])
    print("23:00 ", b["23:00"])
}'
