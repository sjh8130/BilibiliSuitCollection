#

bilibili.com////suit/detail

## stat
|start|end|
|--:|--:|
|1	|	68160 |
|100000000	| 136353001 |
|200000000	| 213153701 |

## replace
,"(time_left|time_left_month|sale_time_end|sale_left_time|sale_surplus|sales_mode)":-?\d+

,"(item_stock_surplus|sale_count_desc)":"\d{0,}[千万]?\+?"  
"(open_platform_vip_discount|hot|gray_rule)":"(true|false)",  
"(tag|tag_month)":"(新品|即将售罄|正在预约|即将下架|大会员平台折扣|粉丝套装已售罄|大会员限时折扣|即将开售)?",

"(current_activity|next_activity)":\{"type":"(vip_discount|open_platform_vip_discount)","time_limit":true,("time_left":-?\d+,)?("tag":"(新品|即将售罄|正在预约|即将下架|大会员平台折扣|粉丝套装已售罄|大会员限时折扣|即将开售)?",)?"price_bp_month":\d+,"price_bp_forever":\d+,"type_month":"(vip_discount|open_platform_vip_discount)"(,"tag_month":"(新品|即将售罄|正在预约|即将下架|大会员平台折扣|粉丝套装已售罄|大会员限时折扣|即将开售)?")?,"time_limit_month":true(,"time_left_month":-?\d+)?\},
,"(current_sources|finish_sources|current_activity|next_activity|unlock_items|activity_entrance|items)":null

("state":"(in)?active",|,"suit_items":\{\}|"gray_rule_type":"all",)  
"(sale_count_desc|total_count_desc|jump_link|tag|tag_month)":"",
,"fan_user":\{"mid":0,"nickname":"","avatar":""\}
,"activity_entrance":\{"id":0,"item_id":0,"title":"","image_cover":""(,"jump_link":"")?\}

## find
(activity_entrance|current_activity|current_sources|finish_sources|gray_rule|gray_rule_type|hot|item_stock_surplus|items|jump_link|next_activity|open_platform_vip_discount|sale_count_desc|sale_left_time|sale_surplus|sale_time_end|sales_mode|state|suit_items|tag|tag_month|time_left|time_left_month|total_count_desc|unlock_items)
(noface|账号已注销)

## desc
| key					| type	| desc	| aaa
|:--|:--|:--|:--|
| item_stock_surplus	| str	| 库存	|
| sale_surplus			| num	| 库存	|
| sale_count_desc		| str	| 已售	|
| sale_quantity			| str	| 总量	|
| time_left				| num	| 剩余时间	|UINT32MAX-unix_ts