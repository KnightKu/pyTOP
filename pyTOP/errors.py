#!/usr/bin/env python
# encoding: utf-8
"""
pyTOP.exceptions
~~~~~~~~~~~~~~~~~~~

This module contains the set of pyTOP's exceptions.

"""

ERROR_MESSAGES = {

    #系统级错误
    3:u'图片上传失败',
    4:u'用户调用次数超限',
    5:u'会话调用次数超限',
    6:u'合作伙伴调用次数超限',
    7:u'应用调用次数超限',
    8:u'应用调用频率超限',
    9:u'HTTP方法被禁止（请用大写的POST或GET）',
    10:u'服务不可用',
    11:u'开发者权限不足',
    12:u'用户权限不足',
    13:u'合作伙伴权限不足',
    15:u'远程服务出错',
    21:u'缺少方法名参数',
    22:u'不存在的方法名',
    23:u'非法数据格式',
    24:u'缺少签名参数',
    25:u'非法签名',
    26:u'缺少SessionKey参数',
    27:u'无效的SessionKey参数',
    28:u'缺少AppKey参数',
    29:u'非法的AppKe参数',
    30:u'缺少时间戳参数',
    31:u'非法的时间戳参数',
    32:u'缺少版本参数',
    33:u'非法的版本参数',
    34:u'不支持的版本号',
    40:u'缺少必选参数',
    41:u'非法的参数',
    42:u'请求被禁止',
    43:u'参数错误',

    #容器类错误
    100:u'授权码已经过期',
    101:u'授权码在缓存里不存在，一般是用同样的authcode两次获取sessionkey',
    103:u'appkey或者tid（插件ID）参数必须至少传入一个',
    104:u'appkey或者tid对应的插件不存在',
    105:u'插件的状态不对，不是上线状态或者正式环境下测试状态',
    106:u'没权限调用此app，由于插件不是所有用户都默认安装，所以需要用户和插件进行一个订购关系。',
    108:u'由于app有绑定昵称，而登陆的昵称不是绑定昵称，所以没权限访问。',
    109:u'服务端在生成参数的时候出了问题（一般是tair有问题）',
    110:u'服务端在写出参数的时候出了问题',
    111:u'服务端在生成参数的时候出了问题（一般是tair有问题）',

    #业务级错误
    501:u'语句不可索引',
    502:u'数据服务不可用',
    503:u'无法解释TBQL语句',
    504:u'需要绑定用户昵称',
    505:u'缺少参数',
    506:u'参数错误',
    507:u'参数格式错误',
    508:u'获取信息权限不足',
    540:u'交易统计服务不可用',
    541:u'类目统计服务不可用',
    542:u'商品统计服务不可用',
    550:u'用户服务不可用',
    551:u'商品服务不可用',
    552:u'商品图片服务不可用',
    553:u'商品更新服务不可用',
    554:u'商品删除失败',
    555:u'用户没有订购图片服务',
    556:u'图片URL错误',
    557:u'商品视频服务不可用',
    560:u'交易服务不可用',
    561:u'交易服务不可用',
    562:u'交易不存在',
    563:u'非法交易',
    564:u'没有权限添加或更新交易备注',
    565:u'交易备注超出长度限制',
    566:u'交易备注已经存在',
    567:u'没有权限添加或更新交易信息',
    568:u'交易没有子订单',
    569:u'交易关闭错误',
    570:u'物流服务不可用',
    571:u'非法的邮费',
    572:u'非法的物流公司编号',
    580:u'评价服务不可用',
    581:u'添加评价服务错误',
    582:u'获取评价服务错误',
    590:u'店铺服务不可用',
    591:u'店铺剩余推荐数 服务不可用',
    592:u'卖家自定义类目服务不可用',
    594:u'卖家自定义类目添加错误',
    595:u'卖家自定义类目更新错误',
    596:u'用户没有店铺',
    597:u'卖家自定义父类目错误',
    601:u'用户不存在',
    611:u'产品数据格式错误',
    612:u'产品ID错误',
    613:u'删除产品图片错误',
    614:u'没有权限添加产品',
    615:u'收货地址服务不可用',
    620:u'邮费服务不可用',
    621:u'邮费模板类型错误',
    622:u'缺少参数：post, express或ems',
    623:u'邮费模板参数错误',
    630:u'收费服务不可用',
    650:u'退款服务不可用',
    651:u'非法的退款编号',
    670:u'佣金服务不可用',
    671:u'佣金交易不存在',
    672:u'淘宝客报表服务不可用',
    673:u'备案服务不可用',
    674:u'应用服务不可用',
    710:u'淘宝客服务不可用',
    900:u'远程连接错误',
    901:u'远程服务超时',
    902:u'远程服务错误',
    
    #CUSTOM ERRORS
    1000:u'Bad Environment',
}

class TOPException(Exception):
    """There was an ambiguous exception that occurred while handling your
    TOP request."""
    def __init__(self, code, msg=None):
        if not msg:
            msg = ERROR_MESSAGES.get(code,u'未知错误(%d)'%code)
        if type(msg) == unicode:
            msg = msg.encode('utf-8')
        super(TOPException, self).__init__(msg)
        self.code = code
    
    def __str__(self):
        return "%s (code=%d)" % (super(TOPException, self).__str__(), self.code)
    
    __repr__ = __str__
