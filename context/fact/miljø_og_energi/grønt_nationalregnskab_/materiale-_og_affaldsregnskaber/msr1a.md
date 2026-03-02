table: fact.msr1a
description: Anvendelse af naturressourcer, varer og affald (Detaljeniveau 1) efter materialetype, kategori og tid
measure: indhold (unit Ton)
columns:
- mater: values [A0=Materialer i alt, A1=Naturressourcer, biomasse (afgrøder, planter, træ, fisk, vildt), A3=Naturressourcer, mineraler (sand, grus, ler mv.), A4=Naturressourcer, fossil energi, CA=Produkter fra landbrug, skovbrug og fiskeri ... WA4=Affald til forbrænding, WA5=Øvrige residualer, udledt til miljø og kloaksystem mv. (balance), WU1=Udledning til luft, energirelaterede, WU2=Udledning til luft, procesrelaterede, ZB=Balance]
- dyrkat: values [AAASUM=Anvendelse i alt, AABSUM=Forbrug i produktionen i alt, ABCSUM=Anden anvendelse i alt, AA9090=Residualer til miljø, AA6000=Eksport ... NBK=Finansiering og forsikring, NBLA_B=Ejendomshandel, boliger og udlejning af erhvervsejendomme, NBM_N=Erhvervsservice, NBO_Q=Offentlig administration mv., undervisning og sundhed, NBR_S=Kultur, fritid, anden service]
- tid: date range 2018-01-01 to 2020-01-01
notes:
- dyrkat mixes aggregate totals and individual categories: AAASUM=Anvendelse i alt, AABSUM=Forbrug i produktionen i alt, ABCSUM=Anden anvendelse i alt are totals; AA9090/AA6000/AA3150/AA5000 are specific outflow flows; NBA/.../NBSA are individual industry branches. Never sum all dyrkat — pick totals or a consistent set of leaves.
- mater is hierarchical — filter to a consistent level to avoid double-counting.
- Very limited time range: 2018–2020 only.
