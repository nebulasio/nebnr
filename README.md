# nebnr
Nebulas Rank SDK

- Operating environment: Python3

- Install

    ```
    pip3 install nebnr
    ```

- Example:
    - Get nr data for all addresses of a day
        ```Python
        from nebnr.api import *

        nr_data = get_daily_all_nr('20180601')
        print(nr_data)
        ```
