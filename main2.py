import requests
from bs4 import BeautifulSoup

base = "https://remote.co"
URL = base + "/remote-jobs/developer/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find("div",class_="card bg-white m-0")
# results = soup.find("div", class_="jobsearch-InlineResumePromo css-12lrs3m eu4oa1w0")

# print(results.prettify())

all_jobs = results.find_all("span", string= lambda text:"frontend" in text.lower())

job_elements = [
    job_element.parent.parent.parent.parent.parent.parent for job_element in all_jobs
]

for jobs in job_elements:
    title = jobs.find("span", class_="font-weight-bold larger")
    date = jobs.find("date")
    time = jobs.find("p", class_="m-0 text-secondary")
    text_secondary = time.find_all("small")
    texts = [
        text.text for text in text_secondary
    ]
    url = jobs["href"]
    print(base+url)
    print(title.text.strip())
    print(date.text.strip())
    print(texts)
    print()