# Prepared by : Shvm-k
import pickle
B = open("BankCustmers_DB.txt", "rb+")
#بيانات العملاء الاساسية المخزة في الملف
# BC=[["Salim",2586,25000000,"","سالم"],["Sara",1978,3000000,"","سارة"],["Khalid",7895,8000000,"","خالد"],["Fatima",1256,1000000,"","فاطمة"]]
BC = pickle.load(B)
B.close()

def save():
    B = open("BankCustmers_DB.txt", "wb+")
    pickle.dump(BC, B)
    B.close()

A = ["أهلا بك في آلة سحب النقود\nادخل بطاقتك من فضلك", "أدخل رقم تعريفك الشخصي المكون من 4 أعداد:", "مرحبا",
     "\nلقد أدخلت رقم تعريفك بنجاح\n", "لا يمكنك المحاولة مجددا لقد تمت مصادرة بطاقتك\n", "رقم تعريف خاطئ\n",
     "اضغط على أي مفتاح لتعود إلى القائمة الرئيسية", "رصيدك هو \n", "كم تريد أن تسحب\n", "خذ مالك من درج الآلة\n",
     "أخذت {} لذلك فإن رصيدك أصبح {}\n", "لايمكنك سحب المال فرصيدك أقل مما تريد سحبه!", "عدد غير صحيح",
     "كم المبلغ الذي تريد إضافته؟\n", "ادخل المبلغ في درج الآلة",
     "انتظر حتى تتم عملية التأكد و حساب المال الذي أدخلته", "لقد أضفت {} لذلك فإن رصيدك هو {}\n",
     "أدخل اسم المستقبل الذي تريد إرسال المال إليه\n", "اسم مستقبل صحيح", "كم المبلغ الذي تريد تحويله إلى {}"
    , "تمت عملية تحويل المال بنجاح و رصيدك الأن هو ", "لقد أرسلت {} حوالة إلى {} لذلك فإن رصيدك هو {}\n",
     "لقد استقبلت {} حوالة من {} لذلك فإن رصيدك هو {}\n",
     "عذراً لا يمكنك التحويل فرصيدك أقل من المبلغ الذي تريد تحويله!!", "اسم مستقبل خاطئ",
     "أنت تحاول إرسال المال إلى نفسك ! \nعلى أي حال لن يتغير شيء و سيبقى رصيدك كما هو", "أدخل رقم تعريفك الشخصي ",
     "أدخل رقم تعريفك الشخصي مرة أخرى", "رقم تعريف صحيح", "أدخل رقم تعريفك الشخصي الجديد يجب أن يتكون من 4 ارقام فقط",
     "تم تغيير رقم تعريفك الشخصي بنجاح!", "لقد غيرت رقم تعريفك الشخصي\n", "رقم التعريف الشخصي يجب أن يتكون من أربعة أرقام حاول مرة أخرى!",
     "رقم تعريف خاطئ حاول مرة أخرى", "لا يمكنك المحاولة مجددا",
     "كيف يمكنني مساعدتك ؟",
     "ادخل 1 للإستعلام عن الرصيد\n ادخل 2 لسحب رصيد\nادخل 3 لإضافة رصيد\nادخل 4 لتحويل رصيد\nادخل 5 لتغيير رقم التعريف الشخصي\nادخل 6 لتغيير اللغة إلى الإنجليزية\nادخل 7 لإستعادة بطاقتك",
     "اضغط واختر ماتريد",
     "\nمن فضلك انتظر حتى تستعيد بطاقتك\n", "سجل إستخدامك للآلة هو", "\nشكرا لك\n", '\nمن فضلك ادخل رقما صحيحا\n', "عذراً و لكن لايمكنك سحب أكثر من 50000 أو أقل من 5000",
     "", "", "", "", ""]

