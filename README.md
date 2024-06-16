# dpl
At work i need to submit my daily progress logs in a google sheet 

## Why build this
I find it very boring to login got to Google sheet and do it
## Tech Stack
Cli written in python using click and requests
and a google apps script
## How to use

First deploy the GAS script as a web app
Configure the cli to use the cli 
```
dpl -c URL
```

For that particular day 
```
dpl -t "hello" -r "from cmd" -e "done"
```