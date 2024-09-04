# Step-by-Step Process for building the comps table

This code uses a combination of **Yahoo Finance** via the `yfinance` Python library, and **web scraping** using Selenium to extract financial data for different stock tickers, which is then saved to a CSV file. Below is the step-by-step process used to gather the necessary data:

---

1. **Install Required Python Libraries**:

- Ensure that the following Python packages are installed:
    - `pandas` for data manipulation
    - `yfinance` for retrieving stock data from Yahoo Finance
    - `selenium` for web scraping
    - `webdriver-manager` to manage the ChromeDriver
    - `re` for regular expressions to extract specific data patterns from text

Open your terminal or command prompt and install the necessary libraries by running the following commands:

```bash
pip install pandas yfinance selenium webdriver-manager
```

### 2. **Set Up the CSV File**:

- Ensure you have a CSV file (e.g., `FTC3_test.csv`) containing stock tickers in a column named `"Ticker"`.
- Place the file in the directory where you'll run the code.
- The CSV file should have at least one column named `Ticker` where each row contains the stock symbol (e.g., AAPL, TSLA, MSFT).
- Create new columns in the DataFrame to store additional data retrieved:
    - **Revenue**: Company’s total revenue
    - **Trailing PE**: Trailing price-to-earnings ratio
    - **Trailing EPS**: Earnings per share over the last 12 months
    - **52 Week Change**: Percentage change in the stock price over the past year
    - **Growth Estimate (Next 5 Years)**: Expected growth rate over the next 5 years
    - **Revenue Estimate**: Analyst-provided revenue estimates from Yahoo Finance's analysis page

### 3. **Download Chrome and Set Up ChromeDriver**:

- Ensure Google Chrome is installed on your machine.
- The script uses `webdriver-manager` to automatically manage ChromeDriver, so you don’t need to manually download it.

### 4. **Run the Code**:

- Copy and paste the provided code into a Python script file (e.g., `financial_scraper.py`).
- Update the `file_path` variable with the path to your CSV file:
    
    ```python
    file_path = '/path/to/your/csv/FTC3_test.csv'
    ```
    
- Run the script from your terminal or IDE:
    
    ```bash
    python financial_scraper.py
    ```
    

### 5. **Understand the Outputs**:

- As the script runs, it will:
    - Retrieve financial data like **Total Revenue**, **Trailing PE**, **Trailing EPS**, **52 Week Change**, etc.
    - Scrape Yahoo Finance's analysis page to gather **5-Year Growth Estimates** and **Revenue Estimates**.
- The processed data will be saved to an output CSV file (`yahoo_FT2_results_v3.csv`), created in the same directory where the script is run.

### 6. **Check Your Results**:

- After the script finishes running, check the CSV file (`yahoo_FT2_results_v3.csv`) to see the updated data for each stock ticker.
- Columns in the output will include:
    - Ticker
    - Revenue (formatted in millions or billions)
    - Trailing PE Ratio
    - Trailing EPS
    - 52 Week Change (%)
    - Stock Price
    - Currency
    - Growth Estimate (Next 5 Years) %
    - Revenue Estimate

---

### Example Folder Structure:

```
/my_project_directory/
    financial_scraper.py         # Python script
    FTC3_test.csv                # Input CSV file
    yahoo_FT2_results_v3.csv     # Output CSV file (created after running the script)

```

### Summary of Tools Used:

- **`yfinance`**: To fetch financial data like revenue, PE ratio, and EPS.
- **`selenium` with ChromeDriver**: For web scraping the Yahoo Finance analysis page to retrieve growth and revenue estimates.
- **Pandas**: For reading, manipulating, and writing CSV data.
- **Regular Expressions (`re`)**: To extract specific patterns of text from the web-scraped content.

By following these steps, you gather key financial metrics for the companies in your list and save them into a structured comp table. For questions and updates please email me at [danieltian.yx@gmail.com](mailto:danieltian.yx@gmail.com).