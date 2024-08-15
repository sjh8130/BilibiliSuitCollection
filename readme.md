#

bilibili.com////suit/detail

## stat
|start|end|
|-:|-:|
|1	|	70666 |
|100000000	| 136353001 |
|200000000	| 222560001 |

## replace
(,"(time_left|time_left_month|sale_time_end|sale_left_time|sale_surplus|sales_mode)":-?\d+|,"(item_stock_surplus|sale_count_desc|ref_mid)":"\d{0,}[千万]?\+?"|"(open_platform_vip_discount|hot|gray_rule)":"(true|false)",|"(tag|tag_month)":"(新品|即将售罄|正在预约|即将下架|大会员平台折扣|粉丝套装已售罄|大会员限时折扣|即将开售)?",|,"(current_sources|finish_sources|current_activity|next_activity|unlock_items|activity_entrance|items)":null|("state":"(in)?active",|,"suit_items":\{\}|"gray_rule_type":"all",)|"(sale_count_desc|total_count_desc|jump_link|tag|tag_month)":"",|,"fan_user":\{"mid":0,"nickname":"","avatar":""\}|,"activity_entrance":\{"id":0,"item_id":0,"title":"","image_cover":""(,"jump_link":"")?\}|"(current_activity|next_activity)":\{"type":"(vip_discount|open_platform_vip_discount)","time_limit":true,("time_left":-?\d+,)?("tag":"(新品|即将售罄|正在预约|即将下架|大会员平台折扣|粉丝套装已售罄|大会员限时折扣|即将开售)?",)?"price_bp_month":\d+,"price_bp_forever":\d+,"type_month":"(vip_discount|open_platform_vip_discount)"(,"tag_month":"(新品|即将售罄|正在预约|即将下架|大会员平台折扣|粉丝套装已售罄|大会员限时折扣|即将开售)?")?,"time_limit_month":true(,"time_left_month":-?\d+)?\},)

\?e=[0-9a-zA-Z_=]{70,}(&|\\\\u0026)uipk=\d+(&|\\\\u0026)nbs=\d+(&|\\\\u0026)deadline=\d+(&|\\\\u0026)gen=playurlv2(&|\\\\u0026)os=(08cbv|cosbv|alibv|upos)(&|\\\\u0026)oi=\d+(&|\\\\u0026)trid=[0-9a-fA-F]{31,33}(&|\\\\u0026)mid=\d+(&|\\\\u0026)platform=html5(&|\\\\u0026)og=(cos|hw)(&|\\\\u0026)upsig=[0-9a-f]{32}(&|\\\\u0026)uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform,og(&|\\\\u0026)bvc=vod(&|\\\\u0026)nettype=\d+(&|\\\\u0026)orderid=\d,\d(&|\\\\u0026)logo=\d+(&|\\\\u0026)f=B_0_0

## find
(activity_entrance|current_activity|current_sources|finish_sources|gray_rule|gray_rule_type|hot|item_stock_surplus|items|jump_link|next_activity|open_platform_vip_discount|sale_count_desc|sale_left_time|sale_surplus|sale_time_end|sales_mode|state|suit_items|tag|tag_month|time_left|time_left_month|total_count_desc|unlock_items)
(noface|账号已注销)

## part_id
| value | desc |
|:--|:--|
1|头像框
2|动态卡片
3|点赞效果
4|表情
5|表情包
6|装扮-主
7|空间背景
8|勋章
9|主题
10|加载动画
11|进度条装扮
12|？
13|NFT

