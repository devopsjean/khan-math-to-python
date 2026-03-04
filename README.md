# khan-math-to-python

Khan Academy 문제를 Python 노트북(`.ipynb`)으로 옮긴 학습 저장소입니다.

## Run Locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

그 다음 VS Code/Jupyter에서 커널로 `.venv`를 선택해 실행합니다.

## Quality Check

GitHub Actions가 push/PR마다 모든 `.ipynb` 파일이:
- 비어있지 않은지
- JSON/Notebook 포맷이 유효한지

를 자동 검증합니다.

## Notebook Pattern (Security + Reproducibility)

이 저장소의 노트북 코드는 아래 패턴을 기본으로 유지합니다.

- `함수`로 계산 로직 정의
- 문제 본문의 숫자로 `고정 예제` 실행
- `use_custom_input = False` 기본값의 선택형 입력 블록 제공

이 방식으로 GitHub/Local/CI에서 실행 재현성을 확보하고, 입력 대기 상태로 파이프라인이 멈추는 문제를 방지합니다.

보안 원칙:
- 노트북/출력에 API 키, 토큰, 개인정보를 저장하지 않음
- 외부 노트북 코드는 검토 후 실행
