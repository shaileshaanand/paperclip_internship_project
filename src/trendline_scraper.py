import requests
from bs4 import BeautifulSoup

# We get a 403 Forbidden if User Agent is not set in the request
# We are using Firefox's User Agent here
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0'
}


def scrape(url: str) -> dict:
    """
    Returns a dict of the calender contents found on
    https://trendlyne.com/equity/calendar/ website in the following format:
    Note: "data" property is an array of event objects.
    {
        "data":[
            {
                "stock":"<Stock Name>",
                "date":"<Date>",
                "type":"<Event Type>",
            }
        ]
    }
    """

    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, 'html.parser')
    events = {"data": []}

    # The first row is the header row, so start from 2nd row below using "[1:]"
    for row in soup.select('tr')[1:]:
        cells = list(row.children)[:3]
        # Every stock cell in table has a "+" at the end and some may have \n
        # in between so we replave them and strip for trailing whitespaces.
        stock = cells[0].text.replace('\n', '').replace('+', '').strip()
        date = cells[1].text.strip()
        type = cells[2].text.strip()
        events["data"].append({
            "stock": stock,
            "date": date,
            "type": type
        })
    # print(len(events["data"]))
    return events


# print(scrape("https://trendlyne.com/equity/calendar/all/all/"))
# print(scrape("https://trendlyne.com/equity/calendar/all/all/?corporate_actions=Results"))
