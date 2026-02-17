# Data Pipeline

Downloads and processes Denmark Statistics data into PostgreSQL.

## Process

1. **statbank_to_disk/**: Download all public tables from dst.dk with descriptions and subject hierarchies
2. **fact_col_to_dim_table/**: Analyze fact tables and create links to dimension tables from dst.dk nomenclature documentation
3. **disk_to_db/**: Process and load all tables into PostgreSQL database
