import os
import logging
import pandas as pd
from datetime import date
from shioaji import Shioaji


class Session(Shioaji):

    def __init__(self, simulation: bool = False, timeout: int = 10000) -> None:
        """

        Args:
            simulation:
            timeout:

        Notes: The ID of test account ranging from `PAPIUSER01` to `PAPIUSER08`,
            with password `2222`.
        """
        _person_id = f"PAPIUSER05" \
            if simulation else os.environ['SINOTRADE_ID']
        _passwd = "2222" \
            if simulation else os.environ['SINOTRADE_PASSWD']
        super(Session, self).__init__(simulation=simulation)
        self.login(
            person_id=_person_id,
            passwd=_passwd,
            contracts_cb=lambda security_type: logging.info(f"{repr(security_type)} fetch done."),
            contracts_timeout=timeout
        )

    def __del__(self) -> None:
        self.logout()
        logging.info("session closed.")

    @property
    def positions(self) -> pd.DataFrame:
        return pd.DataFrame(
            self.list_positions(self.stock_account)
        )

    def profit_loss(self, begin_date: date, end_date: date) -> pd.DataFrame:
        return pd.DataFrame(self.list_profit_loss(
            self.stock_account,
            begin_date=begin_date.strftime('%Y-%m-%d'),
            end_date=end_date.strftime('%Y-%m-%d')
        ))

    @property
    def settlements(self) -> pd.DataFrame:
        return pd.DataFrame(
            self.list_settlements(self.stock_account)
        )

    @property
    def balance(self) -> pd.DataFrame:
        return pd.DataFrame(
            self.account_balance()
        )
