# Bikeshare Data Analysis

In this repository, I explore bike-sharing data using a Python application and a separate data exploration project. I completed both as part of the Udacity data analysis program to practice Python, working with data, and communicating findings through plots.

## What is included?

- **Bikeshare CLI:** An interactive Python application that explores trip data from Chicago, New York City, and Washington. You can choose a city, filter by month or day, and see statistics about popular travel times, stations, trip durations, and users.
- **Ford GoBike exploration:** An analysis of rides in the San Francisco Bay Area during February 2019. I explore how trip duration and ride patterns differ by user type, age, gender, and day of the week. The exploration is saved as HTML, with a separate presentation notebook.

## Data

The datasets used in this project are not included in the repository because of their file size.

The command-line application expects the following files inside the same directory:

- `chicago.csv`
- `new_york_city.csv`
- `washington.csv`

The two parts use different datasets.

## Run the Python application

You need Python 3 and pandas. Keep `chicago.csv`, `new_york_city.csv`, and `washington.csv` in the same folder as `bikeshare.py`. These datasets were provided as part of the Udacity Data Analyst Nanodegree.

The original trip data can also be obtained from the respective bikeshare systems:

- [Chicago Divvy trip data](https://divvybikes.com/system-data)
- [New York Citi Bike trip data](https://citibikenyc.com/system-data)
- [Washington Capital Bikeshare trip data](https://capitalbikeshare.com/system-data)

Please note that the files supplied by Udacity were prepared for the project. Data downloaded directly from the original providers may have different filenames or column structures and may require preprocessing.

Open a terminal in the repository folder containing the script, then run:

```bash
python3 -m pip install pandas
python3 bikeshare.py
```

Follow the prompts to choose a city (`ch`, `ny`, or `w`) and any time filters

## Read the exploration

Open `exploration.html` in a browser to read the analysis and plots. The presentation is also available as HTML and as `slide_deck.ipynb`.

To run the presentation notebook, keep the original dataset `201902-fordgobike-tripdata.csv` -which can be downloaded from Kaggle- beside the notebook.
