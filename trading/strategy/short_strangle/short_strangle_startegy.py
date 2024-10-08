from trading.common.enums import TradeType, Market
from trading.strategy import IStrategy


class ShortStrangleStrategy(IStrategy):
    def start(self, trade_type: TradeType, market: Market, lot_qty: int):
        raise NotImplemented
