# Generated by Django 2.2.16 on 2021-01-12 13:36

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0241_sort_categories_by_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enforcementactiondisposition',
            old_name='name',
            new_name='final_disposition',
        ),
        migrations.RenameField(
            model_name='enforcementactiondisposition',
            old_name='civil_money_penalties',
            new_name='final_order_civil_money_penalty',
        ),
        migrations.RemoveField(
            model_name='enforcementactiondisposition',
            name='date_filed',
        ),
        migrations.RemoveField(
            model_name='enforcementactiondisposition',
            name='institution_type',
        ),
        migrations.RemoveField(
            model_name='enforcementactiondisposition',
            name='settled',
        ),
        migrations.RemoveField(
            model_name='enforcementactiondisposition',
            name='status',
        ),
        migrations.RemoveField(
            model_name='enforcementactiondisposition',
            name='total_consumer_relief',
        ),
        migrations.RemoveField(
            model_name='enforcementactionstatus',
            name='institution',
        ),
        migrations.AddField(
            model_name='enforcementactiondisposition',
            name='estimated_consumers_entitled_to_relief',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='enforcementactiondisposition',
            name='final_disposition_type',
            field=models.CharField(blank=True, choices=[('Final Order', 'Final Order'), ('Dismissal', 'Dismissal')], max_length=15),
        ),
        migrations.AddField(
            model_name='enforcementactiondisposition',
            name='final_order_civil_money_penalty_suspended',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=13),
        ),
        migrations.AddField(
            model_name='enforcementactiondisposition',
            name='final_order_consumer_redress',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=13),
        ),
        migrations.AddField(
            model_name='enforcementactiondisposition',
            name='final_order_consumer_redress_suspended',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=13),
        ),
        migrations.AddField(
            model_name='enforcementactiondisposition',
            name='final_order_disgorgement',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=13),
        ),
        migrations.AddField(
            model_name='enforcementactiondisposition',
            name='final_order_disgorgement_suspended',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=13),
        ),
        migrations.AddField(
            model_name='enforcementactiondisposition',
            name='final_order_other_consumer_relief',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=13),
        ),
        migrations.AddField(
            model_name='enforcementactiondisposition',
            name='final_order_other_consumer_relief_suspended',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=13),
        ),
        migrations.AddField(
            model_name='enforcementactionpage',
            name='initial_filing_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='enforcementactionpage',
            name='public_enforcement_action',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='enforcementactionpage',
            name='settled_or_contested_at_filing',
            field=models.CharField(blank=True, choices=[('Settled', 'Settled'), ('Contested', 'Contested')], max_length=10),
        ),
        migrations.CreateModel(
            name='EnforcementActionStatute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statute', models.CharField(choices=[('CFPA Deceptive', 'Consumer Financial Protection Act - Deceptive Acts or Practices'), ('CFPA Unfair', 'Consumer Financial Protection Act - Unfair Acts or Practices'), ('CFPA Abusive', 'Consumer Financial Protection Act - Abusive Acts or Practices'), ('CFPA', 'Consumer Financial Protection Act - Other'), ('AMTPA', 'Alternative Mortgage Transaction Parity Act/Regulation D'), ('CLA', 'Consumer Leasing Act/Regulation M'), ('Credit Practice Rules', 'Credit Practices Rule'), ('EFTA/Regulation E', 'Electronic Fund Transfer Act/Regulation E'), ('ECOA/Regulation B', 'Equal Credit Opportunity Act/Regulation B'), ('FCBA', 'Fair Credit Billing Act'), ('FCRA/Regulation V', 'Fair Credit Reporting Act/Regulation V'), ('FDCPA', 'Fair Debt Collection Practices Act/Regulation F'), ('FDIA', 'Federal Deposit Insurance Act/Regulation I'), ('GLBA/Regulation P', 'Gramm-Leach-Bliley Act/Regulation P'), ('HMDA', 'Home Mortgage Disclosure Act/Regulation C'), ('HOEPA', 'Home Ownership and Equity Protection Act'), ('HOPA', 'Home Owners Protection Act'), ('ILSFDA', 'Interstate Land Sales Full Disclosure Act/Regulation J, K, and L'), ('Military Lending Act', 'Military Lending Act'), ('Regulation N (MAP Rule)', 'Mortgage Acts and Practices – Advertising Final Rule (Regulation N)'), ('Regulation O (MARS Rule)', 'Mortgage Assistance Relief Services Rule (Regulation O)'), ('MRAPLA', 'Mortgage Reform and Anti-Predatory Lending Act'), ('RESPA', 'Real Estate Settlement Procedures Act/Regulation X'), ('SMLA', 'S.A.F.E. Mortgage Licensing Act/Regulation H'), ('Telemarketing Sales Rule (TSR)', 'Telemarketing Sales Rule'), ('TILA/Regulation Z', 'Truth in Lending Act/Regulation Z'), ('TISA/Regulation DD', 'Truth in Savings Act/Regulation DD')], max_length=30)),
                ('action', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='statutes', to='v1.EnforcementActionPage')),
            ],
        ),
        migrations.CreateModel(
            name='EnforcementActionProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(choices=[('Auto Finance Origination', 'Auto Finance Origination'), ('Auto Finance Servicing', 'Auto Finance Servicing'), ('Consumer Reporting Agencies', 'Consumer Reporting Agencies'), ('Consumer Reporting ? User', 'Consumer Reporting - User'), ('Credit Cards', 'Credit Cards'), ('Credit Repair', 'Credit Repair'), ('Debt Collection', 'Debt Collection'), ('Debt Relief', 'Debt Relief'), ('Deposits', 'Deposits'), ('Furnishing', 'Furnishing'), ('Mortgage Origination', 'Mortgage Origination'), ('Mortgage Servicing', 'Mortgage Servicing'), ('Payments', 'Payments'), ('Prepaid', 'Prepaid'), ('Remittances', 'Remittances'), ('Short Term, Small Dollar', 'Short Term, Small Dollar'), ('Business Lending (ECOA)', 'Business Lending (ECOA)'), ('Student Loan Origination', 'Student Loan Origination'), ('Student Loan Servicing', 'Student Loan Servicing'), ('Other Consumer Lending', 'Other Consumer Lending'), ('Other Consumer Products (Not Lending)', 'Other Consumer Product (not lending)')], max_length=50)),
                ('action', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='v1.EnforcementActionPage')),
            ],
        ),
        migrations.CreateModel(
            name='EnforcementActionDefendantType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('defendant_type', models.CharField(blank=True, choices=[('Non-Bank', 'Nonbank'), ('Bank', 'Bank'), ('Individual', 'Individual')], max_length=15)),
                ('action', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='defendant_types', to='v1.EnforcementActionPage')),
            ],
        ),
        migrations.CreateModel(
            name='EnforcementActionAtRisk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('at_risk_group', models.CharField(choices=[('Older Americans', 'Older Americans'), ('Servicemembers', 'Servicemembers'), ('Limited English Proficiency', 'Limited English Proficiency'), ('Fair Lending', 'Fair Lending'), ('Students', 'Students')], max_length=30)),
                ('action', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='at_risk_groups', to='v1.EnforcementActionPage')),
            ],
        ),
    ]
