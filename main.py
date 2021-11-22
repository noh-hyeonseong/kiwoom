# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from outlook import send_mail

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    from pykiwoom.kiwoom import *

    kiwoom = Kiwoom()
    kiwoom.CommConnect(block=True)

    # 조건식 불러오기
    kiwoom.GetConditionLoad()
    conditions = kiwoom.GetConditionNameList()  #조건식 list
    # 매집봉 조건식에 해당하는 종목 리스트 출력
    condition_index = conditions[2][0]
    condition_name = conditions[2][1]
    codes = kiwoom.SendCondition("0101", condition_name, condition_index, 0)

    for idx, i in enumerate(codes):
        codeNames = kiwoom.GetMasterCodeName(i)
        print(condition_name, idx+1, " : ", codeNames)


    #print(datetime," 전송 완료.")
    #연결 상태 확인
    #state = kiwoom.GetConnectState()
    #if state == 0:
    #    print("미연결")
    #elif state == 1:
    #    print("연결완료")
    # show_account_info()
    # 주식계좌
    # accounts = kiwoom.GetLoginInfo("ACCNO")
    # stock_account = accounts[0]
    # 삼성전자, 10주, 시장가주문 매수
    # kiwoom.SendOrder("시장가매수", "0101", stock_account, 1, "005930", 10, 0, "03", "")

