Windows
```
python -m venv .env
.env/Scripts/Activate.ps1
python -m pip install -r requirements.txt
python -m pip install -e .
```


Linux - I think?
```
python -m venv .env
source .env/Scripts/Activate
python -m pip install -r requirements.txt
python -m pip install -e .
```

Install gcloud
```
https://cloud.google.com/sdk/docs/install
```

Make an account and get the api key - Easy - No card info
```
https://account.mapbox.com/auth/signup/
```

Create a file called `private.py` within the app directory.

Add the api key into `private.py` as ```KEY=API_KEY```


Install Node (LTS should work)
```
https://nodejs.org/en/
```

In one terminal start the python app
```
python app/google_earth.py
```

In another new terminal
```
cd node-app
npm install
npm run watch
```

Navigate to localhost:3000