# suit

## 
| key | type | desc | value |
|:--|:--|:--|:--|
item_id						|num		|物品id	|
name						|str		|装扮名称	|
group_id					|num		|分组id	|
group_name					|str		|装扮名称	|
part_id						|num		|部件id	| 1~13
state						|str		|状态	|"active"	"inactive"
properties					|obj		|	|
current_activity			|null/obj	|	|
next_activity				|null/obj	|	|
current_sources				|null/		|	|
finish_sources				|null/		|	|
sale_left_time				|num		|	|
sale_time_end				|num		|	|
sale_surplus				|num		|	|
sale_count_desc				|str		|	|
total_count_desc			|str		|	|
tag							|str		|	|
jump_link					|str		|	|
sales_mode					|num		|	|
suit_items					|obj		|	|
fan_user					|obj		|	|
unlock_items				|null		|	|
activity_entrance			|obj		|	|

## properties
| key | type | desc | value |
|:--|:--|:--|:--|
desc						|str	|装扮说明	|
fan_id						|str	|物品id	|item_id,name
fan_item_ids				|str	|所有装扮id	|随机排序 "1,3,2,4"
fan_mid						|str	|装扮所属	|mid
fan_no_color				|str	|主题色	|
fan_recommend_desc			|str	|xxx	|
fan_recommend_jump_type		|str	|xxx	|
fan_recommend_jump_value	|str	|xxx	|
fan_share_image				|str	|xxx	|
gray_rule_type				|str	|xxx	|
gray_rule					|str	|xxx	|
image_cover_color			|str	|	|
image_cover_long			|str	|xxx	|
image_cover					|str	|xxx	|
image_desc					|str	|xxx	|
is_hide						|str	|xxx	|
item_base_intro_image		|str	|xxx	|
item_hot_limit				|str	|xxx	|
item_id_card				|str	|xxx	|
item_id_emoji_package		|str	|xxx	|
item_id_emoji				|str	|xxx	|
item_id_pendant				|str	|xxx	|
item_id_thumbup				|str	|xxx	|
item_stock_surplus			|str	|库存	|
open_platform_vip_discount	|str	|xxx	|
owner_uid					|str	|版权方？/制作方？	|
pub_btn_plus_color			|str	|xxx	|
pub_btn_shade_color_bottom	|str	|xxx	|
pub_btn_shade_color_top		|str	|xxx	|
rank_investor_name			|str	|xxx	|
rank_investor_show			|str	|xxx	|
realname_auth				|str	|xxx	|
related_words				|str	|xxx	|
sale_bp_forever_raw			|str	|原价	|
sale_bp_pm_raw				|str	|xxx	|
sale_buy_num_limit			|str	|限购	|
sale_quantity_limit			|str	|总量	|
sale_quantity				|str	|xxx	|
sale_region_ip_limit		|str	|区域限制	|
sale_reserve_switch			|str	|xxx	|
sale_sku_id_1				|str	|xxx	|
sale_sku_id_2				|str	|xxx	|
sale_time_begin				|str	|xxx	|
sale_time_end				|str	|xxx	|
sale_type					|str	|xxx	|
suit_card_type				|str	|xxx	|
timing_online_unix			|str	|xxx	|
type						|str	|xxx	|ip up

## current_activity next_activity
| key | type | desc | value |
|:--|:--|:--|:--|
type				|num	|	|open_platform_vip_discount,vip_discount
time_limit			|bool	|	|
time_left			|str	|剩余时间(秒)	|
tag					|num	|	|新品,即将售罄,正在预约,即将下架,大会员平台折扣,粉丝套装已售罄
price_bp_month		|num	|基础套装 折扣价	|
price_bp_forever	|num	|折扣价	|
type_month			|num	|	|
tag_month			|num	|	|
time_limit_month	|bool	|	|
time_left_month		|str	|基础套装 剩余时间(秒)	|

## suit_items
| key | type | desc | value |
|:--|:--|:--|:--|
card						|list(obj)	|xxxx	|
card_bg						|list(obj)	|xxxx	|
emoji_package				|list(obj)	|xxxx	|
pendant						|list(obj)	|xxxx	|
skin						|list(obj)	|xxxx	|
space_bg					|list(obj)	|xxxx	|
thumbup						|list(obj)	|xxxx	|
loading						|list(obj)	|xxxx	|
play_icon					|list(obj)	|xxxx	|

