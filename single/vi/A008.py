# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) wxmall.janedao.cn
# Author：QQ173782910
#QQ group:528289471
##############################################################################
"""single/vi/A008.py"""

from imp import reload
from basic.publicw import DEBUG
if DEBUG == '1':
    import single.vi.BASE_TPL
    reload(single.vi.BASE_TPL)
from single.vi.BASE_TPL             import cBASE_TPL



class cA008(cBASE_TPL):
    
    def setClassName(self):
        self.dl_name = 'A008_dl'

    def specialinit(self):
        pass

    def goPartList(self):
      
        self.assign('NL',self.dl.GNL)
        self.navTitle = ''
        self.getBreadcrumb() #获取面包屑
        PL,L = self.dl.mRight()
        self.assign('dataList',L)

        self.getPagination(PL)
        s = self.runApp('A008_list.html')
        return s
    
    def initPagiUrl(self):
        lb_code = self.REQUEST.get('lb_code','')
        brand_id = self.REQUEST.get('brand_id','')
        status = self.REQUEST.get('status','')
        ctype = self.REQUEST.get('ctype','')
        qqid = self.REQUEST.get('qqid','')
        url = self.sUrl
        if qqid:
            url += "&qqid=%s" % qqid
        if lb_code:
            url += "&lb_code=%s" % lb_code
        if brand_id:
            url += "&brand_id=%s" % brand_id
        if status:
            url += "&status=%s" % status
        if ctype:
            url += "&ctype=%s" % ctype
        return url
    
    def goPartLocalfrm(self):
        self.navTitle = ''

        self.need_editor = 1
        self.getBreadcrumb() #获取面包屑
        self.initHiddenLocal()#初始隐藏域
        
        self.getBackBtn()

        self.item = self.dl.get_local_data(self.pk)
        self.assign('item', self.item)

        
        s = self.runApp('B004_local.html')
        return s
    
    
    
        
 