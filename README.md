Project Plan: Tiger

Project Members: Rajneet & Hermaan

Project Overview: The project aims to build a web app using Flask and the OpenWeatherMap API to fetch and display the current weather data for Stockholm. The app will retrieve key weather parameters such as temperature, humidity, wind speed, sunrise, and sunset times. 


Workflow:

1) A request is sent to the OpenWeatherMap API to fetch the specific parameter related to weather in Stockholm.
2) A function processes the received data and displays the weather information through a web app, which is hosted on a specific port.
3) This unit test checks if the function returns a valid JSON response with the correct data types.
4) The aim of this integration test is to verify that the Flask app successfully fetches weather data from the OpenWeatherMap API using the correct API key and coordinates.
5) The project is integrated with a GitHub Actions pipeline where tests are run automatically.
6) Docker Containerization: When the tests pass the expected results, the application is containerized with Docker to create a    consistent environment for deployment.
7) The Docker-containerized app is deployed to Azure, where users can access the application with expected and reliable results. 
