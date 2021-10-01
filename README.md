# covid_project
- This project tracks and show the reports of Corona Virus status in real time visualization with graphs.
- I have used Python and Django for backend and JavaScript(Chart.js) for graphical represetation. 


## Run Locally


### Clone the project


```bash
  git clone https://github.com/puspita-sahoo/covid_project.git
```

### Create Environment

```bash
  python3 -m venv env_name
```
### Activate Environment(env)

```bash
  $ souce env/bin/activate
```


## Install all Dependencies


```bash
 $ pip3 install -r requrements.txt
```
## Database Migrations


```bash
 $ python3 manage.py makemigrations
 $ python3 manage.py migrate
```

## Create Super User


```bash
 $ python3 manage.py createsuperuser
```

## Run Server

```bash
$ python3 manage.py runserver
```
