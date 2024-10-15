#script to help me search for jobs
import requests
from bs4 import BeautifulSoup
import re

def search_job_postings():
    # URL of the search page
    url = "https://www.simplyhired.com/search?q=co-op&l="

    # Send an HTTP GET request to the URL
    response = requests.get(url)

    # Check if request was successful
    if response.status_code == 200:
        # Parse HTML content
        soup = BeautifulSoup(response.content, "html.parser")

        # Find all job postings
        job_postings = soup.find_all(class_="jobsearch-SerpJobCard")

        # Iterate through each job posting
        for posting in job_postings:
            # Extract the job title
            title = posting.find(class_="title").get_text()

            # Extract the job location
            location = posting.find(class_="location").get_text()

            # Check if the title contains "co-op" or "coop" (case insensitive)
            if re.search(r'co-?op', title, re.IGNORECASE):
                print("Title:", title.strip())
                print("Location:", location.strip())
                print("-" * 50)

    else:
        print("Failed to retrieve job postings.")

if __name__ == "__main__":
    search_job_postings()
