#!/bin/bash
set -e

psql --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE DATABASE nomnom_db;
    CREATE USER nomnom WITH PASSWORD 'test';
    ALTER DATABASE nomnom_db OWNER TO nomnom;
EOSQL