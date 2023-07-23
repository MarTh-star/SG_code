# 4. Using pandas

Date: 2023-07-23

## Status

Accepted

## Context

There was a need to read a csv file into a database table which made it necessary to somehow find a way to work with the csv file.

## Decision

Pandas was used since it is an easy and well known way to work with data. And in difference with other options (such as reading the csv in immediately to the database table) made it possible to create a dataframe that could be worked on before entering the information into the database.

## Consequences

Entering each dataframe row into the database table was easy.
