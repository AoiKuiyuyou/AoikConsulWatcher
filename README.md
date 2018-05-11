# AoikConsulWatcher
Watch changes of Consul services and call a handler.

Tested woring with:
- Python 3.6.5, 2.7.14

Use cases:
- [AoikConsulWatcherHosts](https://github.com/AoiKuiyuyou/AoikConsulWatcherHosts)  
  Watch changes of Consul services and update hosts file.
- [AoikConsulWatcherNginx](https://github.com/AoiKuiyuyou/AoikConsulWatcherNginx)  
  Watch changes of Consul services and update Nginx config.

## Table of Contents
- [Setup](#setup)
  - [Setup via pip](#setup-via-pip)
  - [Setup via git](#setup-via-git)
- [Usage](#usage)
  - [Run program](#run-program)
  - [Specify config module](#specify-config-module)

## Setup
- [Setup via pip](#setup-via-pip)
- [Setup via git](#setup-via-git)

### Setup via pip
Run:
```
pip install AoikConsulWatcher
```
or:
```
pip install git+https://github.com/AoiKuiyuyou/AoikConsulWatcher
```

### Setup via git
Run:
```
git clone https://github.com/AoiKuiyuyou/AoikConsulWatcher

cd AoikConsulWatcher

python setup.py install
```

## Usage
- [Run program](#run-program)
- [Specify config module](#specify-config-module)

### Run program
Run:
```
aoikconsulwatcher
```
Or:
```
python -m aoikconsulwatcher
```
Or:
```
cd AoikConsulWatcher

python src/aoikconsulwatcher/__main__.py
```

### Specify config module
Config module specifies the Consul server to connect to, and the handler
`handle_service_infos` to be called on changes of Consul services.

An example config module is
[src/aoikconsulwatcher/config.py](/src/aoikconsulwatcher/config.py).

Create a config file:
```
cd AoikConsulWatcher

cp src/aoikconsulwatcher/config.py config.py 
```

Use the config file:
```
aoikconsulwatcher --config config.py
```
