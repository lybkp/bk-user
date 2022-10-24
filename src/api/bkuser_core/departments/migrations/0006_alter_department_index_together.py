# Generated by Django 3.2.15 on 2022-09-19 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("departments", "0005_auto_20210413_1702"),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name="department",
            index_together={("parent_id", "tree_id", "lft"), ("tree_id", "lft", "rght")},
        ),
        migrations.RunSQL(
            sql="alter table departments_department drop index `departments_department_tree_id_28cdc253`;",
            reverse_sql="alter table departments_department add index `departments_department_tree_id_28cdc253` (`tree_id`);",
        ),
        migrations.RunSQL(
            sql="alter table departments_department drop index `departments_department_parent_id_cc8b848e`;",
            reverse_sql="alter table departments_department add index `departments_department_parent_id_cc8b848e` (`parent_id`);",
        ),
    ]
