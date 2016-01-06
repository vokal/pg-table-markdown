### app_email_change_request 

Column | Type | Default | Nullable 
--- | --- | --- | --- 
id | integer | nextval('app_email_change_request_id_seq'::regclass) | NO 
user_id | integer | None | YES 
new_email | character varying | None | NO 
code | character varying | None | NO 
expires | timestamp without time zone | (timezone('utc'::text, now()) + '1 day'::interval) | YES 

### app_password_reset 

Column | Type | Default | Nullable 
--- | --- | --- | --- 
id | integer | nextval('app_password_reset_id_seq'::regclass) | NO 
user_id | integer | None | YES 
code | character varying | None | NO 
expires | timestamp without time zone | (timezone('utc'::text, now()) + '1 day'::interval) | YES 
code_used | boolean | false | YES 

### app_push_tokens 

Column | Type | Default | Nullable 
--- | --- | --- | --- 
id | integer | nextval('app_push_tokens_id_seq'::regclass) | NO 
user_id | integer | None | YES 
token | character varying | None | NO 
type | character varying | None | NO 
sns_arn | character varying | None | NO 
created | timestamp without time zone | timezone('utc'::text, now()) | YES 

### app_users 

Column | Type | Default | Nullable 
--- | --- | --- | --- 
id | integer | nextval('app_users_id_seq'::regclass) | NO 
email | character varying | None | NO 
password | character varying | None | YES 
is_active | boolean | true | YES 
is_admin | boolean | false | YES 
