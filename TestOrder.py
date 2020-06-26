import unittest
from Order import Order

"""
    
    
    @author Erika Leonor Basurto Munguia <iamdleonor@gmail.com>
    @version 1.0.0
"""
class TestOrder(unittest.TestCase):
    def test_text(self):
        textL = 'shoce pq podciy nfwh phfer epgdc dgsloqe do rhfl qhmoixw cmfur qdrulxogji whc ermjdhsx py en ycoienqm wjuln dwuch qinhmjul mjxdqfrnlg iygsex qihmu grewyluhfs ucf us xclpedqmi yrx qinexwo qx rqwwxflpdn rsogxd cpqmxj lgchqdin fdw nwcrus coj nj qplfjnwidg fwdmslqn cwj hysucxdqm ms hdmwpeigxweo sqflo ycqlinro ghu hgecdfj mw xrpmyenq fgixsr fpwcnguieh fclgj ghepqyd jxhwe cejfugn ujxqhihncrl mlceo udr fm ocxfsjdng sfoqmd pdoymnwxei spqinedf ql ncsepfl icmqsdj chwjlg yiq ifl syejrqdlwnepmcg xlmnfqry ghlyopuncw qx iw sionpux cop dmqpchuyf ojxfqhernm ignpeyf rseoyl emjocsildrfimdy mwd oewgjfr uo irmcunfgx ylduwpsnh xrdng gcxr ng prfmjicud srdueqhgiy nmodwsqijh dcnql'
        list_ = textL.split()
        O = Order()
        self.assertEqual(O.do(O.prepare(list_)),['sqflo', 'spqinedf', 'sfoqmd', 'syejrqdlwnepmcg', 'shoce', 'srdueqhgiy', 'sionpux', 'xclpedqmi', 'xlmnfqry', 'xrpmyenq', 'xrdng', 'ocxfsjdng', 'oewgjfr', 'ojxfqhernm', 'cop', 'coj', 'cmfur', 'cwj', 'cpqmxj', 'chwjlg', 'cejfugn', 'qx', 'qx', 'qplfjnwidg', 'qhmoixw', 'ql', 'qdrulxogji', 'qinhmjul', 'qinexwo', 'qihmu', 'ncsepfl', 'nmodwsqijh', 'nwcrus', 'nfwh', 'nj', 'ng', 'ms', 'mw', 'mwd', 'mlceo', 'mjxdqfrnlg', 'whc', 'wjuln', 'podciy', 'pq', 'py', 'phfer', 'prfmjicud', 'pdoymnwxei', 'fclgj', 'fm', 'fwdmslqn', 'fpwcnguieh', 'fdw', 'fgixsr', 'ycoienqm', 'ycqlinro', 'ylduwpsnh', 'yrx', 'yiq', 'hysucxdqm', 'hdmwpeigxweo', 'hgecdfj', 'en', 'emjocsildrfimdy', 'epgdc', 'ermjdhsx', 'lgchqdin', 'jxhwe', 'rsogxd', 'rseoyl', 'rqwwxflpdn', 'rhfl', 'do', 'dcnql', 'dmqpchuyf', 'dwuch', 'dgsloqe', 'gcxr', 'ghepqyd', 'ghlyopuncw', 'ghu', 'grewyluhfs', 'us', 'uo', 'ucf', 'ujxqhihncrl', 'udr', 'icmqsdj', 'iw', 'ifl', 'iygsex', 'irmcunfgx', 'ignpeyf'])
        
if __name__ == '__main__':
    unittest.main()
        