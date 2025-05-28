# 🔍 http_plaintext_login

Wireshark 기반으로 HTTP 트래픽에서 **평문 로그인 시도**를 자동으로 탐지하는 프로젝트입니다.  
Pyshark를 이용해 `.pcap`/`.pcapng` 파일을 분석하며, 로그인 관련 요청을 추출하여 `.txt`, `.md` 리포트로 저장합니다.

---

## 📁 디렉토리 구조

```bash
http_plaintext_login/
├── analysis/ # 탐지 및 추출 모듈
│ ├── detector.py # 로그인 시도 여부 판단
│ └── extractor.py # 로그인 정보 추출
│
├── captures/ # 분석 대상 pcap 파일 저장 폴더
│ └── sample.pcapng
│
├── report/ # 탐지 결과 저장
│ ├── result.txt # 평문 텍스트 결과
│ └── result.md # Markdown 포맷 리포트
│
├── analyzer.py # 메인 분석 실행 스크립트
└── README.md # 프로젝트 설명서
```


---

## 🧠 주요 기능

- `.pcap`/`.pcapng` 네트워크 패킷에서 HTTP 요청 필터링
- 로그인 관련 키워드 기반 요청 자동 탐지
- 요청 내 IP, URL, Payload 등 정보 추출
- 결과 리포트를 `.txt`, `.md`로 저장

---

## 🚀 사용 방법

### 1. 환경 설정

```bash
pip install pyshark          # Pyshark는 tshark가 시스템에 설치되어 있어야 합니다.
```

### 2. `.pcapng` 파일 준비
분석 대상 파일을 captures/ 폴더에 넣습니다.
예시: captures/sample.pcapng

### 3. 분석 실행
```bash
python analyzer.py
```

### 4. 결과 확인

- `report/result.txt`: 평문 텍스트 요약
- `report/result.md`: Markdown 포맷 리포트 (가독성 ↑)


## 📌 로그인 키워드 기준 
URI나 HTTP 페이로드에 아래 키워드가 포함되면 로그인 시도로 간주합니다.

- `login`, `logon`, `signin`
- `user`, `username`, `id`
- `pass`, `password`


## 🛠  향후 개선 아이디어
- HTTPS 트래픽 탐지를 위한 SSL/TLS 복호화 기능
- WebSocket 기반 인증 탐지
- GUI 리포트 (HTML 시각화)
- 자동 시간대 필터 및 IP 필터링 기능


## 👤 작성자
- 프로젝트 담당: 양예진

