# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class AcadAct(models.Model):
    user_id = models.CharField(db_column='User_Id', max_length=30)  # Field name made lowercase.
    year = models.CharField(db_column='Year', max_length=10)  # Field name made lowercase.
    gen_info_aq = models.CharField(db_column='Gen_Info_AQ', max_length=5)  # Field name made lowercase.
    gen_info_noc = models.CharField(db_column='Gen_Info_Noc', max_length=30)  # Field name made lowercase.
    gen_info_place = models.CharField(db_column='Gen_Info_Place', max_length=30)  # Field name made lowercase.
    gen_info_duration = models.CharField(db_column='Gen_Info_Duration', max_length=30)  # Field name made lowercase.
    gen_info_sa = models.CharField(db_column='Gen_Info_SA', max_length=30)  # Field name made lowercase.
    gen_info_aqyear = models.CharField(db_column='Gen_Info_Aqyear', max_length=30)  # Field name made lowercase.
    gen_info_asc = models.CharField(db_column='Gen_Info_ASC', max_length=5)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'acad_act'


class Enclosures(models.Model):
    user_id = models.CharField(db_column='User_Id', max_length=30)  # Field name made lowercase.
    year = models.CharField(db_column='Year', max_length=20)  # Field name made lowercase.
    sno = models.IntegerField(db_column='SNo')  # Field name made lowercase.
    enclosure = models.CharField(db_column='Enclosure', max_length=1000)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'enclosures'


