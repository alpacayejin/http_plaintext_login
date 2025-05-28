def extract_info(pkt):
    """
    로그인 시도로 추정되는 패킷에서 정보 추출 (IP, URL, payload 등)
    """
    try:
        http_layer = pkt.http
        src_ip = pkt.ip.src
        dst_ip = pkt.ip.dst
        method = getattr(http_layer, 'request_method', '')
        host = getattr(http_layer, 'host', '')
        uri = getattr(http_layer, 'request_uri', '')
        full_url = f"http://{host}{uri}"
        payload = getattr(http_layer, 'file_data', '')

        plain_text = f"[{src_ip} -> {dst_ip}] {method} {full_url}\nPayload: {payload}\n"
        markdown = f"### 🔐 Potential Login Attempt\n- **Source IP**: {src_ip}\n- **Destination IP**: {dst_ip}\n- **Method**: `{method}`\n- **URL**: {full_url}\n- **Payload**: `{payload}`\n"

        return plain_text, markdown
    except Exception:
        return None, None

