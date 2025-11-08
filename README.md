# Product Reviews Scraper

A small Python script to scrape product reviews from a webpage using `requests` and `BeautifulSoup`.

> **Warning:** Web scraping should respect a website's `robots.txt` and Terms of Service. Only scrape websites you have permission to access and avoid making excessive requests.

---

## Features

* Fetches HTML content using `requests`.
* Parses reviews using `BeautifulSoup`.
* Returns a list of review text strings.

---

## Files

* `main.py` — The main script that demonstrates fetching and parsing product reviews.

---

## Requirements

* Python 3.8+
* `requests`
* `beautifulsoup4`

Install dependencies with pip:

```bash
pip install -r requirements.txt
# or
pip install requests beautifulsoup4
```

---

## Usage

1. Update the `url` variable in `main.py` to the reviews page you want to scrape.
2. Adjust the parsing logic inside `get_product_reviews` to match the HTML structure of the target site.

Example run:

```bash
python main.py
```

The script will print a Python list of extracted review strings.

---

## How to customize the parser

The example parser in `main.py` looks for elements with `div` and `class="review"`. Most sites have different markup. To adapt:

* Inspect the page in your browser (right-click → Inspect).
* Find the HTML element that contains each review (e.g., `div.review`, `div[data-review-id]`, `span.a-size-base` etc.).
* Update the `soup.find_all(...)` selector and the code that extracts the text (e.g., `.get_text(strip=True)`, `.text.strip()`, or `.find('p').text`).

Example:

```python
for review in soup.find_all('div', class_='review'):
    review_text = review.get_text(strip=True)
    reviews.append(review_text)
```

---

## Improvements & TODO

* Add error handling for network issues and invalid responses.
* Respect rate limits and add delays between requests (`time.sleep`) or use a session with retries.
* Use headers and rotating user-agents / proxies if scraping many pages (respect site rules).
* Save results to a CSV/JSON file.
* Add CLI arguments (e.g., `--url`, `--output`) or turn into a reusable package.
* Consider using APIs or official endpoints if available.

---

## Troubleshooting

* **No reviews found:** The selectors are likely incorrect. Inspect the website's HTML and adjust selectors accordingly.
* **Blocked or 403 responses:** The site may block scraping. Check `robots.txt` and TOS. Try adding `headers={'User-Agent': 'Mozilla/5.0'}` or reduce request frequency.
* **`requests` errors:** Ensure you have an active internet connection and the URL is correct.

---

## License

This project is provided under the MIT License. See `LICENSE` (not included) for details.

---

## Contact

If you want help adapting the parser to a specific website, paste the target page's HTML snippet (the review block) and I can help update the selectors.
