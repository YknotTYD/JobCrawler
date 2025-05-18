import json

pass

job_template = {
    "locations": [
        {
            "city": None,
            "state": None,
            "country": None,
            "place_id": None,
            "sub_state": None,
            "formatted_address": None,
            "latitude": None,
            "longitude": None
        }
    ],
    "contract": {
        "type": {
            "original_label": None
        },
        "duration_min": None,
        "duration_max": None
    },
    "slug":
        None,
    "start_date":
        None,
    "title":
        None,
    "logo_url":
        None,
    "company_name":
        None
}

#logo_url company_name

with open("data.json", "r", encoding = "utf-8") as file:
    data = json.loads(file.read())

def parse_json_pages(data):

    for i in data["results"]:
        if i.get("hits"):
            return i.get("nbPages")
    return None

def parse_json(data):

    pages = None
    hits = None
    for i in data["results"]:
        if i.get("hits"):
            pages = i.get("nbPages")
            print(pages)
            hits = i.get("hits")
            break

    data = list(range(len(hits)))

    for i, hit in enumerate(hits):
        data[i] = job_template.copy()
        data[i]["locations"] = hit.get("locations")
        data[i]["contract"] = hit.get("contract")
        data[i]["slug"] = hit.get("slug")
        data[i]["title"] = hit.get("title")
        data[i]["start_date"] = hit.get("start_date")
        company = hit.get("company")
        if (company):
            data[i]["logo_url"] = company.get("logo_url")
            data[i]["company_name"] = company.get("name")

    return data

data = parse_json(data)

for line in data:
    print(line, end = "\n\n")