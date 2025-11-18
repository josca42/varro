# Fact-to-Dimension Linking Guide

Quick reference guide for linking fact table columns to dimension tables in the PostgreSQL database.

## Quick Decision Process

Follow these steps to identify the correct dimension table for a fact table column:

1. **Check column name pattern** (see patterns below)
2. **Match data type** (int64 → int KODE, object → string KODE)
3. **Validate with preview** (check if values exist in dimension KODE)
4. **Verify semantic meaning** (column content matches dimension purpose)

---

## Column Name → Dimension Table Mapping

### Geographic & Administrative

| Column Pattern | Data Type | Dimension Table | Example Values |
|----------------|-----------|-----------------|----------------|
| `OMRÅDE` | int64 | **nuts** or **kommunegrupper** | 101, 147, 155 (municipality codes) |
| `NUTS*` | varies | **nuts** or **nuts_eu** | Regional codes |
| `KOM*`, `KOMMUNE*` | int64 | **kommunegrupper** | Municipality groups |
| `LANDSDEL*` | int64 | **nuts** (niveau 2) | 1, 2, 3, 4, 5 (landsdele) |
| `REGION*` | int64 | **nuts** (niveau 1) | 84, 83, 82, 81, 85 (regions) |
| `POLITIKREDS*` | int64 | **politikredse** | Police districts |

### Demographics & Labor

| Column Pattern | Data Type | Dimension Table | Example Values |
|----------------|-----------|-----------------|----------------|
| `*HERK`, `HERKOMST*` | int64 | **herkomst** | 1 (dansk oprindelse), 2 (indvandrere), 3 (efterkommere) |
| `*SOCIO`, `SOCIO*` | int64 | **socio** | 1, 11, 110-114 (socio-economic status) |
| `*DISCO`, `DISCO*` | int64 | **disco** or **disco_ls** | 1, 11, 111, 1111 (occupation codes) |
| `*STAT`, `STATUS*` | int64 | **socio** or **soc_status** | Employment/social status |
| `KØN`, `KOEN`, `*KON` | int/object | - (coded: 1/2 or M/K) | Gender (not a dimension table) |

### Industry & Business

| Column Pattern | Data Type | Dimension Table | Example Values |
|----------------|-----------|-----------------|----------------|
| `BRANCHE*`, `*BRANCHE` | object | **db** | "A", "01", "01.1", "01.11.00" (industry codes) |
| `DB*` | object | **db** | Dansk Branchekode |
| `*NR_BRANCHE` | varies | **nr_branche** | National accounts industry |

### Trade & Economic

| Column Pattern | Data Type | Dimension Table | Example Values |
|----------------|-----------|-----------------|----------------|
| `*LAND`, `LANDE*`, `LAND_*` | object | **lande_uhv**, **lande_psd**, **lande_uht_bb** | "BE", "DK", "US" (country codes) |
| `*SITC`, `SITC*` | varies | **sitc** | Trade commodity codes |
| `*KN`, `KN*` | object | **kn** | "0101 21 00" (Combined Nomenclature) |
| `*EBOPS` | varies | **ebops** | Services trade codes |
| `*NST` | varies | **nst** | Transport goods codes |
| `VALUTA*` | object | **valuta_iso** | "DKK", "EUR", "USD" |

### Education

| Column Pattern | Data Type | Dimension Table | Example Values |
|----------------|-----------|-----------------|----------------|
| `*UDD`, `UDD*`, `UDDANNELSE*` | object | **ddu_udd** or **ddu_audd** | "0", "01", "010" (education codes) |

### Consumption & Spending

| Column Pattern | Data Type | Dimension Table | Example Values |
|----------------|-----------|-----------------|----------------|
| `*ECOICOP`, `ECOICOP*` | object | **ecoicop** or **ecoicop_dst** | "01", "01.1", "01.1.1" (consumption) |
| `*COFOG`, `COFOG*` | varies | **cofog** | Government function codes |
| `*CEPA` | varies | **cepa** | Environmental protection |
| `*CREMA` | varies | **crema** | Resource management |

### Buildings & Property

| Column Pattern | Data Type | Dimension Table | Example Values |
|----------------|-----------|-----------------|----------------|
| `BYGANV*`, `*BYGANV` | varies | **byganv** | Building use classification |
| `BYGHERRE*` | varies | **bygherre** | Builder/developer type |
| `EJENDOM*` | varies | **ejendom** | Property classification |
| `*BENKOD` | varies | **benkod** | Building codes |

