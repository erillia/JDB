class finder:
    """make conditions for find elements"""
    def _is(OBJ , Value):
        """OBJ == Value"""
        _condition = {'obj' : OBJ , 'cond':'==' , 'value' : Value}
        return _condition
    def not_is(OBJ , Value):
        """OBJ != Value"""
        _condition = {'obj' : OBJ , 'cond':'!=' , 'value' : Value}
        return _condition
    def condition(OBJ , cond ,Value):
        """OBJ cond Value"""
        _condition = {'obj' : OBJ , 'cond':cond , 'value' : Value}
        return _condition
    def all():
        return {'obj' : '__all__' , 'cond' :'all' , 'value' : '___all___'}