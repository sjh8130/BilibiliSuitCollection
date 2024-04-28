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
finish_sources				|null/list	|	|
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
fan_recommend_desc			|str	|	|
fan_recommend_jump_type		|str	|	|
fan_recommend_jump_value	|str	|	|
fan_share_image				|str	|	|
gray_rule_type				|str	|	|
gray_rule					|str	|	|
image_cover_color			|str	|	|
image_cover_long			|str	|	|
image_cover					|str	|	|
image_desc					|str	|	|
is_hide						|str	|	|
item_base_intro_image		|str	|	|
item_hot_limit				|str	|	|
item_id_card				|str	|	|
item_id_emoji_package		|str	|	|
item_id_emoji				|str	|	|
item_id_pendant				|str	|	|
item_id_thumbup				|str	|	|
item_stock_surplus			|str	|库存	|
open_platform_vip_discount	|str	|	|
owner_uid					|str	|版权方？/制作方？	|
pub_btn_plus_color			|str	|	|
pub_btn_shade_color_bottom	|str	|	|
pub_btn_shade_color_top		|str	|	|
rank_investor_name			|str	|	|
rank_investor_show			|str	|	|
realname_auth				|str	|	|
related_words				|str	|	|
sale_bp_forever_raw			|str	|原价	|
sale_bp_pm_raw				|str	|	|
sale_buy_num_limit			|str	|限购	|
sale_quantity_limit			|str	|总量	|
sale_quantity				|str	|	|
sale_region_ip_limit		|str	|区域限制	|"全球" "大陆地区"
sale_reserve_switch			|str	|	|
sale_sku_id_1				|str	|	|
sale_sku_id_2				|str	|	|
sale_time_begin				|str	|	|
sale_time_end				|str	|	|
sale_type					|str	|	|
suit_card_type				|str	|	|
timing_online_unix			|str	|	|
type						|str	|	|ip up

## finish_sources
| key | type | desc | value |
|:--|:--|:--|:--|
id							|num	|	|
name						|str	|	|
time_from					|num	|	|
time_to						|num	|	|
desc						|str	|	|
jump_url					|str	|	|
source_type					|num	|	|

## current_activity next_activity
| key | type | desc | value |
|:--|:--|:--|:--|
type						|num	|	|open_platform_vip_discount,vip_discount
time_limit					|bool	|	|
time_left					|str	|剩余时间(秒)	|
tag							|num	|	|新品,即将售罄,正在预约,即将下架,大会员平台折扣,粉丝套装已售罄
price_bp_month				|num	|基础套装 折扣价	|
price_bp_forever			|num	|折扣价	|
type_month					|num	|	|
tag_month					|num	|	|
time_limit_month			|bool	|	|
time_left_month				|str	|基础套装 剩余时间(秒)	|

## suit_items
| key | type | desc | value |
|:--|:--|:--|:--|
card						|list(obj)	|	|
card_bg						|list(obj)	|	|
emoji_package				|list(obj)	|	|
pendant						|list(obj)	|	|
skin						|list(obj)	|	|
space_bg					|list(obj)	|	|
thumbup						|list(obj)	|	|
loading						|list(obj)	|	|
play_icon					|list(obj)	|	|

## fan_user
| key | type | desc | value |
|:--|:--|:--|:--|
mid							|num		|	|
nickname					|str		|	|
avatar						|str		|	|

## activity_entrance
| key | type | desc | value |
|:--|:--|:--|:--|
id							|num		|	|
item_id						|num		|	|
title						|num		|	|
image_cover					|num		|	|
jump_link					|num		|	|

## suit_items -> items
## suit_items -> items -> items
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

## suit_items -> items -> properties
## suit_items -> items -> items -> properties
| key | type | desc | value |
|:--|:--|:--|:--|
gray_rule						|str		|	|
gray_rule_type					|str		|	|
realname_auth					|str		|	|
hot								|str		|	|
image							|str		|	|card/card_bg/emoji_package/emoji_package>items
image_preview_small				|str		|	|card[1+]/card_bg/loading
sale_type						|str		|	|card/card_bg/emoji_package/emoji_package>items
addable							|str		|	|emoji_package
biz								|str		|	|emoji_package
is_symbol						|str		|	|emoji_package/emoji_package>items
item_ids						|str		|	|emoji_package
permanent						|str		|	|emoji_package
preview							|str		|	|emoji_package
recently_used					|str		|	|emoji_package
recommend						|str		|	|emoji_package
ref_mid							|str		|	|emoji_package/emoji_package>items
removable						|str		|	|emoji_package
setting_pannel_not_show			|str		|	|emoji_package
size							|str		|	|emoji_package
sortable						|str		|	|emoji_package
associate						|str		|	|emoji_package>items
loading_frame_url				|str		|	|loading
loading_url						|str		|	|loading
ver								|str		|	|loading/skin
fan_no_color					|str		|	|space_bg
fan_no_image					|str		|	|space_bg
image*_landscape				|str		|	|space_bg
image*_portrait					|str		|	|space_bg
image_ani						|str		|	|thumbup
image_ani_cut					|str		|	|thumbup
image_preview					|str		|	|thumbup/skin
color							|str		|	|skin
color_mode						|str		|	|skin
color_second_page				|str		|	|skin
head_bg							|str		|	|skin
head_myself_mp4_play			|str		|	|skin
head_myself_squared_bg			|str		|	|skin
head_tab_bg						|str		|	|skin
image_cover						|str		|	|skin
package_md5						|str		|	|skin
package_url						|str		|	|skin
skin_mode						|str		|	|skin
tail_bg							|str		|	|skin
tail_color						|str		|	|skin
tail_color_selected				|str		|	|skin
tail_icon_ani					|str		|	|skin
tail_icon_ani_mode				|str		|	|skin
tail_icon_channel				|str		|	|skin
tail_icon_dynamic				|str		|	|skin
tail_icon_main					|str		|	|skin
tail_icon_mode					|str		|	|skin
tail_icon_myself				|str		|	|skin
tail_icon_pub_btn_bg			|str		|	|skin
tail_icon_selected_channel		|str		|	|skin
tail_icon_selected_dynamic		|str		|	|skin
tail_icon_selected_main			|str		|	|skin
tail_icon_selected_myself		|str		|	|skin
tail_icon_selected_pub_btn_bg	|str		|	|skin
tail_icon_selected_shop			|str		|	|skin
tail_icon_shop					|str		|	|skin

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
