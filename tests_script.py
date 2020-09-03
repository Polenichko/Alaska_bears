import pytest
from api import Restful

host = 'http://localhost:32768'


def create_new(type_b, name, age):
    parametrs = [type_b, name.upper(), age]
    list_r = ['None', 'None', 'None', 'None']

    # format param
    param_dict = Parametrs_bear().param(type_b, name, age)

    # create new
    res = Restful(host).create_new_bear(param_dict)
    res_stat = res.status_code

    list_r[3] = str(res_stat)
    if res_stat != 500:
        created_id = int(res.content)
        print('id new objeckt: ', created_id,'the collected parameters: ', param_dict, \
              'status_code: ',res_stat)

        # check type created obj
        res = Restful(host).read_bear(created_id)
        l_p = ["bear_type", "bear_name", "bear_age"]
        for i in range(3):
            if res.json() != None:
                par = res.json()[l_p[i]]
            else:
                par = 'None'
            list_r[i] = par
            print('parametr_ecxpect: ', parametrs[i], ' << == >> parametr_fuct:', par)

    print('parametrs fron testing objekt :',list_r)
    return list_r


def create_one():
    param_dict = Parametrs_bear().param('POLAR', 'mihail', 17.5)
    # create new
    res = Restful(host).create_new_bear(param_dict)
    return int(res.content)


def update(type_b, name, age, created_id):
    parametrs = [type_b, name.upper(), age]
    list_r = ['None', 'None', 'None', 'None']

    # format param
    param_dict = Parametrs_bear().param(type_b, name, age)

    # update param
    res = Restful(host).update_bear(created_id, param_dict)
    list_r[3] = str(res.status_code)

    # check update
    res = Restful(host).read_bear(created_id)
    l_p = ["bear_type", "bear_name", "bear_age"]
    for i in range(3):
        if res.json() != None:
            par = res.json()[l_p[i]]
        else:
            par = 'None'
        list_r[i] = par
        print('parametr_ecxpect: ', parametrs[i], ' << == >> parametr_fuct:', par)

    print('parametrs fron testing objekt :', list_r)
    return list_r


def test_dellete_one():
    param = Parametrs_bear().param('POLAR', 'mihail', 17.5)
    # create new
    res = Restful(host).create_new_bear(param)
    created_id = int(res.content)
    print('created_id :', created_id, ' ', param, ' ', res.status_code)
    # dell by id
    Restful(host).dell_bear(created_id)
    # check odj by id dellete
    res = Restful(host).read_bear(created_id)
    assert res.content == b'EMPTY'


class Parametrs_bear:
    def param(self, type_b, name, age):
        param_dict = {"bear_type": type_b, "bear_name": name, "bear_age": age}
        return param_dict


@pytest.mark.parametrize("type_b , name, age, res",
                         [
                             ('POLAR', 'mihail', 17.5, '200'),
                             ('BROWN', 'mihail', 17.5, '200'),
                             ('BLACK', 'mihail', 17.5, '200'),
                             ('GUMMY', 'mihail', 17.5, '200'),
                             ('', 'mihail', 17.5, '500'),
                             ('BROWN', '', 17.5, '500'),
                             ('BLACK', 'mihail', '', '500'),
                             ('BLACK', 'mihail', 0, '200'),
                             ('black', 'mihail', 10, '500'),
                             ('white', 'mihail', 10, '500'),
                             (0, 'mihail', 10, '500'),
                             ('BLACK', 'm' * 100, 10, '200'),
                             ('BLACK', 'm' * 1000, 10, '200'),
                             ('BLACK', 'mihail', -0.1, '200'),
                             ('BLACK', 'mihail', 200, '500'),

                         ]
                         )
def test_create(type_b, name, age, res):
    l_res = create_new(type_b, name, age)
    n_res = l_res[3]
    if age != '' and age < 0:
        age = 0

    assert res in n_res
    if n_res != '500':
        assert type_b in l_res[0]
        assert name.upper() in l_res[1]
        assert age == l_res[2]


@pytest.mark.parametrize("type_b , name, age, res",
                         [
                             ('BROWN', 'mihail', 17.5, '200'),
                             ('POLAR', 'Change_Name', 17.5, '200'),
                             ('POLAR', 'mihail', 10, '200'),
                         ]
                         )
def test_update(type_b, name, age, res):
    l_res = update(type_b, name, age, create_one())
    n_res = l_res[3]

    assert res in n_res
    if n_res != '500':
        assert type_b in l_res[0]
        assert name in l_res[1]
        assert age == l_res[2]


def test_dellete_all():
    # clear base
    Restful(host).dell_all_bear()
    # check base == []
    res = Restful(host).read_all_bears().json()
    assert res == []
