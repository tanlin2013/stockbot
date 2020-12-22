import os
import logging
import shioaji as sj


class Session:

    def __init__(self, dry_run: bool = True, timeout: int = 10000):
        self.api = sj.Shioaji(simulation=dry_run)
        self.api.login(
            person_id=os.environ['SINOTRADE_ID'],
            passwd=os.environ['SINOTRADE_PASSWD'],
            contracts_cb=lambda security_type: logging.info(f"{repr(security_type)} fetch done."),
            contracts_timeout=timeout
        )

    def __del__(self):
        del self.api
        logging.info("session closed.")