class GenInfo(models.Model):
    user_id = models.CharField(db_column='User_Id', primary_key=True, max_length=30)  # Field name made lowercase.
    gen_info_name = models.CharField(db_column='Gen_Info_Name', max_length=30)  # Field name made lowercase.
    gen_info_fname = models.CharField(db_column='Gen_Info_Fname', max_length=30)  # Field name made lowercase.
    gen_info_mname = models.CharField(db_column='Gen_Info_Mname', max_length=30)  # Field name made lowercase.
    gen_info_department = models.CharField(db_column='Gen_Info_Department', max_length=30)  # Field name made lowercase.
    gen_info_cd = models.CharField(db_column='Gen_Info_CD', max_length=30)  # Field name made lowercase.
    gen_info_gp = models.FloatField(db_column='Gen_Info_GP')  # Field name made lowercase.
    gen_info_dlp = models.DateField(db_column='Gen_Info_DLP')  # Field name made lowercase.
    gen_info_afc = models.CharField(db_column='Gen_Info_AFC', max_length=30)  # Field name made lowercase.
    gen_info_pa = models.CharField(db_column='Gen_Info_PA', max_length=30)  # Field name made lowercase.
    gen_info_tno = models.FloatField(db_column='Gen_Info_TNO')  # Field name made lowercase.
    gen_info_email = models.CharField(db_column='Gen_Info_Email', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'gen_info'


class Image(models.Model):
    name = models.CharField(max_length=20)
    path = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'image'


class Orie(models.Model):
    user_id = models.CharField(db_column='User_Id', max_length=30)  # Field name made lowercase.
    year = models.CharField(db_column='Year', max_length=20)  # Field name made lowercase.
    sno = models.IntegerField(db_column='SNo')  # Field name made lowercase.
    details = models.CharField(db_column='Details', max_length=1000)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orie'


class TeachApb(models.Model):
    user_id = models.CharField(db_column='User_Id', max_length=30)  # Field name made lowercase.
    year = models.CharField(db_column='Year', max_length=10)  # Field name made lowercase.
    teach_apb_tno = models.CharField(db_column='Teach_APB_TNO', max_length=50)  # Field name made lowercase.
    teach_apb_bep = models.CharField(db_column='Teach_APB_BEP', max_length=50)  # Field name made lowercase.
    teach_apb_issn = models.CharField(db_column='Teach_APB_ISSN', max_length=30)  # Field name made lowercase.
    teach_apb_wpr = models.CharField(db_column='Teach_APB_WPR', max_length=50)  # Field name made lowercase.
    teach_apb_noc = models.IntegerField(db_column='Teach_APB_NOC')  # Field name made lowercase.
    teach_apb_ma = models.CharField(db_column='Teach_APB_MA', max_length=20)  # Field name made lowercase.
    teach_apb_api = models.IntegerField(db_column='Teach_APB_API')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'teach_apb'


class TeachBpe(models.Model):
    user_id = models.CharField(db_column='User_Id', max_length=30)  # Field name made lowercase.
    year = models.CharField(db_column='Year', max_length=10)  # Field name made lowercase.
    teach_bpe_tpn = models.CharField(db_column='Teach_BPE_TPN', max_length=50)  # Field name made lowercase.
    teach_bpe_tba = models.CharField(db_column='Teach_BPE_TBA', max_length=50)  # Field name made lowercase.
    teach_bpe_pissn = models.CharField(db_column='Teach_BPE_PISSN', max_length=30)  # Field name made lowercase.
    teach_bpe_wpr = models.CharField(db_column='Teach_BPE_WPR', max_length=50)  # Field name made lowercase.
    teach_bpe_noc = models.IntegerField(db_column='Teach_BPE_NOC')  # Field name made lowercase.
    teach_bpe_yn = models.TextField(db_column='Teach_BPE_YN')  # Field name made lowercase.
    teach_bpe_api = models.IntegerField(db_column='Teach_BPE_API')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'teach_bpe'


class TeachClmi(models.Model):
    user_id = models.CharField(db_column='User_Id', max_length=30)  # Field name made lowercase.
    year = models.CharField(db_column='Year', max_length=10)  # Field name made lowercase.
    teach_clmi_toa = models.CharField(db_column='Teach_CLMI_TOA', max_length=100)  # Field name made lowercase.
    teach_clmi_ysr = models.CharField(db_column='Teach_CLMI_YSR', max_length=30)  # Field name made lowercase.
    teach_clmi_api = models.IntegerField(db_column='Teach_CLMI_API')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'teach_clmi'


class TeachCpc(models.Model):
    user_id = models.CharField(db_column='User_Id', max_length=30)  # Field name made lowercase.
    year = models.CharField(db_column='Year', max_length=10)  # Field name made lowercase.
    teach_cpc_title = models.CharField(db_column='Teach_CPC_Title', max_length=50)  # Field name made lowercase.
    teach_cpc_agency = models.CharField(db_column='Teach_CPC_Agency', max_length=50)  # Field name made lowercase.
    teach_cpc_period = models.IntegerField(db_column='Teach_CPC_Period')  # Field name made lowercase.
    teach_cpc_gam = models.FloatField(db_column='Teach_CPC_GAM')  # Field name made lowercase.
    teach_cpc_wpd = models.CharField(db_column='Teach_CPC_WPD', max_length=50)  # Field name made lowercase.
    teach_cpc_api = models.IntegerField(db_column='Teach_CPC_API')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'teach_cpc'


class TeachEcfa(models.Model):
    user_id = models.CharField(db_column='User_Id', max_length=30)  # Field name made lowercase.
    year = models.CharField(db_column='Year', max_length=10)  # Field name made lowercase.
    teach_ecfa_toa = models.CharField(db_column='Teach_ECFA_TOA', max_length=150)  # Field name made lowercase.
    teach_ecfa_ah = models.CharField(db_column='Teach_ECFA_AH', max_length=30)  # Field name made lowercase.
    teach_ecfa_api = models.IntegerField(db_column='Teach_ECFA_API')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'teach_ecfa'


class TeachEdap(models.Model):
    user_id = models.CharField(db_column='User_Id', max_length=30)  # Field name made lowercase.
    year = models.CharField(db_column='Year', max_length=10)  # Field name made lowercase.
    teach_edap_ted = models.CharField(db_column='Teach_EDAP_TED', max_length=100)  # Field name made lowercase.
    teach_edap_da = models.CharField(db_column='Teach_EDAP_DA', max_length=30)  # Field name made lowercase.
    teach_edap_eco = models.CharField(db_column='Teach_EDAP_ECO', max_length=30)  # Field name made lowercase.
    teach_edap_api = models.CharField(db_column='Teach_EDAP_API', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'teach_edap'


class TeachFcp(models.Model):
    user_id = models.CharField(db_column='User_Id', max_length=30)  # Field name made lowercase.
    year = models.CharField(db_column='Year', max_length=10)  # Field name made lowercase.
    teach_fcp_tno = models.CharField(db_column='Teach_FCP_TNO', max_length=50)  # Field name made lowercase.
    teach_fcp_bep = models.CharField(db_column='Teach_FCP_BEP', max_length=50)  # Field name made lowercase.
    teach_fcp_issn = models.CharField(db_column='Teach_FCP_ISSN', max_length=30)  # Field name made lowercase.
    teach_fcp_noc = models.IntegerField(db_column='Teach_FCP_NOC')  # Field name made lowercase.
    teach_fcp_ma = models.TextField(db_column='Teach_FCP_MA')  # Field name made lowercase.
    teach_fcp_api = models.IntegerField(db_column='Teach_FCP_API')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'teach_fcp'


class TeachFdp(models.Model):
    user_id = models.CharField(db_column='User_Id', max_length=30)  # Field name made lowercase.
    year = models.CharField(db_column='Year', max_length=10)  # Field name made lowercase.
    teach_fdp_programme = models.CharField(db_column='Teach_FDP_Programme', max_length=150)  # Field name made lowercase.
    teach_fdp_duration = models.CharField(db_column='Teach_FDP_Duration', max_length=20)  # Field name made lowercase.
    teach_fdp_organized = models.CharField(db_column='Teach_FDP_Organized', max_length=150)  # Field name made lowercase.
    teach_fdp_api = models.IntegerField(db_column='Teach_FDP_API')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'teach_fdp'


class TeachIlc(models.Model):
    user_id = models.CharField(db_column='User_Id', max_length=30)  # Field name made lowercase.
    year = models.CharField(db_column='Year', max_length=10)  # Field name made lowercase.
    teach_ilc_tol = models.CharField(db_column='Teach_ILC_TOL', max_length=50)  # Field name made lowercase.
    teach_ilc_tcs = models.CharField(db_column='Teach_ILC_TCS', max_length=50)  # Field name made lowercase.
    teach_ilc_doe = models.DateField(db_column='Teach_ILC_DOE')  # Field name made lowercase.
    teach_ilc_organized = models.CharField(db_column='Teach_ILC_Organized', max_length=50)  # Field name made lowercase.
    teach_ilc_wins = models.CharField(db_column='Teach_ILC_WINS', max_length=15)  # Field name made lowercase.
    teach_ilc_api = models.IntegerField(db_column='Teach_ILC_API')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'teach_ilc'


class TeachLstp(models.Model):
    user_id = models.CharField(db_column='User_Id', max_length=30)  # Field name made lowercase.
    year = models.CharField(db_column='Year', max_length=10)  # Field name made lowercase.
    teach_lstp_course = models.CharField(db_column='Teach_LSTP_Course', max_length=100)  # Field name made lowercase.
    teach_lstp_level = models.CharField(db_column='Teach_LSTP_Level', max_length=30)  # Field name made lowercase.
    teach_lstp_mot = models.CharField(db_column='Teach_LSTP_MOT', max_length=150)  # Field name made lowercase.
    teach_lstp_noca = models.CharField(db_column='Teach_LSTP_NOCA', max_length=100)  # Field name made lowercase.
    teach_lstp_nocc = models.IntegerField(db_column='Teach_LSTP_NOCC')  # Field name made lowercase.
    teach_lstp_practicals = models.CharField(db_column='Teach_LSTP_Practicals', max_length=70)  # Field name made lowercase.
    teach_lstp_ctdr = models.CharField(db_column='Teach_LSTP_CTDR', max_length=50)  # Field name made lowercase.
    teach_lstp_ctapi = models.IntegerField(db_column='Teach_LSTP_CTAPI')  # Field name made lowercase.
    teach_lstp_tlapi = models.IntegerField(db_column='Teach_LSTP_TLAPI')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'teach_lstp'


class TeachOpc(models.Model):
    user_id = models.CharField(db_column='User_Id', max_length=30)  # Field name made lowercase.
    year = models.CharField(db_column='Year', max_length=10)  # Field name made lowercase.
    teach_opc_title = models.CharField(db_column='Teach_OPC_Title', max_length=50)  # Field name made lowercase.
    teach_opc_agency = models.CharField(db_column='Teach_OPC_Agency', max_length=50)  # Field name made lowercase.
    teach_opc_period = models.CharField(db_column='Teach_OPC_Period', max_length=20)  # Field name made lowercase.
    teach_opc_gam = models.FloatField(db_column='Teach_OPC_GAM')  # Field name made lowercase.
    teach_opc_api = models.IntegerField(db_column='Teach_OPC_API')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'teach_opc'


class TeachPda(models.Model):
    user_id = models.CharField(db_column='User_Id', max_length=30)  # Field name made lowercase.
    year = models.CharField(db_column='Year', max_length=10)  # Field name made lowercase.
    teach_pda_toa = models.CharField(db_column='Teach_PDA_TOA', max_length=150)  # Field name made lowercase.
    teach_pda_ywr = models.CharField(db_column='Teach_PDA_YWR', max_length=50)  # Field name made lowercase.
    teach_pda_api = models.IntegerField(db_column='Teach_PDA_API')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'teach_pda'


class TeachPpc(models.Model):
    user_id = models.CharField(db_column='User_Id', max_length=30)  # Field name made lowercase.
    year = models.CharField(db_column='Year', max_length=10)  # Field name made lowercase.
    teach_ppc_tpp = models.CharField(db_column='Teach_PPC_TPP', max_length=50)  # Field name made lowercase.
    teach_ppc_tcs = models.CharField(db_column='Teach_PPC_TCS', max_length=50)  # Field name made lowercase.
    teach_ppc_doe = models.DateField(db_column='Teach_PPC_DOE')  # Field name made lowercase.
    teach_ppc_organized = models.CharField(db_column='Teach_PPC_Organized', max_length=50)  # Field name made lowercase.
    teach_ppc_wins = models.TextField(db_column='Teach_PPC_WINS')  # Field name made lowercase.
    teach_ppc_api = models.IntegerField(db_column='Teach_PPC_API')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'teach_ppc'


class TeachPpij(models.Model):
    user_id = models.CharField(db_column='User_Id', max_length=30)  # Field name made lowercase.
    year = models.CharField(db_column='Year', max_length=11)  # Field name made lowercase.
    teach_ppij_tno = models.CharField(db_column='Teach_PPIJ_TNO', max_length=30)  # Field name made lowercase.
    teach_ppij_journal = models.CharField(db_column='Teach_PPIJ_Journal', max_length=30)  # Field name made lowercase.
    teach_ppij_isbn = models.CharField(db_column='Teach_PPIJ_ISBN', max_length=30)  # Field name made lowercase.
    teach_ppij_pr = models.CharField(db_column='Teach_PPIJ_PR', max_length=30)  # Field name made lowercase.
    teach_ppij_nca = models.IntegerField(db_column='Teach_PPIJ_NCA')  # Field name made lowercase.
    teach_ppij_ma = models.CharField(db_column='Teach_PPIJ_MA', max_length=30)  # Field name made lowercase.
    teach_ppij_api = models.IntegerField(db_column='Teach_PPIJ_API')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'teach_ppij'


class TeachRg(models.Model):
    user_id = models.CharField(db_column='User_Id', max_length=30)  # Field name made lowercase.
    year = models.CharField(db_column='Year', max_length=11)  # Field name made lowercase.
    teach_rg_ne = models.CharField(db_column='Teach_RG_NE', max_length=30)  # Field name made lowercase.
    teach_rg_ts = models.CharField(db_column='Teach_RG_TS', max_length=50)  # Field name made lowercase.
    teach_rg_da = models.CharField(db_column='Teach_RG_DA', max_length=50)  # Field name made lowercase.
    teach_rg_api = models.IntegerField(db_column='Teach_RG_API')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'teach_rg'


class TeachRimc(models.Model):
    user_id = models.CharField(db_column='User_Id', max_length=30)  # Field name made lowercase.
    year = models.CharField(db_column='Year', max_length=11)  # Field name made lowercase.
    teach_rimc_course = models.CharField(db_column='Teach_RIMC_Course', max_length=100)  # Field name made lowercase.
    teach_rimc_consulted = models.CharField(db_column='Teach_RIMC_Consulted', max_length=255)  # Field name made lowercase.
    teach_rimc_prescribed = models.CharField(db_column='Teach_RIMC_Prescribed', max_length=255)  # Field name made lowercase.
    teach_rimc_arp = models.CharField(db_column='Teach_RIMC_ARP', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'teach_rimc'


class TeachTlm(models.Model):
    user_id = models.CharField(db_column='User_Id', max_length=30)  # Field name made lowercase.
    year = models.CharField(db_column='Year', max_length=11)  # Field name made lowercase.
    teach_tlm_sd = models.CharField(db_column='Teach_TLM_SD', max_length=255)  # Field name made lowercase.
    teach_tlm_api = models.IntegerField(db_column='Teach_TLM_API')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'teach_tlm'


class Userinfo(models.Model):
    user_id = models.CharField(db_column='User_Id', primary_key=True, max_length=30)  # Field name made lowercase.
    pwd = models.CharField(db_column='Pwd', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'userinfo'



class About(models.Model):
	about_desc = models.TextField(max_length=5000)
	def __unicode__(self):              # __str__ on Python 3
        	return str(self.about_desc)

class Myteacher(models.Model):
    name = models.CharField(max_length=200)
    def __unicode__(self):              # __str__ on Python 3
        	return str(self.name)

class Myfriend(models.Model):
    name = models.CharField(max_length=200)
    def __unicode__(self):              # __str__ on Python 3
        	return str(self.name)

class Mystudent(models.Model):
    name = models.CharField(max_length=200)
    def __unicode__(self):              # __str__ on Python 3
        	return str(self.name)
    
