table: fact.msr3t
description: Tilgang af naturressourcer, varer og affald (Detaljeniveau 3) efter materialetype, kategori og tid
measure: indhold (unit Ton)
columns:
- mater: values [A0=Materialer i alt, A110=Naturressourcer, primære afgrøder, A120=Naturressourcer, græs, grønfoder og halm mv., A129=Naturressourcer, anden biomasse, inkl. haveaffald, A130=Naturressourcer, træ, brænde og skovflis ... WA594=Øvrige residualer, human fødevareomsætning og udledning til kloak mv. (balance), WA596=Øvrige residualer, spredning af materialer i miljøet mv. (balance), WU1=Udledning til luft, energirelaterede, WU2=Udledning til luft, procesrelaterede, ZB=Balance]
- dyrkat: values [ATASUM=Tilgang i alt, ATBSUM=Produktion i brancher i alt, ATCSUM=Anden tilgang i alt, TA1090=Indvinding af naturressourcer, TA0700=Import ... NBLA_B=Ejendomshandel, boliger og udlejning af erhvervsejendomme, NBM_N=Erhvervsservice, NBO_Q=Offentlig administration mv., undervisning og sundhed, NBR=Kultur og fritid, NBSA=Andre serviceydelser]
- tid: date range 2018-01-01 to 2020-01-01
notes:
- dyrkat mixes aggregate totals and individual categories: ATASUM=Tilgang i alt, ATBSUM=Produktion i brancher i alt, ATCSUM=Anden tilgang i alt are totals; TA1090/TA0700/TA0150 are specific inflow flows; NBA/NBB/.../NBSA are individual industry branches. Never sum all dyrkat — pick either a total code or a consistent set of leaf codes.
- mater is hierarchical — filter to a consistent level to avoid double-counting.
- Very limited time range: 2018–2020 only.
