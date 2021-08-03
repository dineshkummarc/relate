# Generated by Django 1.10.7 on 2017-12-19 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0108_alter_page_ordinal_verbose_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participationpermission',
            name='permission',
            field=models.CharField(choices=[('edit_course', 'Edit course'), ('use_admin_interface', 'Use admin interface'), ('manage_authentication_tokens', 'Manage authentication tokens'), ('impersonate_role', 'Impersonate role'), ('set_fake_time', 'Set fake time'), ('set_pretend_facility', 'Pretend to be in facility'), ('edit_course_permissions', 'Edit course permissions'), ('view_hidden_course_page', 'View hidden course page'), ('view_calendar', 'View calendar'), ('send_instant_message', 'Send instant message'), ('access_files_for', 'Access files for'), ('included_in_grade_statistics', 'Included in grade statistics'), ('skip_during_manual_grading', 'Skip during manual grading'), ('edit_exam', 'Edit exam'), ('issue_exam_ticket', 'Issue exam ticket'), ('batch_issue_exam_ticket', 'Batch issue exam ticket'), ('view_participant_masked_profile', "View participants' masked profile only"), ('view_flow_sessions_from_role', 'View flow sessions from role'), ('view_gradebook', 'View gradebook'), ('edit_grading_opportunity', 'Edit grading opportunity'), ('assign_grade', 'Assign grade'), ('view_grader_stats', 'View grader stats'), ('batch_import_grade', 'Batch-import grades'), ('batch_export_grade', 'Batch-export grades'), ('batch_download_submission', 'Batch-download submissions'), ('impose_flow_session_deadline', 'Impose flow session deadline'), ('batch_impose_flow_session_deadline', 'Batch-impose flow session deadline'), ('end_flow_session', 'End flow session'), ('batch_end_flow_session', 'Batch-end flow sessions'), ('regrade_flow_session', 'Regrade flow session'), ('batch_regrade_flow_session', 'Batch-regrade flow sessions'), ('recalculate_flow_session_grade', 'Recalculate flow session grade'), ('batch_recalculate_flow_session_grade', 'Batch-recalculate flow sesssion grades'), ('reopen_flow_session', 'Reopen flow session'), ('grant_exception', 'Grant exception'), ('view_analytics', 'View analytics'), ('preview_content', 'Preview content'), ('update_content', 'Update content'), ('use_markup_sandbox', 'Use markup sandbox'), ('use_page_sandbox', 'Use page sandbox'), ('test_flow', 'Test flow'), ('edit_events', 'Edit events'), ('query_participation', 'Query participation'), ('edit_participation', 'Edit participation'), ('preapprove_participation', 'Preapprove participation'), ('manage_instant_flow_requests', 'Manage instant flow requests')], db_index=True, max_length=200, verbose_name='Permission'),
        ),
        migrations.AlterField(
            model_name='participationrolepermission',
            name='permission',
            field=models.CharField(choices=[('edit_course', 'Edit course'), ('use_admin_interface', 'Use admin interface'), ('manage_authentication_tokens', 'Manage authentication tokens'), ('impersonate_role', 'Impersonate role'), ('set_fake_time', 'Set fake time'), ('set_pretend_facility', 'Pretend to be in facility'), ('edit_course_permissions', 'Edit course permissions'), ('view_hidden_course_page', 'View hidden course page'), ('view_calendar', 'View calendar'), ('send_instant_message', 'Send instant message'), ('access_files_for', 'Access files for'), ('included_in_grade_statistics', 'Included in grade statistics'), ('skip_during_manual_grading', 'Skip during manual grading'), ('edit_exam', 'Edit exam'), ('issue_exam_ticket', 'Issue exam ticket'), ('batch_issue_exam_ticket', 'Batch issue exam ticket'), ('view_participant_masked_profile', "View participants' masked profile only"), ('view_flow_sessions_from_role', 'View flow sessions from role'), ('view_gradebook', 'View gradebook'), ('edit_grading_opportunity', 'Edit grading opportunity'), ('assign_grade', 'Assign grade'), ('view_grader_stats', 'View grader stats'), ('batch_import_grade', 'Batch-import grades'), ('batch_export_grade', 'Batch-export grades'), ('batch_download_submission', 'Batch-download submissions'), ('impose_flow_session_deadline', 'Impose flow session deadline'), ('batch_impose_flow_session_deadline', 'Batch-impose flow session deadline'), ('end_flow_session', 'End flow session'), ('batch_end_flow_session', 'Batch-end flow sessions'), ('regrade_flow_session', 'Regrade flow session'), ('batch_regrade_flow_session', 'Batch-regrade flow sessions'), ('recalculate_flow_session_grade', 'Recalculate flow session grade'), ('batch_recalculate_flow_session_grade', 'Batch-recalculate flow sesssion grades'), ('reopen_flow_session', 'Reopen flow session'), ('grant_exception', 'Grant exception'), ('view_analytics', 'View analytics'), ('preview_content', 'Preview content'), ('update_content', 'Update content'), ('use_markup_sandbox', 'Use markup sandbox'), ('use_page_sandbox', 'Use page sandbox'), ('test_flow', 'Test flow'), ('edit_events', 'Edit events'), ('query_participation', 'Query participation'), ('edit_participation', 'Edit participation'), ('preapprove_participation', 'Preapprove participation'), ('manage_instant_flow_requests', 'Manage instant flow requests')], db_index=True, max_length=200, verbose_name='Permission'),
        ),
    ]
