from main import get_notMe, get_Me
import yaml
import requests

with open("config.yaml") as f:
    data = yaml.safe_load(f)


def test_1(login):
    res = get_notMe(login)
    lst = res["data"]
    lst_id = [el["id"] for el in lst]
    assert 78249 in lst_id, "тест провален"

"""Добавить в задание с REST API ещё один тест, в котором создаётся новый пост,
а потом проверяется его наличие на сервере по полю «описание».
Подсказка: создание поста выполняется запросом к https://test-stand.gb.ru/api/posts
с передачей параметров title, description, content.
"""
def test_create_post(login):
    response = requests.post(data["url_posts"],
                             headers={"X-Auth-Token": login},
                             data={'title': data["title"],
                                   'description': data["description"],
                                   'content': data["content"]})

    lst_description = [el["description"] for el in get_Me(login)["data"]]
    assert data["description"] in lst_description, "тест провален"