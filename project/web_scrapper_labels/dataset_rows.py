import requests
import re


class MaxRowData:
    def __init__(self):
        self._rows_dataset = None

    def RowsDataset(self, host):

        pattern = (r'\b.j.+')
        result = re.findall(pattern, host)
        hostid = host.replace("".join(result), '')
        response_up = requests.get(hostid)
        test_load = list(response_up.text.split("cachedContents"))
        self._rows_dataset = self.find_max_size(test_load[1::])
        return self._rows_dataset

    def find_max_size(self, test_load):

        list_cached_contents = []
        # list clean
        for xpression in test_load:
            pattern = (r'non_null.+\blargest*')
            result = re.findall(pattern, xpression)
            pattern2 = (r'.+\,')
            result2 = re.findall(pattern2, result[0])
            for x in result2:
                x = x.replace('"', '')
                x = x.replace("'", '')
                x = x.replace(",", '')
                list_cached_contents.append(x.split(':'))

        return self.find_list_max_size(list_cached_contents)

    def find_list_max_size(self, values):

        ls_max_size = []
        x = [ls_max_size.append(value[1]) for value in values]
        ls_max_size.reverse()
        return int(ls_max_size[0])
