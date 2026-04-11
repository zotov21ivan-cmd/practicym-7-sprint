# Наборы тестовых данных
VALID_LOGIN_DATA = {
    "login": "ninja260316",
    "password": "1234",
    "id": 720724
}

INVALID_LOGIN_DATA_1 = {
    "login": "ninja260316",
    "password": "123",
    "id": 720724
}

INVALID_LOGIN_DATA_2 = {
    "login": "ninja260316",
    "password": None,
    "id": 720724
}

INVALID_LOGIN_DATA_3 = {
    "login": None,
    "password": "123",
    "id": 720724
}

INVALID_LOGIN_DATA_4 = {
    "login": "ninja",
    "password": "1234",
    "id": 12345
}

VALID_ORDER_DATA_SET_1 = {
    "firstName": "Иван",
    "lastName": "Петров",
    "address": "Боярский переулок, 3",
    "metroStation": "Красные ворота",
    "phone": "+79161234567",
    "rentTime": 2,
    "deliveryDate": "2026-04-01",
    "comment": "2 этаж",
    "color": ["BLACK"]
}

VALID_ORDER_DATA_SET_2 = {
    "firstName": "Иван",
    "lastName": "Петров",
    "address": "Боярский переулок, 3",
    "metroStation": "Красные ворота",
    "phone": "+79161234567",
    "rentTime": 2,
    "deliveryDate": "2026-04-01",
    "comment": "2 этаж",
    "color": ["GREY"]
}
VALID_ORDER_DATA_SET_3 = {
    "firstName": "Иван",
    "lastName": "Петров",
    "address": "Боярский переулок, 3",
    "metroStation": "Красные ворота",
    "phone": "+79161234567",
    "rentTime": 2,
    "deliveryDate": "2026-04-01",
    "comment": "2 этаж",
    "color": ["BLACK", "GREY"]
}
VALID_ORDER_DATA_SET_4 = {
    "firstName": "Иван",
    "lastName": "Петров",
    "address": "Боярский переулок, 3",
    "metroStation": "Красные ворота",
    "phone": "+79161234567",
    "rentTime": 2,
    "deliveryDate": "2026-04-01",
    "comment": "2 этаж",
    "color": []
}