---
applyTo: '**'
---
Coding standards, domain knowledge, and preferences that AI should follow.

1. **Tech Stack Guidance**
   - Prefer **Angular** for frontend development.
   - Use **Python** for backend scripting, web scraping (e.g., with `requests`, `BeautifulSoup`, `Selenium`, or `Scrapy`), and automation.
   - When suggesting or generating code, assume a **Node.js + Express** or **Flask** backend (based on Python if applicable).
   - Use **MongoDB** or **PostgreSQL** for storing articles or metadata from scraped sources.

2. **Code Style & Best Practices**
   - Follow **PEP8** style for Python code.
   - Use **async/await** when possible for asynchronous operations.
   - For Angular, prefer **TypeScript**, **RxJS** observables, and **modular components**.
   - Always include **comments** in complex logic or unfamiliar API usage.
   - Suggest **unit tests** where appropriate using `pytest` (Python) or `Jest` (TypeScript).

3. **Web Scraping Domain Knowledge**
   - Handle bot detection and rate limiting carefully. Add random delays and use headers that mimic browsers.
   - Detect and skip duplicate content based on article titles or URLs.
   - Extract and normalize article metadata like title, author, date, and source.
   - Where feasible, extract the **main content** without ads or sidebars.

4. **Project Preferences**
   - When generating articles or outputs, ensure factual accuracy and a **neutral, informative tone**.
   - Make the system **modular** to support plugins or pipelines for different content sources (e.g., RSS, static sites, APIs).
   - Prioritize **scalability** and **maintainability** of code over premature optimization.
   - Provide **clear logging and error handling** in all scripts.

5. **Future Integration Goals**
   - Prepare content for use in **static site generators** (e.g., Hugo or Next.js) or **CMS platforms** (like Ghost or WordPress).
   - Keep scraped content easy to export to **Markdown** or **HTML**.
   - Anticipate possible integration with **YouTube Shorts, TikTok captions**, or **auto-generated summaries** in the future.
