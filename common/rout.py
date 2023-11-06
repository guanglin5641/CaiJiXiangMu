class METHOD_NAME():
    #查询通达国家列表
    check_the_list_of_accessible_countries= "common.country.getlist"
    #查询交货仓列表
    query_delivery_warehouse_list= "common.warehouse.getlist"
    #查询已开通的产品列表
    query_the_list_of_activated_products= "express.channel.getlist"
    #创建运单
    create_waybill= "express.order.create"
    #打印标签
    print_labels= "express.order.label.get"
    #取消运单
    cancel_waybill= "express.order.cancel"
    #查询运单详情
    check_waybill_details= "express.order.get"
    #批量查询单号详情
    batch_inquiry_of_order_number_details= "express.order.getlist"
    #美国地址校验
    us_address_verification= "common.verify.us.address"