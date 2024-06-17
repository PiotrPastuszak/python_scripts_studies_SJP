#!/bin/sh
awk -F, -e '
{
  if (NR>1) {
    niezdawaneosoba=0
    if($4!=-1.0) {
      jeden+=1.0*$4
    }
    else {
      niezdawaneosoba+=1
      niezdawanejeden+=1
    }
    if ($5!=-1.0) {
      dwa+=1.0*$5
    }
    else {
      niezdawaneosoba+=1
      niezdawanedwa+=1
    }
    if($6!=-1.0) {
      trzy+=1.0*$6
    }
    else {
      niezdawaneosoba+=1
      niezdawanetrzy+=1
    }
    if ($7!=-1.0) {
      cztery+=1.0*$7
    }
    else {
      niezdawaneosoba+=1
      niezdawanecztery+=1
    }
    if($8!=-1.0) {
      final+=1.0*$8
    }
    else {
      niezdawaneosoba+=1
      niezdawanefinal+=1
    }
    print($1," ",$2," ",($4+$5+$6+$7+$8)/5.0, " ",($4+$5+$6+$7+$8)/(5-niezdawaneosoba) )
  }
}
END {
  print("srednia z testu 1 ", jeden/(NR-1-niezdawanejeden))
  print("srednia z testu 2 ", dwa/(NR-1-niezdawanedwa))
  print("srednia z testu 3 ", trzy/(NR-1-niezdawanetrzy))
  print("srednia z testu 4 ", cztery/(NR-1-niezdawanecztery))
  print("srednia z testu finalnego ", final/(NR-1-niezdawanefinal))
}
' <$1
