#%% [Gera Informações da PI Planning]

#######################################################################################
#######################################################################################
##                  Gera Informações da PI Planning - PI/CA                          ##
##                                                                                   ##
## Desenvolvido por: Fábio Fumio Wada                                                ##
#######################################################################################
#######################################################################################


# %% -----> [Objetivos] - Lista Objetivos
# fn_obj_listagem(v_pi) / fn_obj_listagem('PI09')

fn_obj_listagem('PI09')

# %% -----> [Feature] - Listagem\Lista Features
#    Parâmetros:    "O" - Somente Objetivos (Sem Objetivos Stretch) 
#                   "S" - Somente Objetivos Stretch
#                   "F" - Todos os Objetivos
# fn_ftr_listagem(v_pi,v_opcao) / fn_ftr_listagem('PI09','F')

fn_ftr_listagem('PI09','F')

# %% -----> [Feature] - Soma Features
# fn_ftr_quantidade(v_pi)

fn_ftr_quantidade('PI09') #detalhamento dos erros podem ser obtidos com a funçao "fn_ftr_erros"

# %% -----> - [Feature] - Lista Erros Cadastrais
# Ex: 1) Feature sem um objetivo da "PI" vinculado. Ex: PI09 é oficial e possui objetivo da PI08
#     2) Feature sem objetivo
# fn_ftr_erros(v_pi) / fn_ftr_erros('PI09')

fn_ftr_erros('PI09')

# %%
