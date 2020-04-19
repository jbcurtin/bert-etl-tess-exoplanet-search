# Bert ETL TESS Exoplanet Search

( Details to come; stubed git-repo )

[Bert ETL](https://bert-etl.readthedocs.io/en/latest/)

## Getting Started

( Documentation coming later )

```
$ virtualenv -p $(which python3) env
$ source env/bin/activate
$ pip install bert-etl -U
$ bert-example.py -n tess-exoplanet-search
$ docker run -p 6379:6379 -d redis

$ cd /tmp/tess-exoplanet-search/
$ bert-runner.py -m tess_exoplanet_search -f
```

### Running the example with `conda`

```
$ conda create --name bert-etl-tess-exoplanet-search python=3.7
$ conda activate bert-etl-tess-exoplanet-search
$ pip install bert-etl -U
$ bert-example.py -n tess-exoplanet-search
$ docker run -p 6379:6379 -d redis

$ cd /tmp/tess-exoplanet-search/
$ bert-runner.py -m tess_exoplanet_search -f
```

