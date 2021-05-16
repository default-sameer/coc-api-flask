from flask import Flask, url_for, render_template, request, flash, redirect
from flask.helpers import flash
import requests
import urllib.parse

app = Flask(__name__)
app.config['SECRET_KEY'] = 'TtNqvoYQX@6Fjr&@GT5pW!brWFSZ'

header = {
    'Accept': 'application/json',
    'authorization': 'Bearer token goes here'
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/clan", methods=['GET','POST'])
def clan():
    headers = header
    url = ('https://api.clashofclans.com/v1/clans/{}')
    if request.method == 'POST':
        query = request.form.get('search')
        clan_id = urllib.parse.quote(query)
        response = requests.get(url.format(clan_id), headers=headers)
        stats = response.json()
        status_code = response.status_code
        success = response.ok
        if status_code == 200:
            return render_template('clan.html', stats=stats, members=stats['memberList'])
        elif status_code == 400:
                flash('Please in include # and also check weather clan id is correct or incorrect ', 'info')
        elif status_code == 403:
            flash('Access denied, either because of missing/incorrect credentials', 'info')
        elif status_code == 404:
            flash('Clan Not Found', 'danger')
        elif status_code == 429:
            flash('Request was throttled,', 'info')
        elif status_code == 500:
            flash('Unknown error happened when handling the request.', 'info')
        elif status_code == 503:
            flash('Service is temprorarily unavailable because of maintenance', 'info')
        elif status_code == 0:
            flash('No Content Found on the server', 'info')
        else:
            flash('Clan Not Found', 'danger')
    else:
        render_template('search_clan.html')
    return render_template('search_clan.html')

@app.route('/player', methods=['GET', 'POST'])
def search_player():
    headers = header
    url = ('https://api.clashofclans.com/v1/players/{}')
    if request.method == 'POST':
        query = request.form.get('search')
        player_id = urllib.parse.quote(query)
        response = requests.get(url.format(player_id), headers=headers)
        stats = response.json()
        status_code = response.status_code
        success = response.ok
        if status_code == 200:
            return render_template('player.html', stats=stats, data=stats['achievements'])
        elif status_code == 400:
            flash('Please in include # and also check weather player id is correct or incorrect ', 'info')
        elif status_code == 403:
            flash('Access denied, either because of missing/incorrect credentials', 'info')
        elif status_code == 404:
            flash('Player Not Found', 'danger')
        elif status_code == 429:
            flash('Request was throttled,', 'info')
        elif status_code == 500:
            flash('Unknown error happened when handling the request.', 'info')
        elif status_code == 503:
            flash('Service is temprorarily unavailable because of maintenance', 'info')
        elif status_code == 0:
            flash('No Content Found on the server', 'info')
        else:
            flash('Player Not Found', 'danger')
    else:
        render_template('search_player.html')
    return render_template('search_player.html')

@app.route('/clans', methods=['GET', 'POST'])
def search_clan():
    headers = header
    url = ('https://api.clashofclans.com/v1/clans?name={}')
    if request.method == 'POST':
        clan_name = request.form.get('search')
        response = requests.get(url.format(clan_name), headers=headers)
        stats = response.json()
        status_code = response.status_code
        success = response.ok
        if status_code == 200:
            return render_template('clans.html', stats=stats['items'])
        elif status_code == 400:
            flash('Clan Not Found', 'info')
        elif status_code == 403:
            flash('Access denied, either because of missing/incorrect credentials', 'info')
        elif status_code == 404:
            flash('Clan Not Found', 'danger')
        elif status_code == 429:
            flash('Request was throttled,', 'info')
        elif status_code == 500:
            flash('Unknown error happened when handling the request.', 'info')
        elif status_code == 503:
            flash('Service is temprorarily unavailable because of maintenance', 'info')
        elif status_code == 0:
            flash('No Content Found on the server', 'info')
        else:
            flash('Clan Not Found', 'danger')
    else:
        render_template('search_clans.html')
    return render_template('search_clans.html')

if __name__ == '__main__':
    app.run(port=5000,debug=True)
