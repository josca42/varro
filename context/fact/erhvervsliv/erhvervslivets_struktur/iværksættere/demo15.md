table: fact.demo15
description: Erhvervsdemografi efter ejerform, enhed og tid
measure: indhold (unit -)
columns:
- ejerform: values [TOT=I ALT, 1=Enkeltmandsfirma, 2=Interessentskab mv., 4=Aktieselskab, 6=Fond, forening mv., 3=Anpartsselskab, 5=Andelsforening, 7=Offentlig myndighed, 9=Anden ejer]
- maengde4: values [AFU=Fuldtidsansatte (antal), OMS=Omsætning (mio kr.) , NYE=Nye firmaer (antal)]
- tid: date range 2019-01-01 to 2023-01-01

notes:
- ejerform TOT = national total across all ownership types. Exclude ejerform = 'TOT' when summing across ejerform categories — it doubles the count.
- maengde4 is a measurement selector — filter to one value: AFU=fuldtidsansatte, NYE=nye firmaer, OMS=omsætning (mio kr.).
- No dimension join needed — ejerform is fully inline with descriptive codes. Use the values directly.
- The dominant legal forms for new firms are enkeltmandsfirmaer (1) and anpartsselskaber (3).