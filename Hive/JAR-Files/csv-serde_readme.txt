CREATE EXTERNAL TABLE w_sbl_s_order_item(
  row_id string COMMENT 'from deserializer',
  created string COMMENT 'from deserializer',
  created_by string COMMENT 'from deserializer',
  last_upd string COMMENT 'from deserializer',
  last_upd_by string COMMENT 'from deserializer',
  x_rel_asset_integ_id string COMMENT 'from deserializer',
  x_support_prod_id string COMMENT 'from deserializer',
  x_support_prov_id string COMMENT 'from deserializer',
  x_survivor_doc_agree_id string COMMENT 'from deserializer',
  x_victim_doc_agree_id string COMMENT 'from deserializer',
  x_cfg_type_cd string COMMENT 'from deserializer',
  x_ship_dt string COMMENT 'from deserializer',
  x_purch_dt string COMMENT 'from deserializer')
ROW FORMAT SERDE
  'com.bizo.hive.serde.csv.CSVSerde'
STORED AS INPUTFORMAT
  'org.apache.hadoop.mapred.TextInputFormat'
OUTPUTFORMAT
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://localtion'