from examples.get_account_info import GetAccountInfo
from examples.get_available_numbers import GetAvailableNumbers
from examples.get_in_service_numbers import GetInServiceNumbers
from examples.get_sip_peers import GetSipPeers
from examples.get_sites import GetSites
from examples.movetns import Movetns
from examples.pagination import Pagination
from examples.write_sip_peers import WriteSipPeers
from examples.write_sites import WriteSites

FILENAME = "examples/config.cfg"

fn = FILENAME

GetAccountInfo(fn)
GetAvailableNumbers(fn)
GetInServiceNumbers(fn)
Pagination(fn)
GetSites(fn)
WriteSites(fn)
GetSipPeers(fn)
WriteSipPeers(fn)
Movetns(fn)