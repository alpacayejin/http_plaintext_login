KEYWORDS = ['login', 'logon', 'signin', 'user', 'username', 'id', 'pass', 'password']

def is_login_attempt(http_layer):
    """
    HTTP 요청의 URI 또는 페이로드에 로그인 시도로 보이는 키워드가 있는지 확인.
    """
    try:
        if hasattr(http_layer, 'request_method'):
            method = http_layer.request_method.lower()
            if method in ['post', 'get']:
                uri = getattr(http_layer, 'request_uri', '')
                payload = getattr(http_layer, 'file_data', '')
                combined_data = f"{uri} {payload}".lower()

                for keyword in KEYWORDS:
                    if keyword in combined_data:
                        return True
    except Exception:
        pass
    return False
