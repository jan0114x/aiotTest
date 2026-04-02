from gpiozero import DigitalInputDevice          # 디지털 입력 장치(가스 센서) 제어를 위한 라이브러리 임포트
from gpiozero import OutputDevice                # 범용 출력 장치(부저 등) 제어를 위한 라이브러리 임포트
import time                                      # 시간 지연(sleep) 기능을 사용하기 위한 모듈 임포트

bz = OutputDevice(18)                            # GPIO 18번 핀을 출력 장치(부저)로 설정하여 bz 객체 생성
gas = DigitalInputDevice(17)                     # GPIO 17번 핀을 디지털 입력 장치(가스 센서)로 설정하여 gas 객체 생성

try:                                             # 프로그램의 정상 실행 블록 시작
    while True:                                  # 중단 전까지 무한히 반복 실행
        if gas.value == 0:                       # 센서값이 0(Low)이면 가스가 감지된 상태로 판단
            print("gas")                         # 터미널 창에 "gas" 문구 출력
            bz.on()                              # 출력 장치(부저)에 전원을 공급하여 켬
        else:                                    # 센서값이 1(High)이면 가스가 감지되지 않은 정상 상태임
            print("no gas")                      # 터미널 창에 "no gas" 문구 출력
            bz.off()                             # 출력 장치(부저)의 전원을 차단하여 끔

        time.sleep(0.2)                          # CPU 부하를 줄이기 위해 0.2초 간격으로 상태 확인

except KeyboardInterrupt:                        # 사용자가 Ctrl+C를 눌러 강제 종료할 경우 발생
    pass                                         # 별도의 오류 메시지 없이 예외를 통과함

bz.off()                                         # 프로그램 종료 시 부저가 켜져 있다면 안전하게 끔
