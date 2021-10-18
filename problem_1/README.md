
## Requirements

* python 3.9
* pytest

Important. Please wrap all strings passed via command line in single quotes.

> python json_parser.py '{"key":"value"}'
>
> True
>
> python json_parser.py '{"key":["a","4",5]}'
>
> True

## Running tests

* Download pytest via pip ie: pip install pytest

> pytest
>
> test session starts ==========================================================
>
> platform darwin -- Python 3.9.7, pytest-6.2.5, py-1.10.0, pluggy-1.0.0
>
> rootdir: /Users/luisrueda/scripts/ltx_qa/problem_1
>
> collected 27 items
> 
> test_json.py ...............                                                                                                      [ 55%]
>
> test_json_simple.py ............                                                                                                  [100%]
>
> 27 passed in 0.04s ===========================================================
