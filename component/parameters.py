# component/parameters.py

from urllib.parse import urlencode

hparams = {
    "BASE_URL": "https://www.findapprenticeship.service.gov.uk",
    "START_URL": "https://www.findapprenticeship.service.gov.uk/apprenticeships",
    "HEADERS": {
        "User-Agent": "Mozilla/5.0"
    }
}

def build_search_url(search_term: str, location: str, sort: str = "DistanceAsc", distance: str = "all") -> str:

    query_params = {
        "sort": sort,
        "searchTerm": search_term,
        "location": location,
        "distance": distance
    }
    return f"{hparams['START_URL']}?{urlencode(query_params)}"
