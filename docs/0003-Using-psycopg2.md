# 3. Using psycopg2

Date: 2023-07-23

## Status

Accepted

## Context

Since there was a need to connect to a postgreSQL server and later database and table a program needed to be chosen to connect to it.

## Decision

Using psycopg2 was decided on since it had an uncomplicated implementation and seemed popular with other python users making it easier to find support if needed.

## Consequences

Connecting to the postgreSQL server and database was easy and setup could be done fairly quickly, and trouble could easily be resolved by looking for others who had had similar issues.
