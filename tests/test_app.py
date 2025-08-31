from http import HTTPStatus


def test_root_deve_retornar_status_ok_e_boas_vindas(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message':
            'Bem-vindos(as) à MidnightLib System, onde sonhos e imaginação'
            'ganham forma através de palavras que farão você viajar '
            'pela mente dos melhores romancistas.'}
