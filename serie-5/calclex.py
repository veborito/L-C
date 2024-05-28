# ------------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------
import ply.lex as lex
import tokrules

tokens = tokrules.tokens
class MyLexer():
    # Build the lexer
    def build(self, **kwargs):
        self.lexer = lex.lex(module=tokrules, **kwargs)
    # Test it out
    def test(self, data):
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            if not tok: 
                break      # No more input
            print(tok)

data = '''
#MBw_X2SCy
fp{p9wfba9
T$#eLhttyL
2NA8,F(=hc
gE!G$N$CUn
ft{v1&J}U=
V(F.Kc,4zk
+&JC1Ez=r?
2Snkc-;0%;
60yd-jv52V
@jigdVC@N(
TR2ih=NKG{
*/gyi$44!d
]p}[pGG1c*
P+8C:xX}&y
+q4c,GfEP&
tk,&-*4,C6
5WJ89?T$1{
/u-Mxkh}N&
{FR?heP$Dm
'''

myLexer = MyLexer()
myLexer.build()
myLexer.test(data)