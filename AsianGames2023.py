from flask import Flask, jsonify
import requests
import lxml.html as lh
import pandas as pd
import json

app = Flask(__name__)

# Load the configuration from config.json
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

@app.route('/api/medal-standings')
def get_medal_standings():
    url = config.get('medal_standings_url')
    if not url:
        return jsonify({'error': 'URL not found in the configuration'}), 500

    page = requests.get(url)
    doc = lh.fromstring(page.content)
    tr_elements = doc.xpath('//tr')
    tr_elements = doc.xpath('//tr')
    col = []
    i = 0
    j = 0
    medal = ['Gold', 'Silver', 'Bronze']
    for t in tr_elements[0]:
        i += 1
        name = t.text_content()

        if str(name) == '\r\r':
            name = medal[j]
            j += 1

        name = name.replace("\r", "")
        col.append((name, []))

    for j in range(1, len(tr_elements)):
        T = tr_elements[j]
        if len(T) != len(col):
            break
        i = 0
        for t in T.iterchildren():
            data = t.text_content()
            data = str(data).replace("\r", "")
            if i > 0:
                try:
                    data = int(data)
                except:
                    pass
            col[i][1].append(data)
            i += 1

    Dict = {title: column for (title, column) in col}
    df = pd.DataFrame(Dict)

    return df.to_json(orient='records')

if __name__ == '__main__':
    app.run(debug=True)
