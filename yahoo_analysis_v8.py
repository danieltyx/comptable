import pandas as pd
import yfinance as yf
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import re


def convert_to_percentage(growth_estimate):
    if "%" in growth_estimate:
        growth_estimate = growth_estimate.replace("%", "")
    # Convert to float and format to one decimal place
    percentage = float(growth_estimate)
    return round(percentage, 1)


def extract_data(text):
    growth_estimate_match = re.search(r'Next 5 Years \(per annum\)\s+([\d.]+%)', text)
    growth_estimate = growth_estimate_match.group(1) if growth_estimate_match else None
    
    # Extract the revenue estimatesu
    pattern = r'Avg\. Estimate\s+((?:[\d,.]+[MKB]\s*)+)'
    match = re.search(pattern, text)
    
    revenue_estimate = None
    numbers = []

    if match:
    
        numbers_str = match.group(1)
        numbers = re.findall(r'[\d,.]+[MKB]', numbers_str)
        
        if len(numbers) >= 2:
            revenue_estimate = numbers[-2]  # Get the second last number
        
    else:
        print("No matches found.")
    
    return growth_estimate, revenue_estimate

# Initialize the WebDriver with options
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless") 
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

file_path = '/Users/danieltian/Desktop/Appleby/FTC3_test.csv'  
data = pd.read_csv(file_path)

data['Ticker'] = data['Ticker'].astype(str)

# Create columns for new data
data['Revenue'] = None
data['trailingPE'] = None
data['trailingEps'] = None
data['52WeekChange'] = None
data['Growth Est 5Yrs'] = None
data['Revenue Estimate'] = None

# Iterate over each ticker
for i, ticker in enumerate(data['Ticker']):
    if ticker and ticker != 'nan':
        # Fetch data using yfinance
        stock = yf.Ticker(ticker)
        total_revenue = stock.info.get('totalRevenue', 'N/A')
        trailing_pe = stock.info.get('trailingPE', 'N/A')
        trailing_eps = stock.info.get('trailingEps', 'N/A')
        week_change = stock.info.get('52WeekChange', 'N/A')
        price = stock.info.get('previousClose', 'N/A')
        currency = stock.info.get('currency', 'N/A')    
        total_revenue_res = ''
        if total_revenue != 'N/A':
            total_revenue = float(total_revenue)
            if total_revenue >= 1000000000:
                total_revenue_res = '{:.2f}B'.format(total_revenue / 1000000000)
            else:
                total_revenue_res = '{:.2f}M'.format(total_revenue / 1000000)

        if trailing_pe != 'N/A':
            trailing_pe = int(trailing_pe)
        if week_change != 'N/A':
            week_change = int(week_change * 100) 
        if price != 'N/A':
            price = price
        if currency != 'N/A':
            currency = currency
        
        data.at[i, 'Revenue'] = total_revenue_res
        data.at[i, 'trailingPE'] = trailing_pe
        data.at[i, 'trailingEps'] = trailing_eps  
        data.at[i, '52WeekChange'] = week_change
        data.at[i, 'Price'] = price
        data.at[i, 'Currency'] = currency

        url = f"https://finance.yahoo.com/quote/{ticker}/analysis/"
        driver.get(url)

        driver.implicitly_wait(10)

        try:
            content = driver.find_element(By.TAG_NAME, 'body')
            res = content.text
            growth_estimate, revenue_estimate = extract_data(res)
            growth_estimate_res = str(convert_to_percentage(growth_estimate)) + '%'
            data.at[i, 'Growth Est 5Yrs'] = growth_estimate_res
            data.at[i, 'Revenue Estimate'] = revenue_estimate
        except Exception as e:
            print(f"Error extracting data for {ticker}: {e}")
        
       
        output_file_path = 'yahoo_FT2_results_v3.csv'
        data.to_csv(output_file_path, index=False)


driver.quit()

print(f"Updated data saved to {output_file_path}")
