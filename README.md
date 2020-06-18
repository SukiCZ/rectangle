# Rectangles

## Install
```shell script
git clone https://github.com/SukiCZ/rectangle.git
cd rectangle/
mkvirtualenv -p python3.7 -a . suki-rectangle
python -m cli --help
```

## Run
```shell script
python -m cli -v
```

## Input
```text
14
1.0 1.0 10.0 6.0
1.5 1.5 6.0 5.0
2.0 2.0 3.0 3.0
2.0 3.5 3.0 4.5
3.5 2.0 5.5 4.5
4.0 3.5 5.0 4.0
4.0 2.5 5.0 3.0
7.0 3.0 9.5 5.5
7.5 4.0 8.0 5.0
8.5 3.5 9.0 4.5
3.0 7.0 8.0 10.0
5.0 7.5 7.5 9.5
5.5 8.0 6.0 9.0
6.5 8.0 7.0 9.0
```

## Output
```text
9
```

## Test
```shell script
pip install coverage
coverage run -m unittest
coverage report -m
```

## Syntax check
```shell script
pip install flake8
flake8 .
```

## Have fun
[Kuba](https://www.suki.wtf)
