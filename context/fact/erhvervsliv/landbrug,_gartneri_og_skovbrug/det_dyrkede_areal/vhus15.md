table: fact.vhus15
description: Kulturer i væksthuse efter enhed, kulturer og tid
measure: indhold (unit -)
columns:
- tal: values [ANTAL=Bedrifter (antal), KVM=Kvadratmeter (m2)]
- kult: values [V90=Væksthuse i alt, V02=Salat, V04=Cherry- og cocktailtomater, V06=Andre tomater, V08=Agurker, V11=Krydderurter, V12=Peber og chili, V14=Andre grøntsager og champignon, V16=Grøntsager og champignon i alt, V18=Jordbær under glas eller anden fast overdækning, V20=Snitblomster og snitgrønt, V50=Potteplanter i alt, V30=Potteplanter, grønne, V40=Potteplanter, blomstrende, V60=Planteskolekulturer, V70=Udplantningsplanter, småplanter og stiklinger, V73=Forædling og forsøg, V77=Andre kulturer i væksthus, V80=Ubenyttet væksthusareal]
- tid: date range 2015-01-01 to 2024-01-01
notes:
- tal is a measurement selector: ANTAL=Bedrifter (antal), KVM=Kvadratmeter. Every kult row appears twice. Always filter to one tal value.
- kult contains subtotals: V16=Grøntsager og champignon i alt (sum of V02–V14), V50=Potteplanter i alt (sum of V30+V40), V90=Væksthuse i alt (grand total = V16+V18+V20+V50+V60+V70+V73+V77+V80). Never sum across all kult values — pick individual cultures OR use the appropriate total.
- V80=Ubenyttet væksthusareal is included in V90 but represents unused space, not a crop. Consider excluding it when counting productive area.
- Table covers only greenhouse (væksthus) cultivation from 2015. For open-field horticulture area use afg6 (afgrode=180 gartneriafgrøder).
