from gpiozero import LED      # gpiozero 라이브러리에서 LED 제어 클래스 불러오기
from time import sleep        # 시간 지연을 위한 sleep 함수 불러오기

carLedRed = 17                 # 자동차용 빨간 LED가 연결된 GPIO 핀 번호 (초기 설정값)
carLedYellow = 27              # 자동차용 노란 LED 핀이 연결된 GPIO 번호
carLedGreen = 4               # 자동차용 초록 LED 핀이 연결된 GPIO 번호
humanLedRed = 20              # 보행자용 빨간 LED 핀이 연결된 GPIO 번호
humanLedGreen = 21            # 보행자용 초록 LED 핀이 연결된 GPIO 번호

carLedRed = LED(17)            # GPIO 17번 핀을 사용하는 빨간 LED 객체 생성 (자동차)
carLedYellow = LED(27)         # GPIO 27번 핀을 사용하는 노란 LED 객체 생성 (자동차)
carLedGreen = LED(4)          # GPIO 4번 핀을 사용하는 초록 LED 객체 생성 (자동차)
humanLedRed = LED(20)         # GPIO 20번 핀을 사용하는 빨간 LED 객체 생성 (보행자)
humanLedGreen = LED(21)       # GPIO 21번 핀을 사용하는 초록 LED 객체 생성 (보행자)

try:                          # 예외 처리를 위한 try 블록 시작
    while 1:                  # 무한 반복 루프 (신호등 계속 반복)
        
        # 자동차: 초록불 / 보행자: 빨간불
        carLedRed.value = 0       # 자동차 빨간 LED 끄기
        carLedYellow.value = 0    # 자동차 노란 LED 끄기
        carLedGreen.value = 1     # 자동차 초록 LED 켜기
        humanLedRed.value = 1     # 보행자 빨간 LED 켜기 (건너지 말 것)
        humanLedGreen.value = 0   # 보행자 초록 LED 끄기
        sleep(3.0)                # 3초 동안 유지
        
        # 자동차: 노란불 / 보행자: 빨간불 유지
        carLedRed.value = 0       # 자동차 빨간 LED 끄기
        carLedYellow.value = 1    # 자동차 노란 LED 켜기 (곧 정지 준비)
        carLedGreen.value = 0     # 자동차 초록 LED 끄기
        humanLedRed.value = 1     # 보행자 빨간 LED 유지
        humanLedGreen.value = 0   # 보행자 초록 LED 끄기
        sleep(1.0)                # 1초 동안 유지
        
        # 자동차: 빨간불 / 보행자: 초록불
        carLedRed.value = 1       # 자동차 빨간 LED 켜기 (정지)
        carLedYellow.value = 0    # 자동차 노란 LED 끄기
        carLedGreen.value = 0     # 자동차 초록 LED 끄기
        humanLedRed.value = 0     # 보행자 빨간 LED 끄기
        humanLedGreen.value = 1   # 보행자 초록 LED 켜기 (건너기 가능)
        sleep(3.0)                # 3초 동안 유지
    
except KeyboardInterrupt:     # Ctrl + C 입력 시 발생하는 예외 처리
    pass                     # 아무 동작도 하지 않고 종료

# 프로그램 종료 시 모든 LED 끄기
carLedRed.value = 0          # 자동차 빨간 LED 끄기
carLedYellow.value = 0       # 자동차 노란 LED 끄기
carLedGreen.value = 0        # 자동차 초록 LED 끄기
humanLedRed.value = 0        # 보행자 빨간 LED 끄기
humanLedGreen.value = 0      # 보행자 초록 LED 끄기
