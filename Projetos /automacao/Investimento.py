class Investimento():
    
    def __init__(self, dy, p_vp, cagr):
        self.dy = dy
        self.p_vp = p_vp
        self.cagr = cagr
        
    
class Acao():
    
    def __init__(self, dy, p_vp, cagr, roe, margem_liquida):
        super().__init__(dy, p_vp, cagr)
        self.roe = roe
        self.margem_liquida = margem_liquida

class Fii():
    
    def __init__(self, dy, p_vp, cagr, num_cotista):
        super().__init__(dy, p_vp, cagr)
        self.num_cotista = num_cotista

    
    