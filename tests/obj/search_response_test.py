# -*- coding: UTF-8 -*-
import json

from yelp.obj.coordinate import Coordinate
from yelp.obj.region import Region
from yelp.obj.search_response import SearchResponse


def test_init_phone_search_response():
    with open('json/search_response.json') as ps:
        response = json.load(ps)
        obj = SearchResponse(response)
        assert len(obj.businesses) == len(response['businesses'])
        assert type(obj.region) == Region
        assert type(obj.region.center) == Coordinate