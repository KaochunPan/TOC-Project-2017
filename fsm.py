from transitions.extensions import GraphMachine


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

    def is_going_to_basic(self, update):
        text = update.message.text
        return text.lower() == 'basic'

    def is_going_to_crouched(self, update):
        text = update.message.text
        return text.lower() == 'crouched'

    def is_going_to_set_up(self, update):
        text = update.message.text
        return text.lower() == 'set_up'

    def is_going_to_spike(self, update):
        text = update.message.text
        return text.lower() == 'spike'

    def is_going_to_advanced(self, update):
        text = update.message.text
        return text.lower() == 'advanced'

    def is_going_to_defence(self, update):
        text = update.message.text
        return text.lower() == 'defence'

    def is_going_to_attack(self, update):
        text = update.message.text
        return text.lower() == 'attack'    

    def is_going_to_record(self, update):
        text = update.message.text
        return text.lower() == 'record'

    def is_going_to_year102(self, update):
        text = update.message.text
        return text.lower() == '102'

    def is_going_to_year103(self, update):
        text = update.message.text
        return text.lower() == '103'

    def is_going_to_year104(self, update):
        text = update.message.text
        return text.lower() == '104'

    def is_going_to_year105(self, update):
        text = update.message.text
        return text.lower() == '105'

    def on_enter_basic(self, update):
        update.message.reply_text("歡迎進入基本排球介紹")
        update.message.reply_text("你可以輸入以下指令來看你想要的介紹:\n crouched  (低手)\n set_up  (托球)\n spike  (攻擊)")

    def on_exit_basic(self, update):
        print('Leaving basic')

    def on_enter_crouched(self, update):
        update.message.reply_text("介紹低手:")
        update.message.reply_text("1.準備姿勢:將腳張開約與肩同寬，膝蓋彎曲呈現低姿勢，重心壓地背部不要蜷縮") 
        update.message.reply_text("2.將手臂延伸出去(夾住肩膀會更容易)，這也會保護你的手肘")
        update.message.reply_text("3.用手肘帶動你的手臂揮動(腳和手要同步帶動)")
        update.message.reply_text("4.當膝蓋轉向時，手臂維持的平面也要轉向同個角度")
        update.message.reply_text("5.擊球時手臂要維持水平和穩固")
        update.message.reply_text("最後，讓我們來欣賞一段影片，讓我們更有概念什麼是正確的低手姿勢\nhttps://youtu.be/DPYZY1BGCgE")
        update.message.reply_text("了解正確姿勢後怕沒有菜單練習嗎？看看這個影片吧！\nhttps://youtu.be/RhM04ppftlI")
        self.go_back(update)

    def on_exit_crouched(self, update):
        print('Leaving crouched')

    def on_enter_set_up(self, update):
        update.message.reply_text("介紹托球")
        update.message.reply_text("1.首先正確移動傳球的位置的下方，雙臂提起，屈肘關節，置於臉前，手自然張開，掌心朝外，手腕後彎，使雙手大姆指相對呈一「八」字型，其寬度與球體的直徑相等。")
        update.message.reply_text("2.各手指都需張開，接觸球時，運用手指的第二關節前部位接球，利用上、下肢屈伸得反作用力量，將球傳出去，眼睛注意球體的飛行。")
        update.message.reply_text("3.伸臂不宜太早，以增加工作的距離。")
        update.message.reply_text("4.觸球之前，全身肌肉放鬆，尤其手臂的放鬆更為重要。")
        update.message.reply_text("如同介紹低手一樣，讓我們欣賞一段影片看看正確姿勢吧\nhttps://youtu.be/-UIu1ybICuM")
        update.message.reply_text("菜單參考\nhttps://youtu.be/jWFsw-SHKWE")
        self.go_back(update)

    def on_exit_set_up(self, update):
        print('Leaving set_up')

    def on_enter_spike(self, update):
        update.message.reply_text("介紹攻擊")
        update.message.reply_text("1.準備起跳前的助跑時，腳要明確的一左一右跨出去，然後手的姿勢也要同時作業，雙手往後伸，手臂成一直線，手肘不要彎，用手腕的力量控制，使手背與手臂呈垂直。")
        update.message.reply_text("2.你藉由手臂將上腿的力量往上跳，雙手手臂與你的身體盡量呈一直線狀態。")
        update.message.reply_text("3.慣用手往後，準備做出攻擊動作。")
        update.message.reply_text("4.準備攻擊時，非慣用手放在下巴下方至胸部一帶，用一種壓胸的力道，帶腰力往下揮，讓揮擊的力道可以帶出來。")
        update.message.reply_text("如同介紹低手一樣，讓我們欣賞一段影片看看正確姿勢吧\nhttps://youtu.be/jL0rz8LYGUI")
        update.message.reply_text("菜單參考\nhttps://youtu.be/0QQ2VBWQgA0")
        self.go_back(update)

    def on_exit_spike(self, update):
        print('Leaving spike')

    def on_enter_advanced(self, update):
        update.message.reply_text("歡迎進入進階排球介紹")
        update.message.reply_text("你可以輸入以下指令來看你想要的介紹:\n defence  (防守站位)\n attack  (攻擊戰術)")

    def on_exit_advanced(self, update):
        print('Leaving advanced')

    def on_enter_defence(self, update):
        update.message.reply_text("介紹防守站位")
        update.message.reply_text("這裡主要要講的是後排防守站位，這裡大概有三個重點，並且隨後會有一部影片讓我們學習")
        update.message.reply_text("【腳先動】\n在球被擊中之前，防守位置的球員已經做好判斷，腳已經先動。")
        update.message.reply_text("【要站在攔網攔不到的地方】\n在球確實被擊中時，防守的人永遠在攔網員的周圍，不是在攔網員的背後。你站的位置應該清楚的可以看到攻擊手擊球而不是被攔網的人擋住。判斷的方式先看攔網的人的位置，再補上其他可能的攻擊範圍。球擊中的瞬間腳已經固定位置準備好去接強力的球。")
        update.message.reply_text("【三角形】\n基本的觀念就是攻擊手的攻擊範圍如果延伸出一個三角形，攔網的人已經遮掉這個三角形的一部分，那後排防守的人當然就是要補上那塊沒人防守的三角形囉。")
        update.message.reply_text("最後是教學影片，看了會更清楚概念\nhttps://youtu.be/fOghg7PTal0")    
        self.go_back(update)

    def on_exit_defence(self, update):
        print('Leaving defence')

    def on_enter_attack(self, update):
        update.message.reply_text("介紹攻擊戰術")
        update.message.reply_text("這邊只會介紹快攻戰術，由於長大大致上就是兩邊常以及後排，所以只要了解快攻的變化，基本上就看得懂大部分的攻擊戰術了。")
        update.message.reply_text("A式快攻(A快):\nA快攻在中國又稱為前快球，是攻擊區靠近球網與舉球員的快攻，距離約在舉球員前方一步。當接發球後，快攻手以45度方向步伐直接切入舉球員前方直立起跳，扣球關鍵是要在空中事先起跳等球。在舉球員舉到球前就體跳，球剛離舉球員指尖時，立刻甩臂攻擊。")
        update.message.reply_text("A快影片:\nhttps://youtu.be/VeGuHMO1Zno")
        update.message.reply_text("B式快攻(B快):\nB快攻又可稱作短平快，攻擊區稍離舉球員前方的快攻，距離約2-3米(約在2號位和3號位之間)。當接發球後，快攻手判斷球速及高度起跳，舉球員舉球平行球網，可藉由跑動距離來甩開攔網者。")
        update.message.reply_text("B快影片:\nhttps://youtu.be/3tFNJknpm1Q")
        update.message.reply_text("C式快攻(C快):\nC快又稱背快球，是攻擊區靠近舉球員背後的快攻，可以說是A隊的鏡像。當接發球後，快攻手往舉球員後方事先起跳等球，舉球員並將球送入正在等待的快攻手手中，而許多厲害的快攻手可以將前一步看似要跑A是快攻的方式卻一步急轉到舉球員背後變成C快打的隊手一個措手不及。")
        update.message.reply_text("C快影片:\nhttps://youtu.be/IvSu3abEDfg")
        update.message.reply_text("D式快攻(D快):\n攻擊區稍離舉球員後方的快攻，距離約2米，也可以說是B是快攻的鏡像，但由於舉球員會較難確認攻擊手的位置，因此比賽中也較少出現。")
        update.message.reply_text("D快影片:\nhttps://youtu.be/frcfdRuBWdQ")
        self.go_back(update)

    def on_exit_attack(self, update):
        print('Leaving attack')

    def on_enter_record(self, update):
        update.message.reply_text("歡迎進入歷年大專排球聯賽成績查詢")
        update.message.reply_text("Please enter the year you want to search(102-105)")

    def on_exit_record(self, update):
        print('Leaving record')

    def on_enter_year102(self, update):
        update.message.reply_text("102學年成績:http://www.sportsstream.idv.tw/Volleyball/Cup_Division.aspx?CupID=7")
        self.go_back(update)

    def on_exit_year102(self, update):
        print('Leaving year102')

    def on_enter_year103(self, update):
        update.message.reply_text("103學年成績:http://www.sportsstream.idv.tw/Volleyball/Cup_Division.aspx?CupID=8")
        self.go_back(update)

    def on_exit_year103(self, update):
        print('Leaving year103')

    def on_enter_year104(self, update):
       update.message.reply_text("104學年成績:http://www.sportsstream.idv.tw/Volleyball/Cup_Division.aspx?CupID=9")
        self.go_back(update)

    def on_exit_year104(self, update):
        print('Leaving year104')

    def on_enter_year105(self, update):
        update.message.reply_text("105學年成績:http://www.sportsstream.idv.tw/Volleyball/Cup_Division.aspx?CupID=25")
        self.go_back(update)

    def on_exit_year105(self, update):
        print('Leaving year105')


