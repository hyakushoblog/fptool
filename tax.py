

# ------------------------------------------------------------------------------
class Income():
    ''' 所得税
            
    Attributes
    ----------
    employmentincom : float
        給与所得    

    '''
    def __init__(self,employmentincome=0,realpropertyincome=0,
                 sposeincome=0,
                 hudosankeihi=0,aoirokojo=0):
        '''
        '''
        self.employmentincome = employmentincome
        self.realpropertyincome = realpropertyincome        
        self.aoirokojo = aoirokojo
        self.hudosankeihi = hudosankeihi
        self.sposeincome = sposeincome
        
        if not self.aoirokojo in [65,10,0]:
            '''
            65：事業規模の不動産所得もしくは、事業所得があり
                貸借対照表と損益計算書を添付した場合
            10: 青色申告をしたが上記以外の場合
            0 : 青色申告をしなかった場合
            '''
            raise ValueError('!')
        
    @property
    def net_income(self):
        '''合計所得額
        '''
        pass

    @net_income.getter
    def net_income(self):
        '''合計所得額
        すべての所得を合計した額。控除前の額。
        '''
        # Fixme!
        net_income = self.employmentincome + self.realpropertyincome        
        return net_income

    @property
    def tax_base(self):
        pass

    @tax_base.getter
    def tax_base(self):
        '''課税標準
        控除後の所得額。税金の課税対象となる所得の合計額。
        '''
        # Fixme!        
        tax_base = self.employmentincome_deduction + self.realpropertyincome_deduction \
        - self.spose_deduction - self.basic_deduction
        return tax_base
    
    @property
    def basic_deduction(self): # 基礎控除
        pass

    @basic_deduction.getter
    def basic_deduction(self):
        '''基礎控除額

        [1] https://www.nta.go.jp/publication/pamph/koho/kurashi/html/01_1.htm#sanshiki02
        '''
        income = self.net_income
    
        if income<=2400:
            kojo = 48
        elif income>2400 and income<=2450:
            kojo = 32
        elif income>2450 and income<=2500:
            kojo = 16
        elif income>2500:
            kojo = 0
        else:
            raise ValueError('!')
        return kojo
    

    @property
    def dependent_deduction(self): # 扶養者控除
        pass    

    @dependent_deduction.getter
    def dependent_deduction(self):
        '''扶養者控除
        
        [1] https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1180.htm
        '''
        return
    
    @property
    def handicapped_deduction(self): # 障害者控除
        '''aaaa
        '''
        pass    

    @handicapped_deduction.getter
    def handicapped_deduction(self):
        '''障害者控除

        [1] https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1160.htm
        '''
        return    
    
    @property
    def widow_deduction(self): # 寡婦控除
        pass

    @widow_deduction.getter
    def widow_deduction(self):
        '''寡婦控除

        [1] https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1170.htm
        '''
        return    

    @property
    def workingstudent_deduction(self): # 勤労学生控除
        pass

    @workingstudent_deduction.getter
    def workingstudent_deduction(self):
        '''勤労学生控除

        [1] https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1175.htm
        '''
        return    

    @property
    def socialinsurancepremium_deduction(self): # 社会保険料控除
        pass        

    @socialinsurancepremium_deduction.getter
    def socialinsurancepremium_deduction(self):
        '''社会保険料控除

        [1] https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1130.htm
        '''
        return
    
    @property
    def lifeinsurancepremium_deduction(self): # 生命保険料控除
        pass

    @lifeinsurancepremium_deduction.getter
    def lifeinsurancepremium_deduction(self):
        '''生命保険控除

        [1] https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1140.htm
        '''
        return
    
    @property
    def earthquakeinsurancepremium_deduction(self): # 地震保険料控除
        pass        

    @earthquakeinsurancepremium_deduction.getter
    def earthquakeinsurancepremium_deduction(self):
        '''地震保険控除

        [1] https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1145.htm
        '''
        return    
    
    @property
    def smallbusiness_deduction(self): # 小規模企業共済等掛金控除
        pass            

    @smallbusiness_deduction.getter
    def smallbusiness_deduction(self):
        '''小規模企業共済等掛金控除
        
        [1] https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1135.htm
        '''
        return    
    
    @property
    def medical_deduction(self): # 医療費控除
        pass            

    @medical_deduction.getter
    def medical_deduction(self):
        '''医療費控除
        
        [1] https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1120.htm
        '''
        return
    
    @property
    def casualtyloss_deduction(self): # 雑損控除
        pass

    @casualtyloss_deduction.getter
    def casualtyloss_deduction(self):
        '''雑損控除

        [1] https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1110.htm

        '''
        return    

    @property
    def donation_deduction(self): # 寄付金控除
        pass

    @donation_deduction.getter
    def donation_deduction(self):
        '''寄付控除

        [1] https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1150.htm
        '''        
        return    

    @property
    def employmentincome_deduction(self):
        pass

    @employmentincome_deduction.getter
    def employmentincome_deduction(self):
        '''給与所得控除額
        給与所得から控除を差し引いた額

        [1] https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1410.htm
        '''        
        income = self.employmentincome        
        if income<=162.5:
            kojo = 55
        elif income>162.5 and income<=180:
            kojo = income*0.4-10
        elif income>180 and income<=360:
            kojo = income*0.3+8
        elif income>360 and income<=660:
            kojo = income*0.2+44
        elif income>660 and income<=850:
            kojo = income*0.1+110
        elif income>850:
            kojo = 195
        else:
            raise ValueError()        
        
        return self.employmentincome - kojo    
        
    @property
    def spose_deduction(self): # 配偶者控除
        pass
    
    @spose_deduction.getter
    def spose_deduction(self):
        '''配偶者控除もしくは配偶者特別控除

        [1] https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1195.htm
        '''
        income_me = self.net_income
        income_spose = self.sposeincome
        if income_me<=900:
            if income_spose<=103:
                kojo = 38
            elif income_spose>103 and income_spose<=150:
                kojo = 38
            elif income_spose>150 and income_spose<=155:
                kojo = 36
            elif income_spose>155 and income_spose<=160:
                kojo = 31
            elif income_spose>160 and income_spose<166.8:
                kojo = 26 
            elif income_spose>=166.8 and income_spose<175.2:
                kojo = 21
            elif income_spose>=175.2 and income_spose<183.2:
                kojo = 16
            elif income_spose>=183.2 and income_spose<190.4:
                kojo = 11
            elif income_spose>=190.4 and income_spose<197.2:
                kojo = 6
            elif income_spose>=197.2 and income_spose<201.6:
                kojo = 3
            elif income_spose>=201.6:
                kojo = 0
            else:
                raise ValueError()
        elif income_me>900 and income_me<=950:
            if income_spose<=103:
                kojo = 26
            elif income_spose>103 and income_spose<=150:
                kojo = 26
            elif income_spose>150 and income_spose<=155:
                kojo = 24
            elif income_spose>155 and income_spose<=160:
                kojo = 21
            elif income_spose>160 and income_spose<166.8:
                kojo = 18 
            elif income_spose>=166.8 and income_spose<175.2:
                kojo = 14
            elif income_spose>=175.2 and income_spose<183.2:
                kojo = 11
            elif income_spose>=183.2 and income_spose<190.4:
                kojo = 8
            elif income_spose>=190.4 and income_spose<197.2:
                kojo = 4
            elif income_spose>=197.2 and income_spose<201.6:
                kojo = 2
            elif income_spose>=201.6:
                kojo = 0
            else:
                raise ValueError()            
        elif income_me>950 and income_me<=1000:
            if income_spose<=103:
                kojo = 13
            elif income_spose>103 and income_spose<=150:
                kojo = 13
            elif income_spose>150 and income_spose<=155:
                kojo = 12
            elif income_spose>155 and income_spose<=160:
                kojo = 11
            elif income_spose>160 and income_spose<166.8:
                kojo = 9 
            elif income_spose>=166.8 and income_spose<175.2:
                kojo = 7
            elif income_spose>=175.2 and income_spose<183.2:
                kojo = 6
            elif income_spose>=183.2 and income_spose<190.4:
                kojo = 4
            elif income_spose>=190.4 and income_spose<197.2:
                kojo = 2
            elif income_spose>=197.2 and income_spose<201.6:
                kojo = 1
            elif income_spose>=201.6:
                kojo = 0
            else:
                raise ValueError()            
        elif income_me>1000:
            kojo = 0
        else:
            raise ValueError('!')
        return kojo

    @property # 不動産の控除
    def realpropertyincome_deduction(self):
        pass

    @realpropertyincome_deduction.getter
    def realpropertyincome_deduction(self):
        '''不動産所得
        総収入額から必要経費と青色特別控除額をひいたもの。
        '''
        return self.realpropertyincome - self.hudosankeihi - self.aoirokojo    

    def get_tax(self,ratio=False):
        '''課税標準をもとに所得税を得る

        # https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2260.htm

        '''
        income = self.tax_base
        if income<195:
            tax = income*0.05
        elif income>=195 and income<330:
            tax = income*0.10-9.75
        elif income>=330 and income<695:
            tax = income*0.20-42.75
        elif income>=695 and income<900:
            tax = income*0.23-63.60
        elif income>=900 and income<1800:
            tax = income*0.33-153.60
        elif income>=1800 and income<4000:
            tax = income*0.40-279.60
        elif income>=4000:
            tax = income*0.45-479.60
        else:
            raise ValueError('!')

        if self.net_income==0.0:
            return 0
        
        if ratio:
            tax /= self.net_income
            tax *= 100
        
        if tax <=0:
            tax = 0
            
        return tax    
