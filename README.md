# Flask template

## Prerequisites
```
sudo apt-get install python3 python3-venv python3-pip
python3 -m venv flask-template
source flask-template/bin/activate
pip3 install -r requirements.txt
```

## Development
* Run
    ```
	python3 src/main.py
    ```

* Test
    ```
    pylint src
    nosetests tests
    ```