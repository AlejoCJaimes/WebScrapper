import json


class UnstruscturedJson:
    def __init__(self, path):
        self._data = None
        self._label_list = []
        self._path = path

    def load_json(self):
        with open(f'{self._path}') as json_file:
            self._data = json.load(json_file)
            json_file.close()
        return self._data

    def search_pos_char(self, str, substring):
        list_pos = []
        pos = 0
        while pos != -1:
            pos = str.find(substring, pos)
            if pos != -1:
                list_pos.append(pos)
                pos += 1
        return list_pos

    def decoder_json(self, data, dict_json):
        list = []
        for key, value in dict_json.items():
            str_temp = data[key:value]
            str_temp = str_temp.replace('|', '')
            list.append(str_temp)
        return list

    def convert_json(self, data):
        s: str = data
        s = s.replace(data[0:3], '|')
        s = s.replace(',"', '|')
        s = s.replace('":', '*')
        sub_str_pipeline = self.search_pos_char(s, substring='|')
        sub_str_asterisk = self.search_pos_char(s, substring='*')
        dic_json = dict(zip(sub_str_pipeline, sub_str_asterisk))
        return dic_json, s

    @property
    def automated_convert_process(self):
        status = True
        try:
            self._data = self.load_json()
            dict_json = self.convert_json(self._data)
            self._label_list = self.decoder_json(dict_json[1],dict_json[0])

        except:
            status = False
        return self._label_list, status
