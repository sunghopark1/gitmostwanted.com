[![wercker status](https://app.wercker.com/status/7767a5325ebf378ede0ac3016c992ebc/s/master "wercker status")](https://app.wercker.com/project/bykey/7767a5325ebf378ede0ac3016c992ebc)
[![Code Climate](https://codeclimate.com/github/kkamkou/gitmostwanted.com/badges/gpa.svg)](https://codeclimate.com/github/kkamkou/gitmostwanted.com)
[![Coverage Status](https://coveralls.io/repos/kkamkou/gitmostwanted.com/badge.svg?branch=HEAD&service=github)](https://coveralls.io/github/kkamkou/gitmostwanted.com?branch=HEAD)

# gitmostwanted
Advanced explorer of github.com. The main goal is to highlight the most interesting repositories and exclude others. You can find some concepts in the [Wiki](https://github.com/kkamkou/gitmostwanted.com/wiki).

## Donation
If you would like to help the project, please consider these topics:
- GMW uses [Google BigQuery](https://cloud.google.com/bigquery/pricing) and the service is pretty expensive.
- GMW is located on a private machine and hosted by [ProfitBricks](https://www.profitbricks.de/).

## Run (Python3)

```bash
# export PYTHONPATH="`pwd`:${PYTHONPATH}"
export GMW_APP_SETTINGS=/path/to/instance.cfg
python gitmostwanted/web.py
```

## Tests

```bash
py.test --pep8 --clearcache --cov gitmostwanted tests/unit
```

## Docker
The first time [it'll fail](https://github.com/docker/compose/issues/374)

```bash
cp instance.cfg.distr instance.cfg
[sudo] docker-compose up -d
# open http://127.0.0.1:5000/ in your browser
```

## Contribution
- Fork this repo
- Modify the source code and create a Pull Request
- Please, follow [these code standards](https://github.com/amontalenti/elements-of-python-style)

## License
The MIT License (MIT)

Copyright (c) 2015-2016 Kanstantsin Kamkou <2ka.by>