E = ["Welcome to ATM machine\nPlease enter your card", 'Please Enter Your 4 Digits PIN: ', "Hi",
     '\nYou entered your PIN Correctly\n', '\nNo more tries,yor card is expropriation', '\nIncorrect PIN',
     "press any key to go back to Main Menu", "\nyour Balance is", '\nHow Much Would you like to withdraw? ',
     "\nTake your money", "\nYou take {}so your balance is {}",
     "you can't withdrawal because your balance less than withdrawal", "Incorrect number",
     '\nHow Much Would You Like To deposit? ', "enter your money to the machine",
     "Wait until I finish count what you enter", "\nYou add {}so your balance is {}", "\nenter the name of receiver",
     "correct receiver", 'How Much Would you like to send to {}'
    , "\nmoney is sent successfully your Balance is", "\nYou send {} to {} so your balance is {}",
     "\nYou receive {} from {} so your balance is {}",
     "you can't send because your balance is less than the number you what to send", "wrong receiver !!",
     "you want to send money to yourself !!!\nanyway nothing will change and your balance will be the same !!!",
     'enter your PIN ', 'enter your PIN again', "Correct PIN",
     'enter your new PIN it Should be in 4 Digit',
     "your PIN changed Correctly", "\nYou change your PIN",
     "your PIN should be in 4 Digits(integers),try again", "Incorrect PIN ,try again", "no more tries",
     "\nHow can I help you ?", "Enter 1 To Show Your Balance\n"
                               "Enter 2 To Make a Withdrawal\nEnter 3 To Deposit\n"
                               "Enter 4 To Send Balance\nEnter 5 To Change your PIN"
                               "\nEnter 6 To change language to Arabic"
                               "\nEnter 7 To Return your card", "choose what you want",
     '\nPlease wait whilst your card is Returned...\n', "the register of your service is", '\nThank you \n',
     "\nPlease Enter a correct number. \n", "Sorry, but you can't withdraw more than 50000 or less than 5000", "", "", "", "", ""]

