-- Active: 1714029462031@@baza.fmf.uni-lj.si@5432@sem2024_mihaj@public
GRANT ALL ON DATABASE sem2024_mihaj TO ninaj WITH GRANT OPTION;
GRANT ALL ON SCHEMA public TO ninaj WITH GRANT OPTION;
GRANT ALL ON ALL TABLES IN SCHEMA public TO ninaj WITH GRANT OPTION;
GRANT ALL ON ALL SEQUENCES IN SCHEMA public TO ninaj WITH GRANT OPTION;

GRANT CONNECT ON DATABASE sem2024_mihaj TO javnost;
########################################################################
-- Najprej se prijavite v PostgreSQL kot lastnik baze ali superuser

-- Dodelite vse pravice uporabniku 'javnost'
GRANT ALL PRIVILEGES ON DATABASE sem2024_mihaj TO javnost;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO javnost;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO javnost;
GRANT ALL PRIVILEGES ON ALL FUNCTIONS IN SCHEMA public TO javnost;

-- Dodelite vse pravice uporabniku 'ninaj'
GRANT ALL PRIVILEGES ON DATABASE sem2024_mihaj TO ninaj;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO ninaj;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO ninaj;
GRANT ALL PRIVILEGES ON ALL FUNCTIONS IN SCHEMA public TO ninaj;

-- Dodelite prihodnje pravice na tabelah, sekvencah in funkcijah uporabniku 'javnost'
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL PRIVILEGES ON TABLES TO javnost;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL PRIVILEGES ON SEQUENCES TO javnost;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL PRIVILEGES ON FUNCTIONS TO javnost;

-- Dodelite prihodnje pravice na tabelah, sekvencah in funkcijah uporabniku 'ninaj'
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL PRIVILEGES ON TABLES TO ninaj;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL PRIVILEGES ON SEQUENCES TO ninaj;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL PRIVILEGES ON FUNCTIONS TO ninaj;