### Health & Social

| Column Pattern | Data Type | Dimension Table | Example Values |
|----------------|-----------|-----------------|----------------|
| `*ICHA` | varies | **icha** | Health care classification |
| `*ICHA_HP` | varies | **icha_hp** | Health care providers |
| `*ESSPROS` | varies | **esspros** | Social protection |

### Public Sector

| Column Pattern | Data Type | Dimension Table | Example Values |
|----------------|-----------|-----------------|----------------|
| `*ESR_SEKT`, `SEKTOR*` | varies | **esr_sekt** | ESA sector codes |
| `*ESA` | varies | **esa** | European System of Accounts |

---

## Common Column Prefixes/Suffixes

Understanding prefixes and suffixes helps identify relationships:

| Prefix/Suffix | Meaning | Example | Links To |
|---------------|---------|---------|----------|
| `MO*` | Mother | MOHERK, MOSTAT | herkomst, socio |
| `FA*` | Father | FAHERK, FASTAT | herkomst, socio |
| `*OPRIND` | Origin | MOOPRIND, FAOPRIND | Country of origin |
| `*TYPE` | Type/Category | YDELSESTYPE, INDKOMSTTYPE | Various classification tables |
| `*GRUPPE` | Group | - | Grouped classifications |

---

## Data Type Matching Rules

**Critical:** Match column data type to dimension KODE type

### Integer Columns (int64)
Link to dimensions with **integer KODE**:
- herkomst
- socio
- disco / disco_ls
- nuts
- kommunegrupper
- politikredse
- soc_status
- degurba_dst / degurba_eu
- landbrugslandsdele

### String/Object Columns
Link to dimensions with **string/object KODE**:
- db (industry codes with dots)
- kn (Combined Nomenclature with spaces)
- ddu_udd / ddu_audd (education codes)
- lande_uhv / lande_psd / lande_uht_bb (country alpha-2 codes)
- ecoicop / ecoicop_dst (consumption codes with dots)
- valuta_iso (currency codes)
- sitc, ebops, nst (trade classifications)

---

## Step-by-Step Linking Guide

### Step 1: Identify the Column
Look at the fact table schema and identify columns that are NOT:
- `INDHOLD` (the measure value)
- `TID` (time period)
- Clear attribute codes (like `ALDER`, `KØN` with simple coded values)

### Step 2: Pattern Match
Use the column name patterns above to find candidate dimension tables.

**Example:**
- Column `OMRÅDE` (int64) → candidates: **nuts**, **kommunegrupper**
- Column `MOHERK` (int64) → candidate: **herkomst**
- Column `BRANCHE` (object) → candidate: **db**

### Step 3: Check Data Type
Ensure the fact table column data type matches the dimension KODE type.

```bash
# Check fact table column type
python .claude/skills/tables/scripts/tables.py view YOUR_FACT_TABLE --rows 5

# Check dimension KODE type
python varro/data/fact_col_to_dim_table/create_dimension_links.py view DIMENSION_NAME --rows 5
```

### Step 4: Validate Values
Preview both tables and verify that values in the fact table column exist in the dimension KODE column.

```bash
# Preview fact table to see actual values
python .claude/skills/tables/scripts/tables.py view YOUR_FACT_TABLE --rows 20

# Preview dimension to see KODE values
python varro/data/fact_col_to_dim_table/create_dimension_links.py view DIMENSION_NAME --rows 20
```

### Step 5: Verify Semantic Meaning
Read the dimension TITEL column to ensure the classification matches the expected meaning of your fact table column.

```bash
# See dimension descriptions
python varro/data/fact_col_to_dim_table/create_dimension_links.py view DIMENSION_NAME --rows 50
```

---

## Complete Examples

### Example 1: FOLK1A (Population Statistics)

**Fact table columns:**
```
OMRÅDE (int64)     → links to nuts.KODE
KØN (object)       → coded value (M/K or 1/2), not a dimension
ALDER (object)     → coded value (age), not a dimension
CIVILSTAND (object) → coded value (marital status), not a dimension
TID (object)       → time period, not a dimension
INDHOLD (int64)    → measure value
```

**Validation:**
```bash
# Check OMRÅDE values
python .claude/skills/tables/scripts/tables.py view FOLK1A --rows 10
# Shows: 101, 147, 155 (municipality codes)

# Verify in nuts
python varro/data/fact_col_to_dim_table/create_dimension_links.py view nuts --rows 20
# Confirms: 101=København, 147=Frederiksberg, 155=Dragør
```

