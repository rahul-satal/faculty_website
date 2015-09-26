# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AcadAct',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.CharField(max_length=30, db_column='User_Id')),
                ('year', models.CharField(max_length=10, db_column='Year')),
                ('gen_info_aq', models.CharField(max_length=5, db_column='Gen_Info_AQ')),
                ('gen_info_noc', models.CharField(max_length=30, db_column='Gen_Info_Noc')),
                ('gen_info_place', models.CharField(max_length=30, db_column='Gen_Info_Place')),
                ('gen_info_duration', models.CharField(max_length=30, db_column='Gen_Info_Duration')),
                ('gen_info_sa', models.CharField(max_length=30, db_column='Gen_Info_SA')),
                ('gen_info_aqyear', models.CharField(max_length=30, db_column='Gen_Info_Aqyear')),
                ('gen_info_asc', models.CharField(max_length=5, db_column='Gen_Info_ASC')),
            ],
            options={
                'db_table': 'acad_act',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Enclosures',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.CharField(max_length=30, db_column='User_Id')),
                ('year', models.CharField(max_length=20, db_column='Year')),
                ('sno', models.IntegerField(db_column='SNo')),
                ('enclosure', models.CharField(max_length=1000, db_column='Enclosure')),
            ],
            options={
                'db_table': 'enclosures',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GenInfo',
            fields=[
                ('user_id', models.CharField(max_length=30, serialize=False, primary_key=True, db_column='User_Id')),
                ('gen_info_name', models.CharField(max_length=30, db_column='Gen_Info_Name')),
                ('gen_info_fname', models.CharField(max_length=30, db_column='Gen_Info_Fname')),
                ('gen_info_mname', models.CharField(max_length=30, db_column='Gen_Info_Mname')),
                ('gen_info_department', models.CharField(max_length=30, db_column='Gen_Info_Department')),
                ('gen_info_cd', models.CharField(max_length=30, db_column='Gen_Info_CD')),
                ('gen_info_gp', models.FloatField(db_column='Gen_Info_GP')),
                ('gen_info_dlp', models.DateField(db_column='Gen_Info_DLP')),
                ('gen_info_afc', models.CharField(max_length=30, db_column='Gen_Info_AFC')),
                ('gen_info_pa', models.CharField(max_length=30, db_column='Gen_Info_PA')),
                ('gen_info_tno', models.FloatField(db_column='Gen_Info_TNO')),
                ('gen_info_email', models.CharField(max_length=30, db_column='Gen_Info_Email')),
            ],
            options={
                'db_table': 'gen_info',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('path', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'image',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Orie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.CharField(max_length=30, db_column='User_Id')),
                ('year', models.CharField(max_length=20, db_column='Year')),
                ('sno', models.IntegerField(db_column='SNo')),
                ('details', models.CharField(max_length=1000, db_column='Details')),
            ],
            options={
                'db_table': 'orie',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TeachApb',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.CharField(max_length=30, db_column='User_Id')),
                ('year', models.CharField(max_length=10, db_column='Year')),
                ('teach_apb_tno', models.CharField(max_length=50, db_column='Teach_APB_TNO')),
                ('teach_apb_bep', models.CharField(max_length=50, db_column='Teach_APB_BEP')),
                ('teach_apb_issn', models.CharField(max_length=30, db_column='Teach_APB_ISSN')),
                ('teach_apb_wpr', models.CharField(max_length=50, db_column='Teach_APB_WPR')),
                ('teach_apb_noc', models.IntegerField(db_column='Teach_APB_NOC')),
                ('teach_apb_ma', models.CharField(max_length=20, db_column='Teach_APB_MA')),
                ('teach_apb_api', models.IntegerField(db_column='Teach_APB_API')),
            ],
            options={
                'db_table': 'teach_apb',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TeachBpe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.CharField(max_length=30, db_column='User_Id')),
                ('year', models.CharField(max_length=10, db_column='Year')),
                ('teach_bpe_tpn', models.CharField(max_length=50, db_column='Teach_BPE_TPN')),
                ('teach_bpe_tba', models.CharField(max_length=50, db_column='Teach_BPE_TBA')),
                ('teach_bpe_pissn', models.CharField(max_length=30, db_column='Teach_BPE_PISSN')),
                ('teach_bpe_wpr', models.CharField(max_length=50, db_column='Teach_BPE_WPR')),
                ('teach_bpe_noc', models.IntegerField(db_column='Teach_BPE_NOC')),
                ('teach_bpe_yn', models.TextField(db_column='Teach_BPE_YN')),
                ('teach_bpe_api', models.IntegerField(db_column='Teach_BPE_API')),
            ],
            options={
                'db_table': 'teach_bpe',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TeachClmi',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.CharField(max_length=30, db_column='User_Id')),
                ('year', models.CharField(max_length=10, db_column='Year')),
                ('teach_clmi_toa', models.CharField(max_length=100, db_column='Teach_CLMI_TOA')),
                ('teach_clmi_ysr', models.CharField(max_length=30, db_column='Teach_CLMI_YSR')),
                ('teach_clmi_api', models.IntegerField(db_column='Teach_CLMI_API')),
            ],
            options={
                'db_table': 'teach_clmi',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TeachCpc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.CharField(max_length=30, db_column='User_Id')),
                ('year', models.CharField(max_length=10, db_column='Year')),
                ('teach_cpc_title', models.CharField(max_length=50, db_column='Teach_CPC_Title')),
                ('teach_cpc_agency', models.CharField(max_length=50, db_column='Teach_CPC_Agency')),
                ('teach_cpc_period', models.IntegerField(db_column='Teach_CPC_Period')),
                ('teach_cpc_gam', models.FloatField(db_column='Teach_CPC_GAM')),
                ('teach_cpc_wpd', models.CharField(max_length=50, db_column='Teach_CPC_WPD')),
                ('teach_cpc_api', models.IntegerField(db_column='Teach_CPC_API')),
            ],
            options={
                'db_table': 'teach_cpc',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TeachEcfa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.CharField(max_length=30, db_column='User_Id')),
                ('year', models.CharField(max_length=10, db_column='Year')),
                ('teach_ecfa_toa', models.CharField(max_length=150, db_column='Teach_ECFA_TOA')),
                ('teach_ecfa_ah', models.CharField(max_length=30, db_column='Teach_ECFA_AH')),
                ('teach_ecfa_api', models.IntegerField(db_column='Teach_ECFA_API')),
            ],
            options={
                'db_table': 'teach_ecfa',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TeachEdap',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.CharField(max_length=30, db_column='User_Id')),
                ('year', models.CharField(max_length=10, db_column='Year')),
                ('teach_edap_ted', models.CharField(max_length=100, db_column='Teach_EDAP_TED')),
                ('teach_edap_da', models.CharField(max_length=30, db_column='Teach_EDAP_DA')),
                ('teach_edap_eco', models.CharField(max_length=30, db_column='Teach_EDAP_ECO')),
                ('teach_edap_api', models.CharField(max_length=30, db_column='Teach_EDAP_API')),
            ],
            options={
                'db_table': 'teach_edap',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TeachFcp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.CharField(max_length=30, db_column='User_Id')),
                ('year', models.CharField(max_length=10, db_column='Year')),
                ('teach_fcp_tno', models.CharField(max_length=50, db_column='Teach_FCP_TNO')),
                ('teach_fcp_bep', models.CharField(max_length=50, db_column='Teach_FCP_BEP')),
                ('teach_fcp_issn', models.CharField(max_length=30, db_column='Teach_FCP_ISSN')),
                ('teach_fcp_noc', models.IntegerField(db_column='Teach_FCP_NOC')),
                ('teach_fcp_ma', models.TextField(db_column='Teach_FCP_MA')),
                ('teach_fcp_api', models.IntegerField(db_column='Teach_FCP_API')),
            ],
            options={
                'db_table': 'teach_fcp',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TeachFdp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.CharField(max_length=30, db_column='User_Id')),
                ('year', models.CharField(max_length=10, db_column='Year')),
                ('teach_fdp_programme', models.CharField(max_length=150, db_column='Teach_FDP_Programme')),
                ('teach_fdp_duration', models.CharField(max_length=20, db_column='Teach_FDP_Duration')),
                ('teach_fdp_organized', models.CharField(max_length=150, db_column='Teach_FDP_Organized')),
                ('teach_fdp_api', models.IntegerField(db_column='Teach_FDP_API')),
            ],
            options={
                'db_table': 'teach_fdp',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TeachIlc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.CharField(max_length=30, db_column='User_Id')),
                ('year', models.CharField(max_length=10, db_column='Year')),
                ('teach_ilc_tol', models.CharField(max_length=50, db_column='Teach_ILC_TOL')),
                ('teach_ilc_tcs', models.CharField(max_length=50, db_column='Teach_ILC_TCS')),
                ('teach_ilc_doe', models.DateField(db_column='Teach_ILC_DOE')),
                ('teach_ilc_organized', models.CharField(max_length=50, db_column='Teach_ILC_Organized')),
                ('teach_ilc_wins', models.CharField(max_length=15, db_column='Teach_ILC_WINS')),
                ('teach_ilc_api', models.IntegerField(db_column='Teach_ILC_API')),
            ],
            options={
                'db_table': 'teach_ilc',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TeachLstp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.CharField(max_length=30, db_column='User_Id')),
                ('year', models.CharField(max_length=10, db_column='Year')),
                ('teach_lstp_course', models.CharField(max_length=100, db_column='Teach_LSTP_Course')),
                ('teach_lstp_level', models.CharField(max_length=30, db_column='Teach_LSTP_Level')),
                ('teach_lstp_mot', models.CharField(max_length=150, db_column='Teach_LSTP_MOT')),
                ('teach_lstp_noca', models.CharField(max_length=100, db_column='Teach_LSTP_NOCA')),
                ('teach_lstp_nocc', models.IntegerField(db_column='Teach_LSTP_NOCC')),
                ('teach_lstp_practicals', models.CharField(max_length=70, db_column='Teach_LSTP_Practicals')),
                ('teach_lstp_ctdr', models.CharField(max_length=50, db_column='Teach_LSTP_CTDR')),
                ('teach_lstp_ctapi', models.IntegerField(db_column='Teach_LSTP_CTAPI')),
                ('teach_lstp_tlapi', models.IntegerField(db_column='Teach_LSTP_TLAPI')),
            ],
            options={
                'db_table': 'teach_lstp',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TeachOpc',
            fields=[
                ('user_id', models.CharField(max_length=30, serialize=False, primary_key=True, db_column='User_Id')),
                ('year', models.CharField(max_length=10, db_column='Year')),
                ('teach_opc_title', models.CharField(max_length=50, db_column='Teach_OPC_Title')),
                ('teach_opc_agency', models.CharField(max_length=50, db_column='Teach_OPC_Agency')),
                ('teach_opc_period', models.CharField(max_length=20, db_column='Teach_OPC_Period')),
                ('teach_opc_gam', models.FloatField(db_column='Teach_OPC_GAM')),
                ('teach_opc_api', models.IntegerField(db_column='Teach_OPC_API')),
            ],
            options={
                'db_table': 'teach_opc',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TeachPda',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.CharField(max_length=30, db_column='User_Id')),
                ('year', models.CharField(max_length=10, db_column='Year')),
                ('teach_pda_toa', models.CharField(max_length=150, db_column='Teach_PDA_TOA')),
                ('teach_pda_ywr', models.CharField(max_length=50, db_column='Teach_PDA_YWR')),
                ('teach_pda_api', models.IntegerField(db_column='Teach_PDA_API')),
            ],
            options={
                'db_table': 'teach_pda',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TeachPpc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.CharField(max_length=30, db_column='User_Id')),
                ('year', models.CharField(max_length=10, db_column='Year')),
                ('teach_ppc_tpp', models.CharField(max_length=50, db_column='Teach_PPC_TPP')),
                ('teach_ppc_tcs', models.CharField(max_length=50, db_column='Teach_PPC_TCS')),
                ('teach_ppc_doe', models.DateField(db_column='Teach_PPC_DOE')),
                ('teach_ppc_organized', models.CharField(max_length=50, db_column='Teach_PPC_Organized')),
                ('teach_ppc_wins', models.TextField(db_column='Teach_PPC_WINS')),
                ('teach_ppc_api', models.IntegerField(db_column='Teach_PPC_API')),
            ],
            options={
                'db_table': 'teach_ppc',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TeachPpij',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.CharField(max_length=30, db_column='User_Id')),
                ('year', models.CharField(max_length=11, db_column='Year')),
                ('teach_ppij_tno', models.CharField(max_length=30, db_column='Teach_PPIJ_TNO')),
                ('teach_ppij_journal', models.CharField(max_length=30, db_column='Teach_PPIJ_Journal')),
                ('teach_ppij_isbn', models.CharField(max_length=30, db_column='Teach_PPIJ_ISBN')),
                ('teach_ppij_pr', models.CharField(max_length=30, db_column='Teach_PPIJ_PR')),
                ('teach_ppij_nca', models.IntegerField(db_column='Teach_PPIJ_NCA')),
                ('teach_ppij_ma', models.CharField(max_length=30, db_column='Teach_PPIJ_MA')),
                ('teach_ppij_api', models.IntegerField(db_column='Teach_PPIJ_API')),
            ],
            options={
                'db_table': 'teach_ppij',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TeachRg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.CharField(max_length=30, db_column='User_Id')),
                ('year', models.CharField(max_length=11, db_column='Year')),
                ('teach_rg_ne', models.CharField(max_length=30, db_column='Teach_RG_NE')),
                ('teach_rg_ts', models.CharField(max_length=50, db_column='Teach_RG_TS')),
                ('teach_rg_da', models.CharField(max_length=50, db_column='Teach_RG_DA')),
                ('teach_rg_api', models.IntegerField(db_column='Teach_RG_API')),
            ],
            options={
                'db_table': 'teach_rg',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TeachRimc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.CharField(max_length=30, db_column='User_Id')),
                ('year', models.CharField(max_length=11, db_column='Year')),
                ('teach_rimc_course', models.CharField(max_length=100, db_column='Teach_RIMC_Course')),
                ('teach_rimc_consulted', models.CharField(max_length=255, db_column='Teach_RIMC_Consulted')),
                ('teach_rimc_prescribed', models.CharField(max_length=255, db_column='Teach_RIMC_Prescribed')),
                ('teach_rimc_arp', models.CharField(max_length=255, db_column='Teach_RIMC_ARP')),
            ],
            options={
                'db_table': 'teach_rimc',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TeachTlm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.CharField(max_length=30, db_column='User_Id')),
                ('year', models.CharField(max_length=11, db_column='Year')),
                ('teach_tlm_sd', models.CharField(max_length=255, db_column='Teach_TLM_SD')),
                ('teach_tlm_api', models.IntegerField(db_column='Teach_TLM_API')),
            ],
            options={
                'db_table': 'teach_tlm',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Userinfo',
            fields=[
                ('user_id', models.CharField(max_length=30, serialize=False, primary_key=True, db_column='User_Id')),
                ('pwd', models.CharField(max_length=30, db_column='Pwd')),
            ],
            options={
                'db_table': 'userinfo',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('about_desc', models.TextField(max_length=5000, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'About',
                'verbose_name_plural': 'About You',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Achievements',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(max_length=500, verbose_name='Description')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=25)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Car2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=25)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name="Employer's Name")),
                ('pin', models.CharField(max_length=50, verbose_name="Employer's PIN")),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Engine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=25)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Engine2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=25)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Example',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default='Rahul', max_length=25)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Myfriend',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Mystudent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Myteacher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=80)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, editable=False)),
                ('faculty_pic', models.ImageField(upload_to='Images/Pic')),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profile',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('place', models.OneToOneField(primary_key=True, serialize=False, to='website.Place')),
                ('serves_hot_dogs', models.BooleanField(default=False)),
                ('serves_pizza', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Waiter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('restaurant', models.ForeignKey(to='website.Restaurant')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='employer',
            unique_together=set([('name', 'pin')]),
        ),
        migrations.AddField(
            model_name='car2',
            name='engine',
            field=models.ForeignKey(to='website.Engine2', unique=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='car',
            name='engine',
            field=models.OneToOneField(to='website.Engine'),
            preserve_default=True,
        ),
    ]
