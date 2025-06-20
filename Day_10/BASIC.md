# Day 10

## Web scrapping

It is a process where we automatically exract usefull information from websites, This infromation can be stored in various formats such as databases, spreadsheets or even raw texts.

This allows for collectiosn fo large amount of fata rom the internet efficieny and quickly.

## Web crawling

Systematiclly browsing the web and downloading the websites, a web crawler is also known as web spider. It navigates from page to via links, indexing cntent for search engines.

## Use of web scrapping

1. **Market research** - Analyzing competitor pricing, product features, and market trends
2. **Content aggregation** - Collecting news articles, blog posts, and social media content
3. **Price monitoring** - Tracking product prices across e-commerce platforms for comparison
4. **Data analytics** - Gathering large datasets for statistical analysis and insights
5. **Research** - Academic and scientific data collection from various online sources
6. **Lead generation** - Extracting contact information and business details

## Components of a web scrapper

1. **HTML requests** - The scrapper send and HTTP request to the target website.
2. **HTML Parsing** - The scrapper parse the HTML to extract the desired data.
3. **Data Storage/ Transform data** - The extracted data is cleaned and transformed as needed.
    > Eg. CSV, MySQL, MongoDB, JSON files
4. **Scheduler** - Automating the scrapping process to run at specific intervals.

### Crawl

Use libraries like `requests` to send HTTP requests.

### Parse

Us elibraries like `BeautifulSoup(bs4)` to parse HTML content.

### Store

Store the data to a CSV file database or any other format.
