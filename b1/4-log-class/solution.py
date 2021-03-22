from io import StringIO
import re
import time
import ipaddress


class LogDicts:
    def __init__(self, logfilename: str):
        self.logfilename = logfilename
        self.logfile = get_log_file(logfilename)

    def dicts(self, key=None) -> list:
        return (
            sorted(re_logtolist(self.logfile), key=key)
            if key
            else re_logtolist(self.logfile)
        )

    def iterdicts(self, key=None) -> iter:
        return (
            sorted(iter(re_logtolist(self.logfile)), key=key)
            if key
            else iter(re_logtolist(self.logfile))
        )

    def earliest(self, key=None) -> dict:
        earliest_time = None
        earliest_dict = {}
        for log_dict in self.dicts():
            log_time = time.strptime(
                log_dict.get("timestamp"), "%d/%b/%Y:%H:%M:%S +0200"
            )
            if not earliest_time or log_time < earliest_time:
                earliest_time = log_time
                earliest_dict = log_dict
        return sorted(earliest_dict, key=key) if key else earliest_dict

    def latest(self, key=None) -> dict:
        latest_time = None
        latest_dict = {}
        for log_dict in self.iterdicts():
            log_time = time.strptime(
                log_dict.get("timestamp"), "%d/%b/%Y:%H:%M:%S +0200"
            )
            if not latest_time or log_time > latest_time:
                latest_time = log_time
                latest_dict = log_dict
        return sorted(latest_dict, key=key) if key else latest_dict

    def for_ip(self, ip_address, key=None) -> list:
        ip = ipaddress.ip_address(ip_address)
        filter_logs = []
        for log_dict in self.iterdicts():
            log_ip = ipaddress.ip_address(log_dict.get("ip_address"))
            if ip == log_ip:
                filter_logs.append(log_dict)
        return sorted(filter_logs, key=key) if key else filter_logs

    def for_request(self, text, key=None) -> list:
        filter_logs = []
        for log_dict in self.iterdicts():
            if text in log_dict.get("request"):
                filter_logs.append(log_dict)
        return sorted(filter_logs, key=key) if key else filter_logs


def re_logtolist(data) -> list:
    parsed_content = []
    pattern = '^(?P<ip_address>(?:[0-9]{1,3}\.){3}[0-9]{1,3}).+\[(?P<timestamp>.+)\].+"(?P<request>GET.+?)".+$'

    for line in StringIO(data):
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


def get_log_file(fname):
    """
    Retrieve the log file data.
    """
    with open(fname) as f:
        return f.read()


if __name__ == "__main__":
    import operator

    ld = LogDicts("mini-access-log.txt")
    print(len(ld.earliest()))
    sorted_ld = ld.dicts(key=operator.itemgetter("timestamp"))

    print(len(sorted_ld))
