import pymel.core as pm

from bsPipe.bs_ui import bs_qui

reload(bs_qui)

bsLS = ['mo_l_smile',
        'mo_r_smile',
        'mo_l_sad',
        'mo_r_sad',
        'mo_l_small',
        'mo_r_small',
        'mo_l_wide',
        'mo_r_wide',
        'mo_l_puff',
        'mo_r_puff',
        'mo_l_disgust',
        'mo_r_disgust',
        'mo_l_up_sneer',
        'mo_r_up_sneer',
        'mo_l_dn_sneer',
        'mo_r_dn_sneer',
        'mo_up',
        'mo_dn',
        'mo_laugh',
        'mo_openSmile',
        'mo_jawDrop',
        'mo_ahh',
        'mo_ohh',
        'ph_a',
        'ph_e',
        'ph_o',
        'ph_u',
        'ph_f',
        'ph_l',
        'ph_mbp',
        'ns_l_up',
        'ns_r_up',
        'ns_l_dn',
        'ns_r_dn',
        'eb_l_up',
        'eb_r_up',
        'eb_l_dn',
        'eb_r_dn',
        'eb_l_in',
        'eb_r_in',
        'eb_l_out',
        'eb_r_out',
        'eb_l_sad',
        'eb_r_sad',
        'eb_l_flat',
        'eb_r_flat',
        'eb_l_angry',
        'eb_r_angry',
        'eb_l_scare',
        'eb_r_scare',
        'eb_l_embarrassed',
        'eb_r_embarrassed',
        'eb_l_sulk',
        'eb_r_sulk',
        'eb_l_worried',
        'eb_r_worried',
        'eb_l_surprise',
        'eb_r_surprise',
        'ey_l_up_close',
        'ey_r_up_close',
        'ey_l_dn_close',
        'ey_r_dn_close',
        'ey_l_up_open',
        'ey_r_up_open',
        'ey_l_dn_open',
        'ey_r_dn_open',
        'ey_l_angry_bl',
        'ey_r_angry_bl',
        'ey_l_scare',
        'ey_r_scare',
        'ey_l_embarrassed',
        'ey_r_embarrassed',
        'ey_l_sulk',
        'ey_r_sulk',
        'ey_l_happy_bl',
        'ey_r_happy_bl',
        'ey_l_sad_bl',
        'ey_r_sad_bl',
        'ey_l_wideOpen',
        'ey_r_wideOpen',
        'ey_l_squint',
        'ey_r_squint',
        'ey_l_tight_bl',
        'ey_r_tight_bl',
        ]


def bswExtract(sel):
    if not sel:
        bs_qui.bs_displayMessage('error', 'Please select geometries.')
        return False
    mainGrp = pm.createNode('transform', n='blendshapeMain_grp', ss=True)
    for each in bsLS:
        shapeGrp = pm.createNode('transform', n=each + '_BSGrp', ss=True)
        for eachGeo in sel:
            dupShape = pm.duplicate(eachGeo, rr=True, n=each + '__' + eachGeo)
            pm.parent(dupShape, shapeGrp)
        pm.parent(shapeGrp, mainGrp)
