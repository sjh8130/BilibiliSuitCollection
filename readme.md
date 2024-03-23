#

bilibili.com////suit/detail

1~67743  
100000000~143770001  
200000000~206110401  

,"sale_time_end":-?[1-9]\d{0,}	,"sale_time_end":0  
,"sale_left_time":-?[1-9]\d{0,}	,"sale_left_time":0  
,"time_left":-?[1-9]\d{0,}	,"time_left":0  
,"time_left_month":-?[1-9]\d{0,}	,"time_left_month":0  
,"item_stock_surplus":"[1-9]\d{0,}"	,"item_stock_surplus":"0"  
,"sale_surplus":-?[1-9]\d{0,}	,"sale_surplus":0  
,"sale_count_desc":"\d+[千万]?\+?",	,"sale_count_desc":"",  

,"unlock_items":null,"activity_entrance":null
,"unlock_items":null,"activity_entrance":\{"id":0,"item_id":0,"title":"","image_cover":"","jump_link":""\}

("sale_time_end"|"sale_left_time"|"time_left"|"time_left_month"|"item_stock_surplus"|"sale_surplus"|"sale_count_desc"):"?-?[1-9]
(noface|账号已注销)

| id					| type	| desc	|aaa
|:--|:--|:--|:--|
| item_stock_surplus	| str	|库存|
| sale_surplus			| num	|库存|
| sale_count_desc		| str	|已售|
| sale_quantity			| str	|总量|
| time_left				| num	|剩余时间|UINT32MAX-unix_ts