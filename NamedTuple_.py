from typing import NamedTuple

class Address(NamedTuple):
    """地址信息结果"""
    country: str
    province: str
    city: str

def latlon_to_address(lat, lon):
    ...
    return Address(country=country, province=province, city=city,)

addr = latlon_to_address(lat, lon)
# 通过属性名来使用 addr
# addr.country / addr.province / addr.city