import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin



def extract_by_label(li, label):
    for p in li.find_all("p"):
        b = p.find("b")
        if b and b.get_text(strip=True) == label:
            return p.get_text(strip=True).replace(label, "").strip()
    return None


def parse_page(html, BASE_URL):
    soup = BeautifulSoup(html, "html.parser")
    jobs = []

    for li in soup.select("li.das-search-results__list-item"):

        title_span = li.select_one("h2 a span[id$='-vacancy-title']")
        title = title_span.get_text(strip=True) if title_span else None
        vacancy_id = title_span["id"].replace("-vacancy-title", "") if title_span else None

        link_tag = li.select_one("a.das-search-results__link")
        url = urljoin(BASE_URL, link_tag["href"]) if link_tag else None

        employer_p = li.find("p", class_="govuk-body")
        employer = employer_p.get_text(strip=True) if employer_p else None


        location_p = li.find("p", class_="das-!-color-dark-grey")
        location = location_p.get_text(strip=True) if location_p else None

        distance = extract_by_label(li, "Distance")
        start_date = extract_by_label(li, "Start date")
        training_course = extract_by_label(li, "Training course")
        wage = extract_by_label(li, "Wage")

        closing_text = None
        for p in li.find_all("p"):
            if p.get_text(strip=True).startswith("Closes"):
                closing_text = p.get_text(strip=True)
                break

        posted_p = li.find("p", class_="govuk-!-font-size-16")
        posted_date = (
            posted_p.get_text(strip=True).replace("Posted", "").strip()
            if posted_p else None
        )

        disability_confident = bool(
            li.find("img", alt="Disability Confident")
        )

        jobs.append({
            "vacancy_id": vacancy_id,
            "title": title,
            "url": url,
            "employer": employer,
            "location": location,
            "distance": distance,
            "start_date": start_date,
            "training_course": training_course,
            "wage": wage,
            "closing_text": closing_text,
            "posted_date": posted_date,
            "disability_confident": disability_confident
        })

    next_page = None
    next_link = soup.select_one(".govuk-pagination__next a")
    if next_link:
        next_page = urljoin(BASE_URL, next_link["href"])

    return jobs, next_page


def scrape_all(BASE_URL, START_URL, HEADERS):
    all_jobs = []
    url = START_URL
    #print(f"Starting scrape at: {url}")
    count = 0
    while url:
        count += 1
        if count > 5:
            break
        print(f"Scraping: {url}")
        r = requests.get(url, headers=HEADERS, timeout=30)
        r.raise_for_status()

        jobs, url = parse_page(r.text, BASE_URL= BASE_URL)
        all_jobs.extend(jobs)

    return all_jobs



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
        'about_organization': '',
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


    req_section = soup.find("section", id="requirements")
    if req_section:
        edu_header = req_section.find("h3", string="Essential qualifications")
        if edu_header:
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

    # --- 3) About the organization ---
    company = soup.find('section', id='company')
    about_org = company.find('p')
    data['about_organization'] = about_org.get_text(strip=True) if about_org else ''

    return data


