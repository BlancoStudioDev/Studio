#!/bin/bash
# Gestione server PostgreSQL per il database imdb sulla porta 5433

PGDATA="/opt/homebrew/var/postgresql@15"
PGPORT=5433

case "$1" in
  start)
    pg_ctl start -D "$PGDATA" -l "$PGDATA/logfile.log"
    echo "PostgreSQL avviato sulla porta $PGPORT"
    ;;
  stop)
    pg_ctl stop -D "$PGDATA"
    echo "PostgreSQL fermato"
    ;;
  restart)
    pg_ctl restart -D "$PGDATA"
    echo "PostgreSQL riavviato sulla porta $PGPORT"
    ;;
  status)
    pg_ctl status -D "$PGDATA"
    ;;
  *)
    echo "Uso: $0 {start|stop|restart|status}"
    exit 1
    ;;
esac
