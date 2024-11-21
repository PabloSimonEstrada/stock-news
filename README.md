# Stock News Alert System

Stock News Alert System is a Python script that monitors stock price fluctuations and sends SMS alerts with the latest relevant news articles. The project uses APIs to track stock prices and gather news, ensuring users stay informed about significant market changes.

## Features

- **Stock Price Monitoring**: Tracks stock prices using the Alpha Vantage API.
- **News Integration**: Fetches relevant news articles related to significant price changes using the News API.
- **Threshold-Based Alerts**: Sends SMS notifications when stock prices fluctuate beyond a specified percentage.
- **SMS Notifications**: Uses Twilio API to deliver real-time alerts directly to the user.

## Technologies Used

- **Programming Language**: Python
- **APIs**:
  - Alpha Vantage API for stock price data.
  - News API for fetching relevant news articles.
  - Twilio API for sending SMS notifications.
- **Libraries**:
  - `requests` for API communication.
  - `datetime` for date and time handling.

## Setup and Installation

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/PabloSimonEstrada/stock-news.git
   cd stock-news
   ```

2. **Install Dependencies**  
   Ensure you have Python installed. Install required libraries using:
   ```bash
   pip install requests twilio
   ```

3. **Configure API Keys**  
   - Sign up and obtain API keys for:
     - [Alpha Vantage](https://www.alphavantage.co/)
     - [News API](https://newsapi.org/)
     - [Twilio](https://www.twilio.com/)
   - Open the script and update the following variables with your credentials:
     ```python
     ALPHA_VANTAGE_API_KEY = "your_alpha_vantage_api_key"
     NEWS_API_KEY = "your_news_api_key"
     TWILIO_ACCOUNT_SID = "your_twilio_account_sid"
     TWILIO_AUTH_TOKEN = "your_twilio_auth_token"
     FROM_PHONE_NUMBER = "your_twilio_phone_number"
     TO_PHONE_NUMBER = "your_phone_number"
     ```

4. **Run the Script**  
   Execute the script to monitor stock prices:
   ```bash
   python stock_news_alert.py
   ```

## Usage

1. **Set the Stock Symbol and Threshold**  
   - Modify the script to specify the stock symbol and percentage threshold for alerts:
     ```python
     STOCK_SYMBOL = "TSLA"
     THRESHOLD_PERCENTAGE = 5  # Example: Trigger alert for a 5% change
     ```

2. **Receive Alerts**  
   - When a significant price change is detected, the script will send an SMS like:
     ```
     TSLA: 🔺5.12%
     Latest News:
     Tesla releases Q3 results: profits soar!
     Read more: https://www.example.com/article
     ```

## Example Output

```bash
Checking stock prices...
Price change detected: +5.12%
Fetching news...
News fetched successfully.
SMS notification sent!
```

## Future Enhancements

- Add support for monitoring multiple stocks simultaneously.
- Implement email notifications as an alternative to SMS.
- Include advanced analytics for stock trends.

## Contribution

Contributions are welcome! Feel free to fork this repository, open issues, or submit pull requests
