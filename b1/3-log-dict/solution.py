# Exercise 3: Read log file into a dict
# Date 13-03-21
# Author: Paddy Kelly
# Python: 3.8.5
from urllib.request import urlopen
import re
import io


def get_log_file(fname: str):
    """
    Retrieve the log file data.
    """
    _URL = "https://gist.github.com/reuven/5875971/raw/0f20d30d9457c1ded3c6c82798946afaf0b82292/mini-access-log.txt"

    if fname.startswith(("https:", "http:", "ftp:")):
        url = urlopen(fname)
        return io.TextIOWrapper(url, encoding="utf-8")
    with open(fname) as f:
        return f.read()


def re_logtolist(data: io.StringIO) -> list:
    """
    Parse a log file into a list of dicts. Each file in the file is a dict object
    parsed based on a regex.

    Args:
        data (str): .

    Returns:
        list: each line parsed into a dict.
    """
    parsed_content = []
    pattern = '^(?P<ip_address>(?:[0-9]{1,3}\.){3}[0-9]{1,3}).+\[(?P<timestamp>.+)\].+"(?P<request>GET.+?)".+$'

    for line in data:
        match = re.match(pattern, line)
        if match:
            parsed_content.append(match.groupdict())
        else:
            parsed_content.append(
                dict(
                    ip_address="No IP address found",
                    timestamp="No timestamp found",
                    request="No request found",
                )
            )
    return parsed_content


def logtolist(data: str) -> list:
    """
    Parse a log file into a list of dicts. Each file in the file is a dict object
    parsed based on a regex.

    Args:
        data (str): name of file to parse.

    Returns:
        list: each line parsed into a dict.
    """
    pattern = '^(?P<ip_address>(?:[0-9]{1,3}\.){3}[0-9]{1,3}).+\[(?P<timestamp>.+)\].+"(?P<request>GET.+?)".+$'
    # data = get_log_file(fname)
    parsed_content = []
    pattern = '^(?P<ip_address>(?:[0-9]{1,3}\.){3}[0-9]{1,3}).+\[(?P<timestamp>.+)\].+"(?P<request>GET.+?)".+$'

    for line in data:
        match = re.match(pattern, line)
        if match:
            parsed_content.append(match.groupdict())
        else:
            parsed_content.append(line)
    return parsed_content


if __name__ == "__main__":
    _URL = "https://gist.github.com/reuven/5875971/raw/0f20d30d9457c1ded3c6c82798946afaf0b82292/mini-access-log.txt"
    logtolist(_URL)