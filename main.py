from person import Residents    


if __name__=='__main__':
    import matplotlib.pyplot as plt
    import numpy as np
    from scipy import special
    from matplotlib import rcParams
    rcParams['font.family'] = 'sans-serif'
    rcParams['font.sans-serif'] = ['Hiragino Maru Gothic Pro',
                                   'Yu Gothic', 'Meirio', 'Takao',
                                   'IPAexGothic', 'IPAPGothic',
                                   'VL PGothic', 'Noto Sans CJK JP']
    
    # 自分(夫)と妻を定義
    wife = Residents(spose=False)
    me = Residents(spose=True)

    # 収入所得のリスト    
    employmentincome_me = np.arange(0,2000,10) #本人の収入所得額(控除前)
    income_spose = np.linspace(103,202,2).astype(int)#配偶者の所得合計額(控除前)

    # 所得税を計算する関数をベクトライズする
    vect_get_incometax = np.vectorize(me.get_incometax)
    
    # プロットする
    ratio = False
    tedori = True
    fig,ax = plt.subplots(1,1,figsize=(7,5))
    for _income_spose in income_spose:
        if ratio:
            ax.plot(employmentincome_me,
                    vect_get_incometax(employmentincome=employmentincome_me,
                                       realpropertyincome=0,
                                       sposeincome=_income_spose,ratio=True),
                    '-',markersize=1,
                    label='所得税(配偶者の合計所得が{0}万円の場合)'.format(_income_spose))
        elif not ratio and tedori:
            ax.plot(employmentincome_me,
                    employmentincome_me-vect_get_incometax(employmentincome=employmentincome_me,
                                       realpropertyincome=0,
                                       sposeincome=_income_spose),
                    'o-',markersize=1,
                    label='所得税(配偶者の合計所得が{0}万円の場合)'.format(_income_spose))
        else:
            ax.plot(employmentincome_me,
                    vect_get_incometax(employmentincome=employmentincome_me,
                                       realpropertyincome=0,
                                       sposeincome=_income_spose),
                    'o-',markersize=1,
                    label='所得税(配偶者の合計所得が{0}万円の場合)'.format(_income_spose)) 
    ax.legend()
    ax.hlines(0,0,2000,linestyle='--',color='gray')
    ax.set_xlim(0,2000)
    ax.set_xlabel('所得額 [万円]',fontsize=15)
    if ratio:
        ax.set_ylabel('課税率[%]',fontsize=15)
        ax.set_ylim(0,25)
        ax.hlines(45,0,2000,linestyle='--',color='gray')            
    elif not ratio and tedori:
        ax.set_ylabel('手取り額 [万円]',fontsize=15)
        ax.plot(employmentincome_me,employmentincome_me,'--',color='gray')
        ax.set_ylim(0,2000)
    else:
        ax.set_ylabel('課税額 [万円]',fontsize=15)
        ax.set_ylim(0,2)                
    plt.savefig('result.png')
    plt.close()
