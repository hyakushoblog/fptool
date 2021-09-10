from person import Residents    
        
if __name__=='__main__':
    import matplotlib.pyplot as plt
    import numpy as np
    from matplotlib import rcParams
    rcParams['font.family'] = 'sans-serif'
    rcParams['font.sans-serif'] = ['Hiragino Maru Gothic Pro',
                                   'Yu Gothic', 'Meirio', 'Takao',
                                   'IPAexGothic', 'IPAPGothic',
                                   'VL PGothic', 'Noto Sans CJK JP']

      
    # 自分(夫)と妻を定義
    wife = Residents(spose=False)
    me = Residents(spose=wife)

    # 収入所得のリスト    
    employmentincome_me = np.arange(0,1250,20) #本人の収入所得額(控除前)
    income_spose = np.linspace(103,202,2).astype(int)#配偶者の所得合計額(控除前)    
    vect_get_incometax = np.vectorize(me.get_incometax)
    
    # プロット
    ratio = False
    fig,ax = plt.subplots(1,1,figsize=(8,5))
    for _income_spose in income_spose:
        if ratio:
            ax.plot(employmentincome_me,
                    vect_get_incometax(employmentincome=employmentincome_me,
                                       realpropertyincome=0,
                                       sposeincome=_income_spose,ratio=True),
                    'o-',markersize=3,
                    label='所得税(配偶者の合計所得が{0}万円の場合)'.format(_income_spose))
        else:
            ax.plot(employmentincome_me,
                    vect_get_incometax(employmentincome=employmentincome_me,
                                       realpropertyincome=0,
                                       sposeincome=_income_spose),'o-',markersize=3,
                    label='所得税(配偶者の合計所得が{0}万円の場合)'.format(_income_spose))
            
    ax.legend()
    ax.hlines(0,0,1250,linestyle='--',color='gray')
    ax.vlines(1000,-100,200,linestyle='--',color='gray')
    ax.set_xlim(0,1200)
    ax.set_xlabel('扶養者の所得額 [万円]')
    if ratio:
        ax.set_ylabel('割合[%]')
        ax.set_ylim(0,15)        
    else:
        ax.set_ylabel('課税額 [万円]')
        ax.set_ylim(0,150)        
    plt.savefig('result.png')
    plt.close()
