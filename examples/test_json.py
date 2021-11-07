import json

def load_json():
    with open('/home/alev/personalProjects/WebScrapper/examples/personal.json') as json_file:
        data = json.load(json_file)
        json_file.close()
    return data

def convert_json_manually(data):
    s: str = data
    s = s.replace(data[0:3], '|')
    s = s.replace(',"', '|')
    s = s.replace('":', '*')
    sub_str_pipeline = search_pos_char(s, substring='|')
    sub_str_asterisk = search_pos_char(s, substring='*')
    dic_json = dict(zip(sub_str_pipeline, sub_str_asterisk))
    return dic_json,s

def search_pos_char(str, substring):
	list_pos = []
	pos = 0
	while pos != -1:
		pos = str.find(substring, pos)
		if pos != -1:
			list_pos.append(pos)
			pos += 1
	return list_pos

def decoder_json(data, dict_json):
    list = []
    for key,value in dict_json.items():
        str_temp = data[key:value]
        str_temp = str_temp.replace('|','')
        list.append(str_temp)
    return list
    
if __name__ == '__main__':
    data = load_json()
    dict_json = convert_json_manually(data)
    labels_dataset =decoder_json(dict_json[1],dict_json[0])
    print(labels_dataset)