\set ON_ERROR_STOP on
BEGIN;
REVOKE ALL PRIVILEGES ON TABLE public.employees, public.clients, public.configs FROM app_user;
GRANT SELECT ON TABLE public.employees, public.clients, public.configs TO app_user;
REVOKE ALL PRIVILEGES ON SEQUENCE public.employees_id_seq, public.clients_id_seq FROM app_user;
REVOKE CREATE, TEMPORARY ON DATABASE corp_data FROM app_user;
REVOKE TEMPORARY ON DATABASE corp_data FROM PUBLIC;
REVOKE CREATE ON SCHEMA public FROM PUBLIC;
COMMIT;
