import sys
import os

PACKAGE_PARENT = '../'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))


from source.code.CtrlHeuristic import CtrlHeuristic
from source.code import Constant
"""
    
    
    @author Erika Leonor Basurto Munguia <iamdleonor@gmail.com>
    @version 1.0.0
"""
class Main:
    def __init__(self):
        self.ch = CtrlHeuristic()
    def do(self, textL):
        
        response = self.ch.execute(textL)
        print(f"Input Text: \n\t {textL}\n")
        print("1) There are(is) "+ str(response[Constant.HERUGLON_NAMES[Constant.HERUGLON_PREPOSITION]]) + " preposition(s) in the text")
        print("2) There are(is) "+ str(response[Constant.HERUGLON_NAMES[Constant.HERUGLON_VERB]]) + " verb(s) in the text")
        print("3) There are(is) "+ str(response[Constant.HERUGLON_NAMES[Constant.HERUGLON_VERB_SUBJUNCTIVE]]) + " subjunctive verb(s) in the text")
        print("4) Vocabulary list: \n\t"+ ' '.join(response['Vocabulary']))
        
        print("5) There are(is) "+ str(response[Constant.HERUGLON_NAMES[Constant.HERUGLON_NUMBER_PRETTY]]) + " distinct pretty number(s) in the text")
        
        
textL = 'shoce pq podciy nfwh phfer epgdc dgsloqe do rhfl qhmoixw cmfur qdrulxogji whc ermjdhsx py en ycoienqm wjuln dwuch qinhmjul mjxdqfrnlg iygsex qihmu grewyluhfs ucf us xclpedqmi yrx qinexwo qx rqwwxflpdn rsogxd cpqmxj lgchqdin fdw nwcrus coj nj qplfjnwidg fwdmslqn cwj hysucxdqm ms hdmwpeigxweo sqflo ycqlinro ghu hgecdfj mw xrpmyenq fgixsr fpwcnguieh fclgj ghepqyd jxhwe cejfugn ujxqhihncrl mlceo udr fm ocxfsjdng sfoqmd pdoymnwxei spqinedf ql ncsepfl icmqsdj chwjlg yiq ifl syejrqd lwnepmcg xlmnfqry ghlyopuncw qx iw sionpux cop dmqpchuyf ojxfqhernm ignpeyf rseoyl emjocsildrfimdy mwd oewgjfr uo irmcunfgx ylduwpsnh xrdng gcxr ng prfmjicud srdueqhgiy nmodwsqijh dcnql'
m = Main()
m.do(textL)