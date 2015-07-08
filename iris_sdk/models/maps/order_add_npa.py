#!/usr/bin/env python

from iris_sdk.models.maps.base_map import BaseMap

class OrderAddNpaMap(BaseMap):

    back_order_requested = None
    customer_order_id = None
    enable_lca = None
    name = None
    npanxx_search_and_order_type = None
    partial_allowed = None
    site_id = None