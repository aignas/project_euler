#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import click

from bs4 import BeautifulSoup
import requests

@click.command()
@click.argument('problem')
def get_euler_problem(problem):
    """Scrape data from the project euler project.
    """
    url_template = "https://projecteuler.net/problem={problem_number}"
    url = url_template.format(
        problem_number=problem)

    request = requests.get(url, verify=False)

    data = request.text

    soup = BeautifulSoup(data)
    content = soup.find("div", {"id": "content"})
    title = content.find("h2")
    problem_number = content.find("h3")
    problem = content.find("div", {"class": "problem_content"})

    from textwrap import TextWrapper

    wrapper = TextWrapper(
        width=79,
        initial_indent='    ',
        subsequent_indent='    ',)

    paragraphs = [i.string for i in problem.find_all('p')]

    try:
        problem_description = '\n\n'.join(
            ['\n'.join(wrapper.wrap(p)) for p in paragraphs])
    except:
        print(problem)
        raise

    description = (
        "    Project Euler solution\n\n"
        "    {problem_number}: {title}\n\n"
        "{problem_description}"
        .format(
            title=title.string,
            problem_number=problem_number.string,
            problem_description=problem_description))

    problem_template = '''
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
{description}
"""

def benchmark(func, *args, **kwargs):
    """A simple benchmark to check execution time of the code
    """
    from timeit import default_timer as timer

    start = timer()
    answer = func(*args, **kwargs)
    end = timer()
    print("Completed in: {{}}".format(end - start))
    return answer


def solution():
    """The solution to the problem
    """
    pass


def main():
    """The main function
    """
    # benchmark(solution)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
'''.format(description=description)

    print(problem_template)


if __name__ == "__main__":
    get_euler_problem()
