table: fact.msr3a
description: Anvendelse af naturressourcer, varer og affald (Detaljeniveau 3) efter materialetype, kategori og tid
measure: indhold (unit Ton)
columns:
- mater: values [A0=Materialer i alt, A110=Naturressourcer, primære afgrøder, A120=Naturressourcer, græs, grønfoder og halm mv., A129=Naturressourcer, anden biomasse, inkl. haveaffald, A130=Naturressourcer, træ, brænde og skovflis ... WA594=Øvrige residualer, human fødevareomsætning og udledning til kloak mv. (balance), WA596=Øvrige residualer, spredning af materialer i miljøet mv. (balance), WU1=Udledning til luft, energirelaterede, WU2=Udledning til luft, procesrelaterede, ZB=Balance]
- dyrkat: values [AAASUM=Anvendelse i alt, AABSUM=Forbrug i produktionen i alt, ABCSUM=Anden anvendelse i alt, AA9090=Residualer til miljø, AA6000=Eksport ... NBLA_B=Ejendomshandel, boliger og udlejning af erhvervsejendomme, NBM_N=Erhvervsservice, NBO_Q=Offentlig administration mv., undervisning og sundhed, NBR=Kultur og fritid, NBSA=Andre serviceydelser]
- tid: date range 2018-01-01 to 2020-01-01
notes:
- dyrkat mixes aggregate totals and individual categories: AAASUM=Anvendelse i alt, AABSUM=Forbrug i produktionen i alt, ABCSUM=Anden anvendelse i alt are totals; AA9090/AA6000/AA3150/AA5000 are specific outflow flows; NBA/.../NBSA are individual industry branches. Never sum all dyrkat — pick totals or a consistent set of leaves.
- mater is hierarchical — filter to a consistent level to avoid double-counting.
- Very limited time range: 2018–2020 only.
