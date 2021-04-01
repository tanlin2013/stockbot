import os
import logging
import shioaji as sj


class Session:

    def __init__(self, dry_run: bool = True, timeout: int = 10000):
        """

        Args:
            dry_run:
            timeout:

        Notes: The ID of test account ranging from PAPIUSER01 to PAPIUSER08
        """
        self.api = sj.Shioaji(simulation=dry_run)
        _person_id = "PAPIUSER05" if dry_run else os.environ['SINOTRADE_ID']
        _passwd = "2222" if dry_run else os.environ['SINOTRADE_PASSWD']
        self.api.login(
            person_id=_person_id,
            passwd=_passwd,
            contracts_cb=lambda security_type: logging.info(f"{repr(security_type)} fetch done."),
            contracts_timeout=timeout
        )

    def close(self):
        del self.api
        logging.info("session closed.")
