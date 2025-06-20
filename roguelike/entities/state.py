class IMobState:
    def modify_strategy(self, base_strategy):
        return base_strategy

class NormalState(IMobState):
    pass

class PanicState(IMobState):
    def modify_strategy(self, base_strategy):
        from entities.strategy import FleeingStrategy
        return FleeingStrategy()
