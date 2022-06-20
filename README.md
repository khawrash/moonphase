# moonphase

## Developers

### Python Developer Environment Setup
* Setup a Pipfile
* Ran...
```
pipenv install
pipenv install --dev
```

### Enter Development Environment

```
pipenv shell
```

### Deploy
* Setup
```
# Install heroku cli
heroku login
heroku git:remote -a moonphaseapi # in the git repo of your app
```

* Deploy
```
git add -A
git commit "your message"
git push heroku master
```



