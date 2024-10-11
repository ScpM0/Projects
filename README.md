### README for Job Scraping Script

# Job Scraping Script

This Python script scrapes job listings from **Wuzzuf** based on a target job keyword, extracting useful information about the job title, company, location, skills required, and links to the individual job postings. The collected data is then exported to a CSV file for further analysis or use.

## Features

- **Web Scraping**: The script scrapes job listings from [Wuzzuf](https://wuzzuf.net/).
- **Custom Search**: You can enter a job keyword, and the script will search for relevant jobs based on that keyword.
- **Data Extraction**: Extracts key job-related information such as:
  - Job title
  - Company name
  - Location
  - Skills required
  - Job listing link
- **CSV Export**: All the extracted data is saved in a CSV file for easy access and further processing.

## Prerequisites

Before running this script, ensure you have the following Python libraries installed:

- `requests`
- `BeautifulSoup4` (from `bs4`)
- `lxml`
- `csv`

To install the required libraries, run:

```bash
pip install requests beautifulsoup4 lxml
```

## Usage

1. Clone or download the repository to your local machine.
2. Open a terminal or command prompt.
3. Run the Python script by executing:

```bash
python job_scraper.py
```

4. When prompted, enter the **target job keyword** (e.g., "Data Scientist", "Software Engineer", etc.).
   
   Example input:
   ```
   Please Enter Target Job: Software Engineer
   ```

5. The script will search for jobs on Wuzzuf, scrape the relevant information, and save it to a file named `Jobs.csv`.

   The CSV file will contain the following columns:
   - **Job Title**
   - **Company Name**
   - **Location**
   - **Job Skills**
   - **Links**

## Example Output (CSV)

| Job Title        | Company Name   | Location  | Job Skills   | Links                                      |
|------------------|----------------|-----------|--------------|--------------------------------------------|
| Data Scientist   | XYZ Corp       | Cairo     | Python, SQL  | [Link](https://wuzzuf.net/jobs/12345)      |
| Software Engineer| ABC Inc.       | Alexandria| Java, Spring | [Link](https://wuzzuf.net/jobs/67890)      |

## Notes

- The script works by scraping job data from **Wuzzuf**, a popular job listing website in Egypt.
- The output CSV file is saved to the directory where the script is run, or you can specify the path as required (modify the path in the script).
- The script is designed to work with **Wuzzuf's current webpage structure**. If the website structure changes, the script may need to be updated.

## Troubleshooting

- **Empty or Missing Data**: If some jobs have missing data (e.g., job title or skills), it might be due to changes in the website structure. Inspect the HTML structure to check for any changes in class names or elements.
- **No Jobs Found**: Ensure that the job keyword you're searching for has available listings on Wuzzuf. If the keyword returns no results, the script may not output any data.

## License

This project is open-source and available under the MIT License.

---

Feel free to modify and improve the script to suit your needs!
