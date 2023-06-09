from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    salary_list = read(path)
    return max(
        [
            int(salary["max_salary"])
            for salary in salary_list
            if (salary["max_salary"]).isdigit()
        ]
    )
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """


def get_min_salary(path: str) -> int:
    salary_list = read(path)
    return min(
        [
            int(salary["min_salary"])
            for salary in salary_list
            if (salary["min_salary"]).isdigit()
        ]
    )

    """Get the minimum salary of all jobs
    Must call `read`
    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    if (
        "min_salary" not in job or "max_salary" not in job
    ):
        raise ValueError
    if (
        not str(job["max_salary"]).isdigit()
        or not str(job["min_salary"]).isdigit()
    ):
        raise ValueError
    if (
        int(job["min_salary"]) > int(job["max_salary"])
        or not str(salary).lstrip('-').isdigit()
    ):
        raise ValueError

    return int(job["min_salary"]) <= int(salary) <= int(job["max_salary"])
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    raise NotImplementedError


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:

    jobs_list = []

    for job in jobs:
        try:
            if (matches_salary_range(job, salary)):
                jobs_list.append(job)
        except ValueError:
            print(ValueError)
    return jobs_list
    # """Filters a list of jobs by salary range

    # Parameters
    # ----------
    # jobs : list
    #     The jobs to be filtered
    # salary : int
    #     The salary to be used as filter

    # Returns
    # -------
    # list
    #     Jobs whose salary range contains `salary`
    # """
    # raise NotImplementedError
