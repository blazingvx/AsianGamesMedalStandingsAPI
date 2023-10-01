# Medal Standings API

This is a simple Flask web application that scrapes medal standings data from a specific URL and serves it as a JSON API. The data is extracted from the [Hangzhou 2022 Asian Games official website](https://info.hangzhou2022.cn/en/results/all-sports/medal-standings.htm).

AccessAPI: https://blazingvx.github.io/AsianGamesMedalStandingsAPI/api/medal-standings


## Features

- Scrapes medal standings data from a specified URL.
- Serves the data as a JSON API.
- Easy configuration of the URL through a JSON configuration file.

## Usage

### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/medal-standings-api.git

2. Install the required Python packages using pip:

    ```bash
    pip install -r requirements.txt

### Configuration

1. Create a JSON configuration file named config.json in the project directory:

    ```bash
    {
    "medal_standings_url": "https://info.hangzhou2022.cn/en/results/all-sports/medal-standings.htm"
    }

Replace the medal_standings_url value with the URL from which you want to scrape medal standings data.

### Running the Application

1. Run the Flask application:

    ```bash
    python AsianGames2023.py

The application will start on http://localhost:5000/

2. Access the API endpoint to retrieve medal standings data in JSON format:

    ```bash
    http://localhost:5000/api/medal-standings

Replace localhost with the appropriate host if you are deploying the application on a server.

### Sample Response

The API will respond with a JSON array containing medal standings data. Each entry in the array represents a country's medal standings:

    [
    {
        "Rank": 1,
        "Country": "Japan",
        "Gold": 12,
        "Silver": 8,
        "Bronze": 5,
        "Total": 25
    },
    {
        "Rank": 2,
        "Country": "China",
        "Gold": 10,
        "Silver": 11,
        "Bronze": 5,
        "Total": 26
    },
    // ...
    ]

### Contributing

Feel free to contribute to this project by opening issues or submitting pull requests. Your contributions are highly appreciated.

### License

This project is licensed under the MIT License - see the LICENSE file for details.

### Acknowledgments

- This project uses the Flask web framework.
- Data is scraped from the [Hangzhou 2022 Asian Games official website](https://info.hangzhou2022.cn/en/results/all-sports/medal-standings.htm).


