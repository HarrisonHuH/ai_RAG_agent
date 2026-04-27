import json

d = {
    "name": "周杰伦",
    "age": 11,
    "gender": "男"
}
s = json.dumps(d, ensure_ascii=False)
print(s)

l = [{
    "name": "周杰伦",
    "age": 11,
    "gender": "男"
    },
    {
    "name": "蔡依林",
    "age": 12,
    "gender": "女"
    },
    {
    "name": "小明",
    "age": 16,
    "gender": "男"
}]
s = json.dumps(l, ensure_ascii=False)
print(s)

json_str = '{"name": "周杰伦", "age": 11, "gender": "男"}'
json_array_str = '[{"name": "周杰伦", "age": 11, "gender": "男"}, {"name": "蔡依林", "age": 12, "gender": "女"}, {"name": "小明", "age": 16, "gender": "男"}]'

print(json.loads(json_str))
print(json.loads(json_array_str))

