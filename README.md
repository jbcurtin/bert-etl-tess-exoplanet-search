# Bert ETL Simple Project

A very simple exmaple project about using [Bert ETL](https://bert-etl.readthedocs.io/en/latest/)

## Getting Started

( Documentation coming later )

```
$ virtualenv -p $(which python3) env
$ source env/bin/activate
$ pip install bert-etl -U
$ bert-example.py -n simple-project -d /tmp/bert-etl
$ docker run -p 6379:6379 -d redis

$ cd /tmp/bert-etl
$ bert-runner.py -m simple_project -f
```

### Running the example with `conda`

```
$ conda create --name bert-etl-simple-project python=3.7
$ conda activate bert-etl-simple-project
$ pip install bert-etl -U
$ bert-example.py -n simple-project -d /tmp/bert-etl
$ docker run -p 6379:6379 -d redis

$ cd /tmp/bert-etl
$ bert-runner.py -m simple_project -f
```

