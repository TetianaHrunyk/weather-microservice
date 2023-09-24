# To run the application:

(1.)The repo comes with a db with some test data
If you want to start with a fresh db, delete `database.db` file and create a new sqlite db with the following command:

    make create_db # then type in .quit

2.  Insert your token for the weather API in src/config.py (or contact me to get mine)

3.  run the following command:

         docker-compose up

    This command will automatically start the service for storing the temperature each hour and
    the API.

    The API will be available at 0.0.0.0:80
    The root url is redirected to swagger docs (i.e 0.0.0.0:80/docs)

    Sample request: http://0.0.0.0:80/temperature?day=2023-09-23 (and add the header)

    The x-token is set in src/config.py

    Initially it is: asjdh98as7agejh325l4359ta1ysfdof

## Things to improve:

- Split requirements for API and data_processor
- Use hashed requirements.txt
- Add unit tests for the API

## How I would do this in the cloud

- I would not use the infinite while loop in src.data_processor.main, but rathe make a cloud function
  and a cloud scheduler to publish message every hour to the function
- I would use a database hosted in a cloud rather than the local db or db in docker
- The API and the data_collector would be two separate services
