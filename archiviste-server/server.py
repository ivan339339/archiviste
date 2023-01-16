from flask import Flask

app = Flask(__name__)


@app.route("/members")
def members():
    return {
        "datasets": 
        [
            { 
            "name": "Common Crawl",
            "description": "We build and maintain an open repository of web crawl data that can be accessed and analyzed by anyone.",
            "owner": "STT"
            },
            { 
            "name": "Kazakh Speech Corpus",
            "description": "We present an open-source speech corpus for the Kazakh language. The Kazakh speech cor- pus (KSC) contains around 332 hours of tran- scribed audio comprising over 153,000 utter- ances spoken by participants from different re- gions and age groups, as well as both genders. It was carefully inspected by native Kazakh speakers to ensure high quality. The KSC is the largest publicly available database devel- oped to advance various Kazakh speech and language processing applications",
            "owner": "STT"
            }
        ]
    }


if __name__ == "__main__":
    app.run(debug=True)