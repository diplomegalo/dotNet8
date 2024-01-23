#!/bin/bash
docker run -p 1433:1433 --name sqlserver1 -d -it --rm -e "ACCEPT_EULA=Y" -e "MSSQL_SA_PASSWORD=P@ssw0rd" mcr.microsoft.com/mssql/server:2022-latest
