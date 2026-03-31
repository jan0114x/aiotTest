from gpiozero import Buzzer, DigitalInputDevice  # 부저 및 디지털 입력 제어 라이브러리 임포트
import time                                      # 시간 지연 함수 사용을 위한 모듈 임포트

bz = Buzzer(18)                                  # GPIO 18번 핀에 부저(Buzzer) 객체 할당
gas = DigitalInputDevice(17)                     # GPIO 17번 핀에 MQ-2 가스 센서 객체 할당

try:                                             # 프로그램 실행 및 예외 처리 시작
    while True:                                  # 무한 루프 시작
        if gas.value == 0:                       # 센서값이 0(Low)이면 가스가 감지된 상태임
            print("가스 감지됨")                   # 콘솔에 감지 메시지 출력
            bz.on()                              # 가스 감지 시 부저 가동 (경보음)
        else:                                    # 센서값이 1(High)이면 가스가 없는 정상 상태임
            print("정상")                         # 콘솔에 정상 메시지 출력
            bz.off()                             # 정상 상태 시 부저 정지

        time.sleep(0.2)                          # 0.2초 간격으로 센서 상태 반복 체크

except KeyboardInterrupt:                        # 사용자가 Ctrl+C 입력 시 발생
    pass                                         # 루프를 종료하고 예외 처리 통과

bz.off()                                         # 프로그램 종료 시 부저를 안전하게 끔
