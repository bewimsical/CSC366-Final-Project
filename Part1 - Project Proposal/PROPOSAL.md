### Project Title: <br/>	
_How Do Online Reviews of Consumer Tech Products Correlate with Sales Performance?_

**Research Question**:	<br/>
Do customer ratings and review sentiment for consumer tech products (e.g., laptops, headphones, phones, smartwatches, etc.) have a measurable impact on their sales performance? We want to know do consumers heavily rely on reviews before making tech purchases. Do reviews or price have higher impact on competitive products.

### Data Sources (Messy Data Requirement): <br/>
**Amazon Product Advertising API**:
> (or scraping Walmart, BestBuy, Newegg, Amazon gives reviews, ratings, and metadata (number of reviews, star rating, etc.).

**Sales data proxies**:
> Amazon/Walmart Best Seller Ranks (BSR), which correlate with sales volume.
Monthly product rankings from BestBuy/Newegg (scrapable).

**Messiness**:
> Reviews are unstructured text → requires NLP preprocessing.
Sales ranks are indirect (need normalization).
Data must be merged across time and product categories.

