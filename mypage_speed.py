import requests



api_key = 'YOUR_API_KEY'
url = 'https://mysite.com'



response = requests.get(f'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={url}&key={api_key}')
data = response.json()

print('Speed Score:', data['lighthouseResult']['categories']['performance']['score'] * 100)
