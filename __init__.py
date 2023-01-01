from random import randrange
from time import time
import psutil
from functools import wraps, partial
from a_pandas_ex_automate_win32 import pd_add_automate_win32
import pandas as pd


def add_kill_selenium(f_py=None):

    assert callable(f_py) or f_py is None

    def _decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            killid = get_random_id()
            beforeselenium = get_all_pids()
            create_date = time()

            driver = func(*args, **kwargs)

            afterselenium = get_all_pids()
            aftercheck_ = objects_in_a_but_not_in_b(a=afterselenium, b=beforeselenium)
            driver._executelist = {
                "before": beforeselenium.copy(),
                "after": afterselenium.copy(),
                "aftercheck": aftercheck_.copy(),
            }
            driver._create_date = create_date
            driver._killid = killid
            return_date = time()
            driver._return_date = return_date
            driver.die_die_die_selenium = partial(_killfunction, driver)
            return driver

        return wrapper

    return _decorator(f_py) if callable(f_py) else _decorator


def get_all_pids():
    beforeselenium = []
    for p in psutil.pids():
        try:
            pro = psutil.Process(p)
            cmdline = pro.cmdline()
            beforeselenium.append((pro.pid, cmdline))
        except Exception as F:
            continue
    return beforeselenium


def get_random_id():
    random_number = str(randrange(1, 1000000000)).zfill(10)
    killid = f"--killid_{random_number}"
    return killid


def get_string_dict(nestedlist):
    tempstringlist = {}
    for ergi in nestedlist:
        tempstringlist[str(ergi)] = ergi
    askeys = [x for x in tempstringlist]

    return tempstringlist, askeys


def objects_in_a_but_not_in_b(a, b):
    a_, akeys = get_string_dict(a)
    b_, bkeys = get_string_dict(b)
    result = set(akeys) - set(bkeys)
    finallist = [a_[x] for x in list(result)]
    return finallist


def _killfunction(driver, soft_kill_first=False):
    if soft_kill_first:
        try:
            driver.close()
        except Exception:
            pass
        try:
            driver.quit()
        except Exception:
            pass

    pd_add_automate_win32()

    df = pd.Q_get_automate32_df()
    for k in df.loc[
        df.pid.isin([x[0] for x in driver.__dict__["_executelist"]["aftercheck"]])
    ].pid.to_list():
        try:
            p = psutil.Process(k)
            p.kill()
        except Exception:
            continue