class ATM():
    def __init__(self):
        self.register = ""
        language = input(
            "Choose your language press 1 for Arabic or 2 for English\nاختر لغتك اضغط 1 للغة العربية و 2 للغة الانجليزية")
        if language == "1":
            self.language = A

        elif language == "2":
            self.language = E

        else:
            self.language = A
            print("مدخل غير صحيح لذلك سيتم استخدام اللغة العربية يمكنك تغيرها من القائمة الرئيسية متى شئت")
        print(self.language[0])
        chances = 4

        while chances > 0:
            pin = input(self.language[1])
            if self.CheckIf_PIN_4integers(pin):
                pin = int(pin)
                for i in range(len(BC)):  # BC=BankCastumers list

                        if self.language==A:
                          a=4
                        else:
                          a=0
                        if pin == BC[i][1]:
                            print(self.language[2], BC[i][a], self.language[3])
                            self.CI = i  # the index of custmer
                            self.option()
                            chances = 0
                            break

                else:
                    print(self.language[5])
                    chances = chances - 1
                    if chances == 0:
                        print(self.language[4])
                        break

            else:
                print(self.language[5])
                chances = chances - 1
                if chances == 0:
                    print(self.language[4])
                    print("-" * 10, "\n", "-" * 10, "\n")
                    break

    def CheckIf_PIN_4integers(self, PIN):
        cn = 0
        for n in PIN:
            if 57 >= ord(n) >= 48 :
                cn += 1
        if cn == len(PIN) == 4 and len(PIN)!=0:
            return True
        else:
            return False

    def CheckIf_num(self, n):
        cf = 0
        for f in n:
            if 57 >= ord(f) >= 48:
                cf += 1
        if cf == len(n) and  len(n)!=0:
            return True
        else:
            return False

    def reoption(self ):
        k = input(self.language[6])
        print("-" * 50, "\n", "-" * 50, "\n")
        self.option()

    def BalanceInfo(self):
        print(self.language[7], BC[self.CI][2])
        self.reoption()

    def CheckBalance(self, n):
        if BC[self.CI][2] >= n:
            return True

    def withdrawl(self):
        w = input(self.language[8])
        if self.CheckIf_num(w):
            w = int(w)
            if self.CheckBalance(w):
              if 5000<=w<=50000:
                BC[self.CI][2] -= w
                print(self.language[9])
                print(self.language[7], BC[self.CI][2])
                self.register += self.language[10].format(w, BC[self.CI][2])
                BC[self.CI][3] += self.language[10].format(w, BC[self.CI][2])
                save()
              else:
                  print(self.language[42])

            else:
                print(self.language[11])
                print(self.language[7], BC[self.CI][2])
        else:
            print(self.language[12])

        self.reoption()

    def deposit(self):
        d = input(self.language[13])
        if self.CheckIf_num(d):
            print(self.language[14])
            d = int(d)
            BC[self.CI][2] += d
            print(self.language[15])
            print(self.language[7], BC[self.CI][2])
            self.register += self.language[16].format(d, BC[self.CI][2])
            BC[self.CI][3] += self.language[16].format(d, BC[self.CI][2])
            save()
        else:
            print(self.language[12])
        self.reoption()

    def SendBalance(self):
        receiver = input(self.language[17])
        receiver = receiver.capitalize()
        if receiver != BC[self.CI][0]:
            for j in BC:
                if (receiver == j[0] or receiver==j[4]):
                  print(self.language[18])
                  s = input(self.language[19].format(receiver))
                  if self.CheckIf_num(s):
                    s=int(s)
                    if self.CheckBalance(s):
                        BC[self.CI][2] -= s
                        j[2] += s
                        print(self.language[20], BC[self.CI][2])
                        self.register += self.language[21].format(s, receiver, BC[self.CI][2])
                        BC[self.CI][3] += self.language[21].format(s, receiver, BC[self.CI][2])
                        j[3] += self.language[22].format(s, BC[self.CI][0], j[2])
                        save()
                        break
                    else:
                        print(self.language[23])
                        print(self.language[7], BC[self.CI][2])
                        break
                  else:
                      print(self.language[12])
                      break
            else:
                print(self.language[24])
        else:
            print(self.language[25])

        self.reoption()

    def ChangePIN(self):
        for c in range(3):
            opin1 = input(self.language[26])
            opin2 = input(self.language[27])
            if self.CheckIf_PIN_4integers(opin1) and self.CheckIf_PIN_4integers(opin2):
                opin1 = int(opin1)
                opin2 = int(opin2)
                if BC[self.CI][1] == opin1 and opin1 == opin2:
                    print(self.language[28])
                    NewPIN = input(self.language[29])
                    if self.CheckIf_PIN_4integers(NewPIN):
                        NewPIN = int(NewPIN)
                        BC[self.CI][1] = NewPIN
                        print(self.language[30])
                        self.register += self.language[31]
                        BC[self.CI][3] += self.language[31]
                        save()
                        break
                    else:
                        print(self.language[32])
                else:
                    print(self.language[33])
            else:
                print(self.language[32])
        else:
            print(self.language[34])
        self.reoption()

    def option(self):
        print(self.language[35])
        print(self.language[36])
        option = input(self.language[37])
        if option == "1":
            self.BalanceInfo()

        elif option == "2":
            self.withdrawl()

        elif option == "3":
            self.deposit()

        elif option == "4":
            self.SendBalance()

        elif option == "5":
            self.ChangePIN()

        elif option == "6":
            if self.language == A:
                self.language = E
            else:
                self.language = A
            self.reoption()

        elif option == "7":
            print(self.language[38])
            if self.register!="":
             print(self.language[39], self.register)
            print(self.language[40], "-" * 50,"\n" ,"-" * 50,"\n" ,"-" * 50)

        else:
            print(self.language[41])
            self.reoption()

while 1:
    a = ATM()