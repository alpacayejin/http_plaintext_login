import pyshark
import os
from analysis.detector import is_login_attempt
from analysis.extractor import extract_info

os.makedirs("report", exist_ok=True)
os.makedirs("captures", exist_ok=True)

CAPTURE_FILE = 'captures/sample.pcapng'
TXT_RESULT = 'report/result.txt'
MD_RESULT = 'report/result.md'

def analyze_pcap(file_path):
    if not os.path.exists(file_path):
        print(f"[!] 파일이 존재하지 않습니다: {file_path}")
        return

    try:
        capture = pyshark.FileCapture(file_path, display_filter="http.request")
        txt_results = []
        md_results = []

        print(f"[*] {file_path} 분석 중...")

        for pkt in capture:
            if 'HTTP' in pkt and is_login_attempt(pkt.http):
                plain, md = extract_info(pkt)
                if plain:
                    txt_results.append(plain)
                    md_results.append(md)
                    print("[+] 로그인 시도 탐지:")
                    print(plain)

        os.makedirs("report", exist_ok=True)

        with open(TXT_RESULT, 'w', encoding='utf-8') as f_txt, open(MD_RESULT, 'w', encoding='utf-8') as f_md:
            for line in txt_results:
                f_txt.write(line + "\n")
            for section in md_results:
                f_md.write(section + "\n\n")

        print(f"[*] 분석 완료. 결과를 '{TXT_RESULT}' 및 '{MD_RESULT}'에 저장했습니다.")
    except Exception as e:
        print(f"[!] 분석 중 오류 발생: {e}")

if __name__ == "__main__":
    analyze_pcap(CAPTURE_FILE)
