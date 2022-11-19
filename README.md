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