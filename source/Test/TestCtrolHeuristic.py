import unittest
import sys
import os

PACKAGE_PARENT = '../..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from source.code.CtrlHeuristic import CtrlHeuristic

"""
    
    
    @author Erika Leonor Basurto Munguia <iamdleonor@gmail.com>
    @version 1.0.0
"""
class TestOrder(unittest.TestCase):
    def test_text(self):
        ch = CtrlHeuristic()
        # textL = 'sqflo spqinedf sfoqmd syejrqd shoce srdueqhgiy sionpux xclpedqmi xlmnfqryxrpmyenq xrdng ocxfsjdng oewgjfr ojxfqhernm cop coj cmfur cwj cpqmxj chwjlg cejfugn qx qplfjnwidgqhmoixw ql qdrulxogji qinhmjul qinexwo qihmu ncsepfl nmodwsqijh nwcrus nfwh nj ng ms mw mwdmlceo mjxdqfrnlg wxflpdn whc wjuln podciy pq py phfer prfmjicud pdoymnwxei fclgj fm fwdmslqnfpwcnguieh fdw fgixsr yco ycqlinro ylduwpsnh yrx yiq hysucxdqm hdmwpe hgecdfj en emjocsild epgdcermjdhsx lwnepmcg lgchqdin jxhwe rsogxd rseoyl rqw rfimdy rhfl do dcnql dmqpchuyf dwuch dgsloqegcxr ghepqyd ghlyopuncw ghu grewyluhfs us uo ucf ujxqh udr icmqsdj iw ifl iygsex ihncrl ienqm irmcunfgxigxweo ignpeyf'
        textL = 'shoce pq podciy nfwh phfer epgdc dgsloqe do rhfl qhmoixw cmfur qdrulxogji whc ermjdhsx py en ycoienqm wjuln dwuch qinhmjul mjxdqfrnlg iygsex qihmu grewyluhfs ucf us xclpedqmi yrx qinexwo qx rqwwxflpdn rsogxd cpqmxj lgchqdin fdw nwcrus coj nj qplfjnwidg fwdmslqn cwj hysucxdqm ms hdmwpeigxweo sqflo ycqlinro ghu hgecdfj mw xrpmyenq fgixsr fpwcnguieh fclgj ghepqyd jxhwe cejfugn ujxqhihncrl mlceo udr fm ocxfsjdng sfoqmd pdoymnwxei spqinedf ql ncsepfl icmqsdj chwjlg yiq ifl syejrqd lwnepmcg xlmnfqry ghlyopuncw qx iw sionpux cop dmqpchuyf ojxfqhernm ignpeyf rseoyl emjocsildrfimdy mwd oewgjfr uo irmcunfgx ylduwpsnh xrdng gcxr ng prfmjicud srdueqhgiy nmodwsqijh dcnql'
        self.assertEqual(ch.execute(textL), {
                                            "Preposition": 3,
                                            "Verb": 35,
                                            "Verb Subjunctive": 23,
                                            "Pretty Number": 11,
                                            "Vocabulary": [
                                                "sqflo",
                                                "spqinedf",
                                                "sfoqmd",
                                                "syejrqd",
                                                "shoce",
                                                "srdueqhgiy",
                                                "sionpux",
                                                "xclpedqmi",
                                                "xlmnfqry",
                                                "xrpmyenq",
                                                "xrdng",
                                                "ocxfsjdng",
                                                "oewgjfr",
                                                "ojxfqhernm",
                                                "cop",
                                                "coj",
                                                "cmfur",
                                                "cwj",
                                                "cpqmxj",
                                                "chwjlg",
                                                "cejfugn",
                                                "qx",
                                                "qplfjnwidg",
                                                "qhmoixw",
                                                "ql",
                                                "qdrulxogji",
                                                "qinhmjul",
                                                "qinexwo",
                                                "qihmu",
                                                "ncsepfl",
                                                "nmodwsqijh",
                                                "nwcrus",
                                                "nfwh",
                                                "nj",
                                                "ng",
                                                "ms",
                                                "mw",
                                                "mwd",
                                                "mlceo",
                                                "mjxdqfrnlg",
                                                "whc",
                                                "wjuln",
                                                "podciy",
                                                "pq",
                                                "py",
                                                "phfer",
                                                "prfmjicud",
                                                "pdoymnwxei",
                                                "fclgj",
                                                "fm",
                                                "fwdmslqn",
                                                "fpwcnguieh",
                                                "fdw",
                                                "fgixsr",
                                                "ycoienqm",
                                                "ycqlinro",
                                                "ylduwpsnh",
                                                "yrx",
                                                "yiq",
                                                "hysucxdqm",
                                                "hdmwpeigxweo",
                                                "hgecdfj",
                                                "en",
                                                "emjocsildrfimdy",
                                                "epgdc",
                                                "ermjdhsx",
                                                "lwnepmcg",
                                                "lgchqdin",
                                                "jxhwe",
                                                "rsogxd",
                                                "rseoyl",
                                                "rqwwxflpdn",
                                                "rhfl",
                                                "do",
                                                "dcnql",
                                                "dmqpchuyf",
                                                "dwuch",
                                                "dgsloqe",
                                                "gcxr",
                                                "ghepqyd",
                                                "ghlyopuncw",
                                                "ghu",
                                                "grewyluhfs",
                                                "us",
                                                "uo",
                                                "ucf",
                                                "ujxqhihncrl",
                                                "udr",
                                                "icmqsdj",
                                                "iw",
                                                "ifl",
                                                "iygsex",
                                                "irmcunfgx",
                                                "ignpeyf"
                                            ]
                                        } )
        
if __name__ == '__main__':
    unittest.main()