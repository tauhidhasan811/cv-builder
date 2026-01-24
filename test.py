from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
"""
client = OpenAI()
"""

"""
audio_file = open("audio.mp3", "rb")

stream = client.audio.transcriptions.create(
  model="gpt-4o-mini-transcribe", 
  file=audio_file, 
  response_format="text",
  stream=True
)

for event in stream:
  print(event)
"""
"""

model = OpenAI().models

print(model)"""

"""from component.config.audio_model import OpenAIAudio

model = OpenAIAudio()
audio_path = "audio.mp3"

text = model.ConvertToText(audio_path=audio_path)

print(text)"""

"""from component.services.mocktest_prompt import MockTestPrompt

prompt = MockTestPrompt(domain_name="Law", topic_name = 'creminal', 
                        num_of_question="10", def_level='hard')
print(prompt)"""

"""import json

def is_valid_json(response_text):
    try:
        parsed = json.loads(response_text)
        return True, parsed
    except json.JSONDecodeError:
        return False, None

# Example usage:
response = '{"Result": "CORRECT", "Score": "90%", "Reason": "Answer is mostly correct"}'

valid, data = is_valid_json(response)
if valid:
    print("Valid JSON:", data)
else:
    print("Invalid JSON")
"""

"""import re

text = r'''
\[{\"question\": \"Explain the difference between word embeddings and one-hot encoding.\"}\]
```json
\bash
'''

# Step 1: Remove all literal backslashes
cleaned = text.replace("\\", "")

# Step 2: Remove backticks (` or ``` )
cleaned = re.sub(r"`{1,3}", "", cleaned)

# Step 3: Remove code language keywords (json, bash, python, etc.)
cleaned = re.sub(r'\b(json|bash|python)\b', '', cleaned, flags=re.IGNORECASE)

# Step 4: Remove newlines and extra spaces
cleaned = re.sub(r'\s+', ' ', cleaned).strip()

print(cleaned)"""

"""
from component.core.job_scrape import scrape_all
import component.parameters as hparams

BASE_URL = hparams.hparams["BASE_URL"]
HEADERS = hparams.hparams["HEADERS"]

# Build the dynamic search URL
START_URL = hparams.build_search_url(search_term="law", location="CM13 3JA")

# Now call the scraper
jobs = scrape_all(BASE_URL, START_URL, HEADERS)
print(f"Total jobs scraped: {len(jobs)}")


#data = scrape_all(BASE_URL = BASE_URL, START_URL=START_URL, HEADERS=HEADERS)
print(f"\nTotal jobs scraped: {len(jobs)}")
print(jobs)"""


### video to audio extract
"""import os
import time
import moviepy
import tempfile
from component.core.video_to_audio import ExtractAudio


path = 'Download.mp4'

with tempfile.TemporaryDirectory() as dir:
    f_name = 'output_audio.mp3'
    pth = os.path.join(dir, f_name)
    check = ExtractAudio(vdo_path=path, audio_path=pth)
    print(pth)

    time.sleep(60)"""

"""import component.parameters as hparams
from component.core.job_scrape import scrape_all
from component.core.clear_data import CleanData

x = {
        'job_posts': 
            ['Software Engineer', 'Backend Developer', 
             'C++ Developer', 'C#/.NET Developer', 'Systems Engineer', 
             'Desktop Application Developer', 'Full Stack Developer', 
             'Software Development Engineer', 'Product Engineer', 'Technical Project Lead'
             ]
    }

job_titles = x['job_posts']
print('*' * 100)
print(job_titles)
print('*' * 100)



BASE_URL = hparams.hparams["BASE_URL"]
HEADERS = hparams.hparams["HEADERS"]

job_post = []

for job in job_titles:
    START_URL = hparams.build_search_url(search_term=job, 
                                                location=" ")

    jobs = scrape_all(BASE_URL, START_URL, HEADERS)
    print('-' * 100)
    print(f"Jobs for {job}: {len(jobs)}")
    print('-' * 100)
    job_post.extend(jobs)

print('x' * 100)
print(f"Total jobs scraped: {len(job_post)}")
print('x' * 100)"""

"""
import requests
from bs4 import BeautifulSoup

def scrape_apprenticeship(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch page: {response.status_code}")

    soup = BeautifulSoup(response.text, "html.parser")

    data = {
        "work_full_text": "",
        "responsibilities": [],
        "skills": [],
        "education": []
    }

    # --- 1) Work / Responsibilities ---
    work_section = soup.find("section", id="work")
    if work_section:
        # get all paragraphs under "Work"
        paragraphs = work_section.find_all("p")
        data["work_full_text"] = "\n".join(p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True))

        # get all bullet items under "Work"
        for ul in work_section.find_all("ul"):
            for li in ul.find_all("li"):
                text = li.get_text(strip=True)
                if text:
                    data["responsibilities"].append(text)

    # --- 2) Education & Skills in Requirements ---
    req_section = soup.find("section", id="requirements")
    if req_section:
        # EDUCATION (Essential qualifications)
        edu_header = req_section.find("h3", string="Essential qualifications")
        if edu_header:
            # take all text until next subsection
            for sibling in edu_header.find_next_siblings():
                # stop if a new h3 starts
                if sibling.name == "h3":
                    break
                text = sibling.get_text(strip=True)
                if text:
                    data["education"].append(text)

        # SKILLS
        skills_header = req_section.find("h3", string="Skills")
        if skills_header:
            ul = skills_header.find_next("ul")
            if ul:
                data["skills"] = [li.get_text(strip=True) for li in ul.find_all("li")]

    return data


if __name__ == "__main__":
    url = "https://www.findapprenticeship.service.gov.uk/apprenticeship/VAC2000001965"
    info = scrape_apprenticeship(url)

    print("\n--- Work Full Text ---")
    print(info["work_full_text"])

    print("\n--- Responsibilities ---")
    for r in info["responsibilities"]:
        print("-", r)

    print("\n--- Skills ---")
    for s in info["skills"]:
        print("-", s)

    print("\n--- Education ---")
    for e in info["education"]:
        print("-", e)


"""

from bs4 import BeautifulSoup
import requests


header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"
}
url = 'https://www.findapprenticeship.service.gov.uk/apprenticeship/VAC2000001961'




#class_text = text.find('p', 'govuk-hint')
#all = text.find_all('p')
#print(all)
#print(class_text)

"""
for p in all:
    print(p.get_text())
"""



#print(about_org.text.strip())

#print(text.find('p'))


from component.core.job_scrape import scrape_apprenticeship

print('x' * 100)
print('Scraping apprenticeship details...')
print('x' * 100)

data = scrape_apprenticeship(url)
print(data)

