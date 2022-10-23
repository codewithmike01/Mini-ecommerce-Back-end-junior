--
-- PostgreSQL database dump
--

-- Dumped from database version 13.0 (Debian 13.0-4)
-- Dumped by pg_dump version 13.2 (Debian 13.2-1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: mike-savy
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO "mike-savy";

--
-- Name: categories; Type: TABLE; Schema: public; Owner: mike-savy
--

CREATE TABLE public.categories (
    id integer NOT NULL,
    category character varying
);


ALTER TABLE public.categories OWNER TO "mike-savy";

--
-- Name: categories_id_seq; Type: SEQUENCE; Schema: public; Owner: mike-savy
--

CREATE SEQUENCE public.categories_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.categories_id_seq OWNER TO "mike-savy";

--
-- Name: categories_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: mike-savy
--

ALTER SEQUENCE public.categories_id_seq OWNED BY public.categories.id;


--
-- Name: products; Type: TABLE; Schema: public; Owner: mike-savy
--

CREATE TABLE public.products (
    id integer NOT NULL,
    price integer NOT NULL,
    category_id integer NOT NULL,
    sku character varying NOT NULL,
    name character varying NOT NULL,
    measure character varying NOT NULL
);


ALTER TABLE public.products OWNER TO "mike-savy";

--
-- Name: products_id_seq; Type: SEQUENCE; Schema: public; Owner: mike-savy
--

CREATE SEQUENCE public.products_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.products_id_seq OWNER TO "mike-savy";

--
-- Name: products_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: mike-savy
--

ALTER SEQUENCE public.products_id_seq OWNED BY public.products.id;


--
-- Name: categories id; Type: DEFAULT; Schema: public; Owner: mike-savy
--

ALTER TABLE ONLY public.categories ALTER COLUMN id SET DEFAULT nextval('public.categories_id_seq'::regclass);


--
-- Name: products id; Type: DEFAULT; Schema: public; Owner: mike-savy
--

ALTER TABLE ONLY public.products ALTER COLUMN id SET DEFAULT nextval('public.products_id_seq'::regclass);


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: mike-savy
--

COPY public.alembic_version (version_num) FROM stdin;
b85a1e343639
\.


--
-- Data for Name: categories; Type: TABLE DATA; Schema: public; Owner: mike-savy
--

COPY public.categories (id, category) FROM stdin;
1	book
2	dvd
3	furniture
\.


--
-- Data for Name: products; Type: TABLE DATA; Schema: public; Owner: mike-savy
--

COPY public.products (id, price, category_id, sku, name, measure) FROM stdin;
1	20	1	KDFUCK3	shelom Homes	90
3	20	1	KDFUCK4	shelom Homes	90
\.


--
-- Name: categories_id_seq; Type: SEQUENCE SET; Schema: public; Owner: mike-savy
--

SELECT pg_catalog.setval('public.categories_id_seq', 3, true);


--
-- Name: products_id_seq; Type: SEQUENCE SET; Schema: public; Owner: mike-savy
--

SELECT pg_catalog.setval('public.products_id_seq', 3, true);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: mike-savy
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: categories categories_pkey; Type: CONSTRAINT; Schema: public; Owner: mike-savy
--

ALTER TABLE ONLY public.categories
    ADD CONSTRAINT categories_pkey PRIMARY KEY (id);


--
-- Name: products products_pkey; Type: CONSTRAINT; Schema: public; Owner: mike-savy
--

ALTER TABLE ONLY public.products
    ADD CONSTRAINT products_pkey PRIMARY KEY (id);


--
-- Name: products products_sku_key; Type: CONSTRAINT; Schema: public; Owner: mike-savy
--

ALTER TABLE ONLY public.products
    ADD CONSTRAINT products_sku_key UNIQUE (sku);


--
-- Name: products products_category_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: mike-savy
--

ALTER TABLE ONLY public.products
    ADD CONSTRAINT products_category_id_fkey FOREIGN KEY (category_id) REFERENCES public.categories(id);


--
-- PostgreSQL database dump complete
--

