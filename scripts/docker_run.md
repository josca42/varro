docker run -d -p 3142:3000 \
  --name metabase \
  -e "MB_DB_TYPE=postgres" \
  -e "MB_DB_DBNAME=metabaseappdb" \
  -e "MB_DB_PORT=5432" \
  -e "MB_DB_USER=metabase" \
  -e "MB_DB_PASS=zr4G32Bv62phpKxDwF" \
  -e "MB_DB_HOST=172.17.0.1" \
  metabase/metabase