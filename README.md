# SumuPoly

SumuPoly is a Django app used to obtain reports from the SumUp payment processor API, for AGEPoly the EPFL general students association.

## License

Not yet defined.

## Authors

Cedric Cook so far.

## Installation

### Package installation

`pip install git+https://github.com/CedricCook/sumupoly.git`

### Settings

Add to the end of your `settings.py` file:
```
SUMUPOLY_SUMUP_API_HOST = 'https://api.sumup.com/'
SUMUPOLY_SUMUP_CLIENT_ID = '' 
SUMUPOLY_SUMUP_CIENT_SECRET = ''
SUMUPOLY_URI_BASE = '' # Where sumupoly will be accessible on your server
SUMUPOLY_SUMUP_REDIRECT_URI = '' # MUST contain SUMUPOLY_URI_BASE.
```
### Urls

In your settings.py, add this to the url definitions:
```
url(r'^SUMUPOLY_URI_BASE/', include('sumupoly.urls')),
```

### Migrations

So far no migrations are necessary.


