from typing import List, Dict
from src.insights.jobs import read

# retirei a solução da lista vazia deste endereço:
# https://pythonhelp.wordpress.com/2013/05/23/retirando-elementos-vazios-de-uma-lista/


def get_unique_industries(path: str) -> List[str]:
    unique_industries = read(path)
    industries_list = []
    for industries in unique_industries:
        industries_list.append(industries["industry"])
    return set(filter(None, industries_list))
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    raise NotImplementedError


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    return [
        industries for industries in jobs if industries["industry"] == industry
    ]
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    raise NotImplementedError
