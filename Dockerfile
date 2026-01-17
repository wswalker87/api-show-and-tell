FROM postgres:15


ENV POSTGRES_DB=api_show_and_tell
ENV POSTGRES_PASSWORD=postgres

COPY --chown=postgres:postgres init.sql /docker-entrypoint-initdb.d/

RUN chmod 644 /docker-entrypoint-initdb.d/init.sql