### Example 2: FODIE (Birth Statistics)

**Fact table columns:**
```
OMRÅDE (int64)      → links to nuts.KODE
MOHERK (int64)      → links to herkomst.KODE (mother's origin)
MOOPRIND (int64)    → country code or classification
MOSTAT (int64)      → links to socio.KODE (mother's socio-economic status)
MODERSALDER (int64) → coded value (mother's age), not a dimension
BARNKON (object)    → coded value (child gender), not a dimension
TID (int64)         → time period, not a dimension
INDHOLD (int64)     → measure value
```

**Validation:**
```bash
# Check MOHERK values
python .claude/skills/tables/scripts/tables.py view FODIE --rows 10
# Shows: 5 and other values

# Verify in herkomst
python varro/data/fact_col_to_dim_table/create_dimension_links.py view herkomst --rows 10
# Confirms: 1=dansk oprindelse, 2=indvandrere, 3=efterkommere, 9=uoplyst
# Note: Value 5 might need further investigation
```

### Example 3: DODA1 (Death Statistics)

**Fact table columns:**
```
ÅRSAG (object)  → likely ICD10 disease codes (check if there's an ICD dimension)
ALDER (object)  → coded value (age), not a dimension
KØN (object)    → coded value (gender), not a dimension
TID (int64)     → time period, not a dimension
INDHOLD (int64) → measure value
```

**Note:** ÅRSAG appears to use ICD codes (e.g., "A01"). Check if an ICD dimension table exists in your database.

---

## When NOT to Link to a Dimension

Some columns are simple coded values and don't need dimension tables:

1. **Gender codes** (`KØN`, `KOEN`, `*KON`): Usually 1/2 or M/K
2. **Age groups** (`ALDER`): Often ranges like "0-4", "5-9", "TOT"
3. **Time periods** (`TID`): Dates or periods like "2008K2", "2024"
4. **Measures** (`INDHOLD`): The actual statistical value
5. **Simple binary flags**: Yes/No, True/False coded as 0/1
6. **Totals**: "TOT", "I ALT" indicating aggregate values

---

## Troubleshooting

### Problem: Column name doesn't match any pattern
**Solution:**
1. Preview the fact table to see actual values
2. Look at value format (numeric, alphanumeric, structure)
3. Search dimension tables for similar code structures
4. Check documentation or table description

### Problem: Data types don't match
**Solution:**
1. Consider if the column needs casting (int to string or vice versa)
2. Check if there are alternative dimension tables with different KODE types
3. Verify you're looking at the correct dimension variant (e.g., ecoicop vs ecoicop_dst)

### Problem: Values in fact table not found in dimension
**Solution:**
1. Check if the dimension table is for the correct time period
2. Look for historical dimension tables (e.g., amt_kom for pre-2007 data)
3. Verify you're using the right hierarchical level (NIVEAU)
4. Values might be aggregated codes not in the dimension

### Problem: Multiple candidate dimensions
**Solution:**
1. Check the dimension row counts and descriptions
2. Preview both dimensions to compare coverage
3. Look at the fact table time period (TID) to determine which classification version
4. Consult the [dimension_tables_overview.md](../../notes/dimension_tables_overview.md)

---

## Quick Commands Reference

```bash
# Preview a fact table
python .claude/skills/tables/scripts/tables.py view TABLE_NAME --rows 20

# Preview a dimension table
python varro/data/fact_col_to_dim_table/create_dimension_links.py view DIM_NAME --rows 20

# Get dimension description (if available)
python varro/data/fact_col_to_dim_table/create_dimension_links.py describe DIM_NAME

# List all available dimension tables
python varro/data/fact_col_to_dim_table/create_dimension_links.py list
```

---

## Summary Checklist

When linking a fact table column to a dimension table:

- [ ] Column name matches a known pattern
- [ ] Data types match (int64 ↔ int KODE, object ↔ string KODE)
- [ ] Sample values from fact table exist in dimension KODE
- [ ] Dimension TITEL descriptions make semantic sense
- [ ] Time period alignment (current vs historical classifications)
- [ ] Not a simple coded attribute (gender, age, totals)

---

**Related Documentation:**
- [Dimension Tables Overview](../../notes/dimension_tables_overview.md)
- Tables Skill: `/root/varro/.claude/skills/tables/`
