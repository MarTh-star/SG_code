# SG code

## Project description
This project is able to take parameters in order to collect information from a table in the database.
Furthermore it's possible to create a new table and insert information into the table.
There are two get commands, one will get an interval of date and times from the chosen table as chosen by the user. The other one will simply collect the top values from the database, limited by user input but with a default input of 10.

## Skills used
This project uses FastAPI to create a quick API Framework in order to query the database that was created using psycopg2 and is also what connects the python project with the PostgreSQL database.

## Challenges
This project has been put into a docker container which was quite a challenge to do to ensure that both the database and server were put into the same controller and working together. Since it was also the first time using Docker it was quite a challenge to get it all going like intended.

## Future improvements
The code could do with a lot of improvements that have not been implemented because of a lack of time. The code is note as modulated and as it could be and improvements could be made for how methods are made. More classes could have been used and better handling to make the code have an overall higher quality.

One of the requirements of the challenge was scalability but this was not something that I had time to implement in the given time frame. Given enough time I would have liked to work on this more in order to really create an application that could easily scale up and down.

## How to run the project
1. Clone repository
2. Run docker compose up --build in the terminal
3. Go to localhost:8000/docs, instructions 4-6 are all done on this page
4. Create table using the /create_table post request and enter in a name for the table as a paramter
5. Input data into table that you created using /input_test_data and enter the table name as a parameter
    -The inquiry will run for a long time but doesn't have to be repeated after the first build
6. Query data using /data or /get_top get requests. /get_top uses the table name and a number limiter as parameters. /data has several paramters that is explained below.

### Query parameters for testing api_queries /data
In order to get data
- ```table_name``` = the name that you chose in step 4 (string)
- ```start_time``` = YYYY-MM-DDTHH:MM:SS (string)
- ```end_time``` = YYYY-MM-DDTHH:MM:SS (string)
- ```interval_minutes``` = integer
