from functools import lru_cache
from typing import List, Dict

import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path) as csv_list:
        conteudos = csv.DictReader(csv_list)
        conteudos_list = []
        for valor in conteudos:
            conteudos_list.append(valor)

        return conteudos_list


# print(read("data/jobs.csv"))
# """Reads a file from a given path and returns its contents

# Parameters
# ----------
# path : str
#     Full path to file

# Returns
# -------
# list
#     List of rows as dicts
# """
# raise NotImplementedError


def get_unique_job_types(path: str) -> List[str]:
    unique_job = read(path)
    job_list = []
    for job in unique_job:
        job_list.append(job["job_type"])
    return set(job_list)
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    raise NotImplementedError


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    return [job for job in jobs if job["job_type"] == job_type]
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
