 # AI Log

## Entry 1

Date: 2026-10-05  
Tool: ChatGPT

Purpose:  
Help with the structure of the Python application.

What was suggested:
- Break the app into small modules for configuration, data loading, and report generation.
- Use a simple CLI entry point and keep business logic separate from file I/O.
- Add a clear folder structure so the code is easier to test and extend.

What I used:
- A modular layout with distinct Python files for app setup and logic.
- A main script that orchestrates tasks and calls reusable functions.

What I changed:
- Organized the application into smaller, focused components rather than keeping everything in one file.
- Added explicit responsibilities for configuration, data handling, and output generation.
- Established a cleaner flow for running the app from a single entry point.

How I tested it:
- Ran the app in a local development environment to confirm it started correctly.
- Checked that each module could be invoked without unexpected coupling.
- Verified the entry point produced the expected output and did not crash on a normal run.

## Entry 2

Date: 2026-10-05  
Tool: ChatGPT

Purpose:  
Help with Python programming.

Problem:
- The app logic needed clearer implementation details for processing input data and producing the final result.
- There was uncertainty around the best way to structure reusable functions and handle edge cases.

Suggested solution:
- Define helper functions for each task with clear inputs and outputs.
- Use readable variable names and guard clauses for validation.
- Keep functions small enough to test in isolation.

What I changed:
- Refactored repeated logic into helper functions.
- Added parameter validation and more defensive checks around file/data handling.
- Improved readability by simplifying the flow of operations in the main program.

How I tested it:
- Ran the script with sample input data.
- Confirmed expected outputs were produced for valid data.
- Tested a few edge cases, such as missing or malformed input, to ensure the program behaved predictably.

## Entry 3

Date: 2026-10-05  
Tool: ChatGPT

Purpose:  
Help with automated testing.

What was suggested:
- Add tests for the core functions instead of only testing the full app manually.
- Cover normal behavior, edge cases, and failure conditions.
- Keep tests focused and easy to run in an automated environment.

What I used:
- A small test suite targeting the most important functions.
- Assertions to verify expected results and error handling.

How I tested it:
- Executed the automated test suite locally.
- Confirmed the tests passed for the main scenarios and highlighted any failing assumptions.
- Used the results to refine the code and improve reliability.

## Entry 4
Date: 9/10/26
Tool: VS Code Copilot
Prompt: Suggest ways to expand the app using our current data set.

Yes. With the existing data, you can make the app more interactive and insightful without adding datasets. You have roughly a year of daily weather observations (`weather.csv`) and descriptions for all six seasons (`season_info.csv`).

**My top pick: a seasonal timeline.** Let users move through the year by date or season and see the corresponding seasonal description alongside daily or summarized temperature and rainfall. This connects the two datasets in a useful way without implying that the weather data validates the cultural knowledge.

Other good options:
- **Rainfall and temperature calendar:** Use a month-by-month heatmap or timeline to make changes across the year easier to spot.
- **Custom date range:** Let users select dates and see summary statistics and charts for that period, alongside the seasons it covers.
- **Season comparison cards:** Present each season’s description, typical period, average temperatures, rainfall, and rainy days together.
- **Data explorer:** Add a table users can filter by date or season and download as CSV.
- **Season transition view:** Highlight the changes between consecutive seasons in the observations, while presenting them as weather patterns—not as cultural indicators.

Because the current data covers only one location and one year, comparisons between years or places would need more data. But a timeline or date-range explorer is a practical next step using what you already have.

## Entry 5
Date: 9/10/26
Tool: VS Code Copilot
Prompt: Can you make another page titled 'Select a date' where you add the custom date range idea.

I’ll move the date-range controls and filtered analysis into a dedicated **Select a date** page, and leave **Weather Analysis** with its original all-data behavior.

Edit 

Ran terminal command: git --no-pager diff --check && git --no-pager diff -- app.py

Running tests...

## Entry 6
Date: 9/10/26
Tool: VS Code Copilot
Prompt: Please change the seasonal explorere tab background colour to #a4bab9.

I’ll add the requested color to Seasonal Explorer only, preserving the Home background.

Read , lines 30 to 90
Completed with input: {
  "path": "/Users/cassiemcallen/Documents/cits1501/Group_Project/seasonal-knowledge/app.py",
  "view_range": [
    30,
    90
  ]
}

Edit 

Ran terminal command: git --no-pager diff --check

Set the Seasonal Explorer background to **`#a4bab9`**. The Home page remains **`#b4d9b7`**. Whitespace validation passed.

## Entry 7
Date: 9/10/26
Tool: VS Code Copilot
Prompt: Can you please add this image (https://www.waitoc.com/fast-find/latest-news/birak-season-young) underneath the general overview when the Birak season is selected in the seasonal explorer tab.

I’ll verify the Wikimedia image’s attribution/license details, then add it beneath the Birak overview with an appropriate source credit.

Fetched [https://commons.wikimedia.org/wiki/File:Christmas_tree_02_gnangarra.jpg](https://commons.wikimedia.org/wiki/File:Christmas_tree_02_gnangarra.jpg)
Completed with input: {"url":"https://commons.wikimedia.org/wiki/File:Christmas_tree_02_gnangarra.jpg"}

Read , lines 45 to 90
Completed with input: {
  "path": "/Users/cassiemcallen/Documents/cits1501/Group_Project/seasonal-knowledge/app.py",
  "view_range": [
    45,
    90
  ]
}

Ran terminal command: git status --short

Fetched [https://commons.wikimedia.org/w/api.php?action=query&titles=File%3AChristmas_...](https://commons.wikimedia.org/w/api.php?action=query&titles=File%3AChristmas_tree_02_gnangarra.jpg&prop=imageinfo&iiprop=extmetadata%7Curl&iiurlwidth=1200&format=json)
Completed with input: {"url":"https://commons.wikimedia.org/w/api.php?action=query&titles=File%3AChristmas_tree_02_gnangarra.jpg&prop=imageinfo&iiprop=extmetadata%7Curl&iiurlwidth=1200&format=json"}

Edit 

Ran terminal command: /usr/local/bin/python3 -c "from streamlit.testing.v1 import AppTest; app=AppTest.from_file('app.py').run(); app.sidebar.radio[0].set_value('Seasonal Explorer').run(); print('images:', len(app.get('imgs')), 'exceptions:', len(app.exception)); print('caption:', [e.value for e in app.caption])"

Ran terminal command: git --no-pager diff --check && git --no-pager diff -- app.py

Ran terminal command: /usr/local/bin/python3 -c "from streamlit.testing.v1 import AppTest; app=AppTest.from_file('app.py').run(); app.sidebar.radio[0].set_value('Seasonal Explorer').run(); print([(s.label, s.value) for s in app.selectbox]); print([(e.type, getattr(e, 'value', None)) for e in app])"

Edit 

Ran terminal command: /usr/local/bin/python3 -m pytest -q tests/test_seasonal_explorer.py tests/test_date_picker.py

Ran terminal command: git --no-pager diff --check && git status --short

Added the Wikimedia Commons Christmas tree image beneath the environmental overview when Birak is selected in `app.py`. The image includes its caption and Gnangarra attribution with a link to its **CC BY 2.5 AU** license.

Added tests in `test_seasonal_explorer.py` to verify the image appears for Birak only. All 5 seasonal explorer and date-picker tests passed.