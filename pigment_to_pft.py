import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

#This is based on the pigment to PFT associations given in 
#https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2005JC003207 

#TODO: With updates from https://www.sciencedirect.com/science/article/pii/S0034425715300614

def PigmentRatioToGroups(pigment_data, chl_varname):
    #We expect pigment data to be an Dataframe with pigment concentrations
    DiagnosticPigmentList=['Fuco','Peri','Hex','But','Allo','TChlb','Zea']
    Chl=pigment_data[chl_varname]
    GroupList=['Diatoms','dinoflagellates','cryptophytes','green_flag','prochlorophytes','cyanobacteria','nano_flag','chromophytes']
    DP_subset=data[DiagnosticPigmentList]
    DP_sum=DP_subset.sum(axis=1)
    DP_estimated_tchla=(1.41*(DP_subset['Fuco']+DP_subset['Peri']))+(1.27*DP_subset['Hex'])+\
        (0.35*DP_subset['But'])+(0.6*DP_subset['Allo'])+\
        (1.01*DP_subset['TChlb'])+(0.86*DP_subset['Zea'])
    
    diatom_contribution=(1.41*DP_subset['Fuco'])/DP_estimated_tchla
    dinoflag_contribution=(1.41*DP_subset['Peri'])/DP_estimated_tchla
    crypto_contribution=(0.6*DP_subset['Allo'])/DP_estimated_tchla
    chromo_nano_contribution=(((1.27*DP_subset['Hex'])+0.35*DP_subset['But']))/DP_estimated_tchla
    cyano_prochlor_contribution=(0.86*DP_subset['Zea'])/DP_estimated_tchla
    Gflag_prochlor_contribution=(1.01*DP_subset['TChlb'])/DP_estimated_tchla

    log_Tchl_est_offset=np.log10(Chl)-np.log10(estimated_tchla)

    Groups=pd.DataFrame({'Diatoms': diatom_contribution, 'Dinoflag':dinoflag_contribution,'cyano_prochlor':cyano_prochlor_contribution, 'log_chl_mismatch': log_Tchl_est_offset})

    return Groups


