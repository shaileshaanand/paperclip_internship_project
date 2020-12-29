from flask import Flask, jsonify
from trendline_scraper import scrape


app = Flask(__name__)


@app.route('/api/all')
def get_all():
    return jsonify(scrape('https://trendlyne.com/equity/calendar/all/all/'))


@app.route('/api/bonus_split')
def get_bonus_split():
    return jsonify(scrape('https://trendlyne.com/equity/calendar/all/all/?corporate_actions=Bonus%2FSplit'))


@app.route('/api/dividend')
def get_dividend():
    return jsonify(scrape('https://trendlyne.com/equity/calendar/all/all/?corporate_actions=Dividends'))


@app.route('/api/board_meetings')
def get_board_meetings():
    return jsonify(scrape('https://trendlyne.com/equity/calendar/all/all/?corporate_actions=Board+Meetings'))


@app.route('/api/results')
def get_results():
    return jsonify(scrape('https://trendlyne.com/equity/calendar/all/all/?corporate_actions=Results'))


@app.route('/')
def root():
    return("""
    <!DOCTYPE html>
<html lang="en">

<head>
    <title>Trendline Scraper</title>
</head>

<body>
    <h1>Trendline Scraper API</h1>
    <p>
        Available Endpoints:
    <ul>
        <li><a href="api/all">/api/all</a></li>
        <li><a href="api/bonus_split">/api/bonus_split</a></li>
        <li><a href="api/dividend">/api/dividend</a></li>
        <li><a href="api/board_meetings">/api/board_meetings</a></li>
        <li><a href="api/results">/api/results</a></li>
    </ul>
    </p>
</body>

</html>""")


def main():
    app.run(threaded=True, port=5000)


if __name__ == "__main__":
    main()
