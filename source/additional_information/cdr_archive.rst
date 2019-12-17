###################
CDR Archive Server
###################

* Note: This feature is on version 4.5+ and requires PostgreSQL ver 9.5+
| Fusionpbx has the ability to access CDR records on a seperate archive database. This is helpful for longterm CDR storage while keeping your active database small. When the feature is enabled you will see an "ARCHIVE" button in CDR page that accesses records on your archive database. 

| The first step is to install an archive database. This can be done by standing up another fusionpbx server or by setting up a postgres server. If postgres is installed by itself you will need to manage the indexes, tables names and column names manually on the archive server. They need to match the values on the live database. 

| Once you get your archive database setup and can access both databases in both directions (live <-> archive), you will need a mechanism to move the CDR Records from the live database to the archive database. In this example I have a complete fusionpbx install on the archive server. That way I can use the fusionpbx web gui to explore the records and use the Upgrade feature to keep the table & column names in sync. 

|

**Move the Records**
^^^^^^^^^^^^^^^^^^^^

| Create a shell script to copy the records. 

| ``touch /etc/cron.daily/db_copy.sh``
| ``chmod +x /etc/cron.daily/db_copy.sh``
| ``nano /etc/cron.daily/db_copy.sh``

::

 #!/bin/sh
 
 #copy the data from the fusion db to a local csv file
 psql --host=x.x.x --username=fusionpbx -c "\copy (SELECT * FROM v_domains) TO '/tmp/domains.csv' WITH CSV"
 psql --host=x.x.x --username=fusionpbx -c "\copy (SELECT * FROM v_fax_logs) TO '/tmp/fax_logs.csv' WITH CSV"
 psql --host=x.x.x --username=fusionpbx -c "\copy (SELECT * FROM v_xml_cdr) TO '/tmp/xml_cdr.csv' WITH CSV"
 psql --host=x.x.x --username=fusionpbx -c "\copy (SELECT * FROM v_conference_sessions) TO '/tmp/conference_sessions.csv' WITH CSV"
 psql --host=x.x.x --username=fusionpbx -c "\copy (SELECT * FROM v_conference_session_details) TO '/tmp/conference_session_details.csv' WITH CSV"
 
 #Insert the data into the cdr server
 # - create a temp tables
 # - copy the csv data to the temp tables
 # - insert data from the temp table to the real tables
 # - delete the temp tables
 # - remove the json data from the cdrs. too much space
 psql --host=x.x.x.x --username=fusionpbx << EOF
 
 CREATE TEMP TABLE tmp_domains AS SELECT * FROM v_domains WITH NO DATA;
 CREATE TEMP TABLE tmp_fax_logs AS SELECT * FROM v_fax_logs WITH NO DATA;
 CREATE TEMP TABLE tmp_xml_cdr AS SELECT * FROM v_xml_cdr WITH NO DATA;
 CREATE TEMP TABLE tmp_conference_sessions AS SELECT * FROM v_conference_sessions WITH NO DATA;
 CREATE TEMP TABLE tmp_conference_session_details AS SELECT * FROM v_conference_session_details WITH NO DATA; 
 
 COPY tmp_domains FROM '/tmp/domains.csv' DELIMITER ',' CSV HEADER;
 COPY tmp_fax_logs FROM '/tmp/fax_logs.csv' DELIMITER ',' CSV HEADER;
 COPY tmp_xml_cdr FROM '/tmp/xml_cdr.csv' DELIMITER ',' CSV HEADER;
 COPY tmp_conference_sessions FROM '/tmp/conference_sessions.csv' DELIMITER ',' CSV HEADER;
 COPY tmp_conference_session_details FROM '/tmp/conference_session_details.csv' DELIMITER ',' CSV HEADER;
 
 INSERT INTO v_domains SELECT DISTINCT ON (domain_uuid) * FROM tmp_domains ON CONFLICT DO NOTHING;
 INSERT INTO v_fax_logs SELECT DISTINCT ON (fax_log_uuid) * FROM tmp_fax_logs ON CONFLICT DO NOTHING;
 INSERT INTO v_xml_cdr SELECT DISTINCT ON (xml_cdr_uuid) * FROM tmp_xml_cdr ON CONFLICT DO NOTHING;
 INSERT INTO v_conference_sessions SELECT DISTINCT ON (conference_session_uuid) * FROM tmp_conference_sessions ON CONFLICT DO NOTHING;
 INSERT INTO v_conference_session_details SELECT DISTINCT ON (conference_session_detail_uuid) * FROM tmp_conference_session_details ON CONFLICT DO NOTHING;
 
 DROP TABLE tmp_domains;
 DROP TABLE tmp_fax_logs;
 DROP TABLE tmp_xml_cdr;
 DROP TABLE tmp_conference_sessions;
 DROP TABLE tmp_conference_session_details;
 
 UPDATE v_xml_cdr SET json = NULL;
 
 EOF
 
 #remove the csv files
 rm /tmp/domains.csv
 rm /tmp/fax_logs.csv
 rm /tmp/xml_cdr.csv
 rm /tmp/conference_sessions.csv
 rm /tmp/conference_session_details.csv
 
 
| Add to cron 

| ``crontab -e``

::

 15 0 * * * bash /etc/cron.daily/db_copy.sh
 
* Note: In this example I remove the json data from the records. You will need to comment out the "SET json = NULL" line if you want to keep the call variables. 

`CDR <default_settings/cdr.html>`_
=======================================

FusionPBX menu `Apps > CDR <../applications/call_detail_record.html>`_

Setup your live server to connect to the archive database. 

+-------------------------------+------------------------+-------------------------+---------------------------+--------------------------------------+
| Default Setting Subcategory   | Default Setting Name   | Default Setting Value   | Setting Enabled           | Default Setting Description          |
+===============================+========================+=========================+===========================+======================================+
| archive_database_driver       | text                   | pgsql                   | TRUE                      | Archive Database Driver              |
+-------------------------------+------------------------+-------------------------+---------------------------+--------------------------------------+
| archive_database_host         | text                   | x.x.x.x                 | TRUE                      | IP/Hostname of Archive Database      |
+-------------------------------+------------------------+-------------------------+---------------------------+--------------------------------------+
| archive_database_password     | text                   | somethingSecret         | TRUE                      | Archive Database Password            |
+-------------------------------+------------------------+-------------------------+---------------------------+--------------------------------------+
| archive_database_port         | text                   | 5432                    | TRUE                      | Archive Database Port                |
+-------------------------------+------------------------+-------------------------+---------------------------+--------------------------------------+
| archive_database_username     | text                   | fusionpbx               | TRUE                      | Archive Database Username            |
+-------------------------------+------------------------+-------------------------+---------------------------+--------------------------------------+
| archive_database              | boolean                | TRUE                    | FALSE                     | Enable Dedicated CDR Database Access |
+-------------------------------+------------------------+-------------------------+---------------------------+--------------------------------------+
| archive_database_name         | text                   | fusionpbx               | FALSE                     | Archive Database Name                |
+-------------------------------+------------------------+-------------------------+---------------------------+--------------------------------------+