## fan_user
| key | type | desc | value |
|:--|:--|:--|:--|
mid							|num		|	|
nickname					|str		|	|
avatar						|str		|	|

## activity_entrance
| key | type | desc | value |
|:--|:--|:--|:--|
id							|num		|xxxx	|
item_id						|num		|xxxx	|
title						|num		|xxxx	|
image_cover					|num		|xxxx	|
jump_link					|num		|xxxx	|

## suit_items -> items <- items
| key | type | desc | value |
|:--|:--|:--|:--|
item_id						|num		|物品id	|
name						|str		|装扮名称	|
state						|str		|状态	|"active"	"inactive"
tab_id						|str		|	|
suit_item_id				|num		|	|
properties					|obj		|	|
current_activity			|null		|	|
next_activity				|null		|	|
current_sources				|null		|	|
finish_sources				|null		|	|
sale_left_time				|num		|	|
sale_time_end				|num		|	|
sale_surplus				|num		|	|
items						|null/obj	|	| depth = 1

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

## properties fan_recommend_jump_value
| desc | example |
|:--|:--|
视频BVid_URL|https://www.bilibili.com/video/BV1xxxxxxxxx
-|https://www.bilibili.com/video/BV1xxxxxxxxx?from=search&seid=xxxxxxxxxxxxxxxxxxxx&spm_id_from=333.337.0.0
-|https://www.bilibili.com/video/BV1xxxxxxxxx?p=1
-|https://www.bilibili.com/video/BV1xxxxxxxxx?spm_id_from=333.999.0.0
-|https://www.bilibili.com/video/BV1xxxxxxxxx?spm_id_from=333.999.0.0&vd_source=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
-|https://www.bilibili.com/video/BV1xxxxxxxxx?vd_source=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
-|https://www.bilibili.com/video/BV1xxxxxxxxx/
-|https://www.bilibili.com/video/BV1xxxxxxxxx/?share_source=copy_web&vd_source=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
-|https://www.bilibili.com/video/BV1xxxxxxxxx/?spm_id_from=333.337.search-card.all.click
-|https://www.bilibili.com/video/BV1xxxxxxxxx/?spm_id_from=333.337.search-card.all.click&vd_source=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
-|https://www.bilibili.com/video/BV1xxxxxxxxx/?spm_id_from=333.999.0.0
-|https://www.bilibili.com/video/BV1xxxxxxxxx/?spm_id_from=333.999.0.0&vd_source=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
-|https://www.bilibili.com/video/BV1xxxxxxxxx/?spm_id_from=333.999.list.card_archive.click
-|https://www.bilibili.com/video/BV1xxxxxxxxx/?spm_id_from=333.999.list.card_archive.click&vd_source=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
-|https://www.bilibili.com/video/BV1xxxxxxxxx/?vd_source=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
个人主页URL|https://space.bilibili.com/XXX
-|https://space.bilibili.com/XXX?from=search&seid=xxxxxxxxxxxxxxxxxxxx
-|https://space.bilibili.com/XXX?from=search&seid=xxxxxxxxxxxxxxxxxxxx&spm_id_from=333.337.0.0
-|https://space.bilibili.com/XXX?share_from=space&share_medium=iphone&share_plat=ios&share_session_id=FFFFFFFF-FFFF-4FFF-FFF-FFFFFFFFFFFF&share_source=WEIXIN&share_tag=s_i&timestamp=1668066267&unique_k=xxxxxxx
-|https://space.bilibili.com/XXX?spm_id_from=333.1007.0.0
-|https://space.bilibili.com/XXX?spm_id_from=333.337.0.0
-|https://space.bilibili.com/XXX?spm_id_from=333.337.search-card.all.click
-|https://space.bilibili.com/XXX?spm_id_from=333.999.0.0
-|https://space.bilibili.com/XXX?spm_id_from=666.25.0.0
-|https://space.bilibili.com/XXX/
-|https://space.bilibili.com/XXX/?spm_id_from=333.999.0.0
-|https://space.bilibili.com/XXX/dynamic
-|https://space.bilibili.com/XXX/dynamic?spm_id_from=444.41.my-info.face.click
-|_` https://space.bilibili.com/XXX/`
biligame_URL|https://www.biligame.com/detail/?id=123456
-|https://www.biligame.com/detail/?id=123456&sourceFrom=1234
-|https://www.biligame.com/detail/?id=123456&sourceFrom=1234&spm_id_from=333.337.0.0
-|https://ly2202.biligame.com/2022wdxpzh2409/h5?process=main
bili游戏_URL|https://game.bilibili.com/gjqt3/
短链接（有可能已过期）|https://b23.tv/xxxxxxxx
-|_` https://b23.tv/TZkLVTb`
bangumi_URL|https://www.bilibili.com/bangumi/media/md12345678
-|https://www.bilibili.com/bangumi/media/md12345678/?from=decoration
-|https://www.bilibili.com/bangumi/media/md12345678/?spm_id_from=666.25.b_6d656469615f6d6f64756c65.2
-|https://www.bilibili.com/bangumi/play/ep12345678
-|https://www.bilibili.com/bangumi/play/ep12345678?from_spmid=666.19.0.0
-|https://www.bilibili.com/bangumi/play/ep12345678?from_spmid=666.25.episode.0
-|https://www.bilibili.com/bangumi/play/ep12345678?from_spmid=666.25.titbit.0
-|https://www.bilibili.com/bangumi/play/ep12345678?from_spmid=666.5.0.0
-|https://www.bilibili.com/bangumi/play/ep12345678?spm_id_from=333.337.0.0&from_spmid=666.25.episode.0
-|https://www.bilibili.com/bangumi/play/ep12345678?spm_id_from=333.999.0.0&from_spmid=666.25.episode.0
-|https://www.bilibili.com/bangumi/play/ep12345678/?from=decoration
-|https://www.bilibili.com/bangumi/play/ss12345678
-|https://www.bilibili.com/bangumi/play/ss12345678?spm_id_from=333.337.0.0
-|https://www.bilibili.com/bangumi/play/ss12345678?theme=movie&spm_id_from=333.337.0.0
-|https://www.bilibili.com/bangumi/play/ss12345678/
-|https://www.bilibili.com/bangumi/play/ss12345678/?from=search&seid=xxxxxxxxxxxxxxxxxxxx
-|https://www.bilibili.com/bangumi/play/ss12345678/?from=search&seid=xxxxxxxxxxxxxxxxxxxx&spm_id_from=333.337.0.0
-|`"作品跳转：https://www.bilibili.com/bangumi/play/ep12345678"`
blackboard_URL|https://www.bilibili.com/blackboard/2021bnj-pre.html?current_tab=week-4
-|https://www.bilibili.com/blackboard/activity-7yksWguqU.html?msource=zhuangban
-|https://www.bilibili.com/blackboard/activity-yellowVSgreen5th.html?from=decoration
-|https://www.bilibili.com/blackboard/group/131148?tab_id=21&tab_module_id=71
-|https://www.bilibili.com/blackboard/ULTFEST2020.html
-|https://live.bilibili.com/blackboard/activity-k1mAlaSYlk.html?spm_id_from=333.999.0.0
-|https://mall.bilibili.com/blackboard/activity-kss12345678LsOqFQ.html
-|https://mall.bilibili.com/blackboard/activity-uhI33YzFDm.html
播放列表|https://www.bilibili.com/medialist/play/123456789?from=space&business=space&sort_field=pubtime
会员购URL|https://show.bilibili.com/platform/home.html?msource=pc_web&spm_id_from=333.851.b_696e7465726e6174696f6e616c486561646572.5
-|https://www.bilibili.com/h5/mall/home
-|https://www.bilibili.com/h5/mall/suit/detail?navhide=1&id=1234
漫画URL|https://manga.bilibili.com/detail/mc12345?from=manga_serach
-|https://manga.bilibili.com/detail/mc12345
其它|https://bml.bilibili.com
-|https://bml.bilibili.com/
-|https://bw.bilibili.com
-|https://bw.bilibili.com/2021/
？|64719309416237108045788062947
