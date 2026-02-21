# Mapping Tables Overview

Quick reference guide for Danmarks Statistik mapping tables. Use this to find the right classification for your analysis.

## Geographic & Administrative

### Regional Structure

| Table ID | Description | Rows | Period | Use When |
|----------|-------------|------|--------|----------|
| **nuts** | Regions, landsdele, municipalities (post-2007 reform) | 115 | 2007+ | Current administrative structure |
| **politikredse** | Police districts (12 districts) | 111 | 2007+ | Law enforcement geography |
| **landbrugslandsdele** | Agricultural regions (between regions and landsdele) | 123 | - | Agriculture-specific regional analysis |

### Municipality Classifications

| Table ID | Description | Rows | Use When |
|----------|-------------|------|----------|
| **kommunegrupper** | 5 municipality types by urbanization | 103 | Comparing urban/rural characteristics |
| **degurba_dst** | Urbanization degree (DST version) | 108 | Population density analysis |
| **degurba_eu** | Urbanization degree (EU version) | 102 | EU-comparable urbanization data |

### International Geography

| Table ID | Description | Rows | Use When |
|----------|-------------|------|----------|
| **lande_uhv** | GEONOM country codes (alpha-2) | 280 | Foreign trade statistics |
| **lande_uht_bb** | Country classification (alternative) | 269 | Specific foreign trade contexts |
| **lande_psd** | Country classification (alternative) | 284 | Public sector data |
| **nuts_eu** | EU regional nomenclature | 2,079 | EU-wide regional comparisons |

## Economic Classifications

### Industry & Business

| Table ID | Description | Rows | Period | Use When |
|----------|-------------|------|--------|----------|
| **db** | Dansk Branchekode 2025 (DB25) - 6-digit | 1,785 | 2025+ | Current industry classification |
| **nr_branche** | National accounts industry grouping | 258 | - | National accounts analysis |

### Trade & Transport

| Table ID | Description | Rows | Use When |
|----------|-------------|------|----------|
| **sitc** | Standard International Trade Classification | 3,292 | Goods trade by commodity type |
| **ebops** | Extended Balance of Payments Services 2010 | 91 | Services trade classification |
| **nst** | Standard Goods Classification for Transport (2007) | 101 | Transport statistics |
| **kn** | Combined Nomenclature (detailed goods) | 16,766 | Highly detailed goods classification |
| **valuta_iso** | ISO currency codes | 163 | Foreign exchange/trade |

### Consumption & Prices

| Table ID | Description | Rows | Use When |
|----------|-------------|------|----------|
| **ecoicop** | Consumption expenditure classification | 479 | Consumer spending analysis |
| **ecoicop_dst** | ECOICOP (DST extended version) | 867 | Detailed consumption analysis |

## Labor Market & Demographics

### Occupation & Employment

| Table ID | Description | Rows | Use When |
|----------|-------------|------|----------|
| **disco** | DISCO-08 occupational classification (6-digit) | 1,171 | Job/occupation classification |
| **disco_ls** | DISCO variant | 1,158 | Alternative DISCO application |
| **socio** | Socio-economic classification (SOCIO13) | 35 | Income source/employment status |
| **soc_status** | Social status classification | 52 | Social position analysis |

### Origin & Demographics

| Table ID | Description | Rows | Use When |
|----------|-------------|------|----------|
| **herkomst** | Origin/heritage classification | 4 | Immigrant background analysis |

## Education

| Table ID | Description | Rows | Use When |
|----------|-------------|------|----------|
| **ddu_udd** | Danish Education Classification (DDU) | 4,627 | All education types |
| **ddu_audd** | Danish Education Classification (alternative) | 4,422 | Specific education contexts |

## Public Sector & Finance

### Government Functions

| Table ID | Description | Rows | Use When |
|----------|-------------|------|----------|
| **cofog** | Classification of Functions of Government | 188 | Government expenditure by purpose |
| **cepa** | Environmental protection activities | 75 | Environmental spending |
| **crema** | Resource management activities | 7 | Resource management spending |

### National Accounts

| Table ID | Description | Rows | Use When |
|----------|-------------|------|----------|
| **esr_sekt** | ESA sector classification | 49 | Institutional sector analysis |
| **esa** | European System of Accounts | 48 | National accounts framework |
| **icha** | Health care classification | 48 | Health expenditure analysis |
| **icha_hp** | Health care providers | 41 | Health provider analysis |
| **esspros** | Social protection classification | 59 | Social security statistics |

## Buildings & Property

| Table ID | Description | Rows | Use When |
|----------|-------------|------|----------|
| **byganv** | Building use classification (BBR-based) | 121 | Building type analysis |
| **bygherre** | Builder/developer classification | - | Construction statistics |
| **ejendom** | Property classification | 34 | Real estate analysis |
| **benkod** | Building codes | 39 | Specific building categorization |

## Other Specialized Classifications

| Table ID | Description | Rows | Use When |
|----------|-------------|------|----------|
| **kulturemner** | Cultural topics (28 categories, UNESCO-based) | 34 | Cultural statistics |
| **okologisketail** | Organic statistics | 101 | Organic product analysis |
| **overtraedtype** | Offense/violation types | 1,408 | Crime statistics |

## Quick Selection Guide

### By Data Type

**Population data** → herkomst, socio, disco
**Business data** → db/db07, nr_branche
**Trade data** → sitc, ebops, kn, lande_uhv
**Regional data** → nuts, kommunegrupper, degurba_dst
**Public spending** → cofog, cepa, crema
**Education** → ddu_udd, ddu_audd
**Buildings** → byganv, bygherre, ejendom
**Health** → icha, icha_hp

### By Time Period

**Current (2007+)** → nuts, db (2025+), politikredse
**Historical (pre-2007)** → amt_kom, db07

## Technical Notes

- All dimension tables are stored in `data/dst/mapping_tables/{table_id}/`
- Standard columns: SEKVENS, KODE, NIVEAU, TITEL, GENERELLE_NOTER, INKLUDERER, INKLUDERER_OGSÅ, EKSKLUDERER, PARAGRAF, MÅLEENHED
- Use the `tables` skill to preview, describe, or inspect any mapping table
- Most classifications have multiple hierarchical levels accessible via the NIVEAU column

## Usage Examples

```bash
# Preview a mapping table
python .claude/skills/tables/scripts/tables.py preview disco --type dimension --rows 10

# Get full description
python .claude/skills/tables/scripts/tables.py describe nuts

# View schema
python .claude/skills/tables/scripts/tables.py schema db --type dimension
```
